import os

# Set variabel lingkungan sebelum mengimpor tf_keras
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import joblib
import numpy as np
from PIL import Image
import streamlit as st
import tf_keras as keras


# ------------------------------------------------------------------------
# PATCH KOMPATIBILITAS KERAS 3 METADATA (.h5) KE TF_KERAS (KERAS 2)
# ------------------------------------------------------------------------
class PatchedInputLayer(keras.layers.InputLayer):
    """Mengubah kunci 'batch_shape' dari Keras 3 menjadi 'batch_input_shape'."""

    def __init__(self, *args, **kwargs):
        if "batch_shape" in kwargs:
            kwargs["batch_input_shape"] = kwargs.pop("batch_shape")
        super().__init__(*args, **kwargs)


class DTypePolicy(keras.mixed_precision.Policy):
    """Menerjemahkan DTypePolicy dari Keras 3 agar dapat dibaca oleh tf_keras."""

    def __init__(self, name="float32", **kwargs):
        if isinstance(name, dict):
            name = name.get("name", "float32")
        super().__init__(str(name))

    @classmethod
    def from_config(cls, config):
        name = (
            config.get("name", "float32")
            if isinstance(config, dict)
            else config
        )
        return cls(name)


# Path File Model di folder 'models/'
RESNET_PATH = "models/best_resnet50_finetuned_model.h5"
INCEPTION_PATH = "models/final_inceptionv3_finetuned_model.h5"
META_LEARNER_PATH = "models/meta_learner.pkl"

# Preprocessing spesifik arsitektur Keras
PREPROCESS_INC = keras.applications.inception_v3.preprocess_input
PREPROCESS_RES = keras.applications.resnet50.preprocess_input

# Mapping kelas sesuai urutan alfabetis Keras ImageDataGenerator (0-6)
DISEASE_CLASSES = {
    0: {
        "label": "Actinic Keratoses (AKIEC)",
        "description": (
            "Bercak bersisik pada kulit akibat paparan sinar matahari jangka"
            " panjang."
        ),
    },
    1: {
        "label": "Basal Cell Carcinoma (BCC)",
        "description": "Jenis kanker kulit paling umum yang tumbuh lambat.",
    },
    2: {
        "label": "Benign Keratosis (BKL)",
        "description": "Pertumbuhan kulit jinak non-kanker seiring usia.",
    },
    3: {
        "label": "Dermatofibroma (DF)",
        "description": (
            "Benjolan jinak di bawah kulit yang keras dan berwarna cokelat."
        ),
    },
    4: {
        "label": "Melanoma (MEL)",
        "description": (
            "Jenis kanker kulit serius dari sel pigmen yang membutuhkan"
            " penanganan cepat."
        ),
    },
    5: {
        "label": "Melanocytic Nevi / Tahi Lalat (NV)",
        "description": "Tahi lalat normal yang bersifat jinak.",
    },
    6: {
        "label": "Vascular Lesions (VASC)",
        "description": (
            "Gangguan pembuluh darah di kulit seperti tanda lahir merah yang"
            " umumnya jinak."
        ),
    },
}


@st.cache_resource
def load_all_models():
    """Memuat InceptionV3, ResNet50, dan Meta-Learner ke memori."""
    # Mendaftarkan seluruh patch kompatibilitas Keras 3 -> Keras 2
    custom_objs = {
        "InputLayer": PatchedInputLayer,
        "DTypePolicy": DTypePolicy,
    }

    inc_model = (
        keras.models.load_model(
            INCEPTION_PATH, compile=False, custom_objects=custom_objs
        )
        if os.path.exists(INCEPTION_PATH)
        else None
    )
    res_model = (
        keras.models.load_model(
            RESNET_PATH, compile=False, custom_objects=custom_objs
        )
        if os.path.exists(RESNET_PATH)
        else None
    )
    meta_learner = (
        joblib.load(META_LEARNER_PATH)
        if os.path.exists(META_LEARNER_PATH)
        else None
    )

    return inc_model, res_model, meta_learner


def prepare_metadata_vector(age, gender, location, expected_dim=18):
    """Mengonversi input UI menjadi vektor metadata tanpa merusak distribusi fitur."""
    real_age = float(age) if age is not None and age != "" else 45.0

    # Normalisasi usia standar (HAM10000 rentang 0-100)
    age_normalized = real_age / 100.0

    gender_male = 1.0 if gender == "Laki-Laki" else 0.0
    gender_female = 1.0 if gender == "Perempuan" else 0.0

    meta_list = [age_normalized, gender_male, gender_female]

    # Padding dengan nilai netral/0 jika dimensi kurang
    if len(meta_list) < expected_dim:
        meta_list.extend([0.0] * (expected_dim - len(meta_list)))
    elif len(meta_list) > expected_dim:
        meta_list = meta_list[:expected_dim]

    return np.array(meta_list, dtype=np.float32).reshape(1, -1)


def get_meta_dim(model, default_dim=18):
    """Mendeteksi jumlah fitur metadata yang dibutuhkan model dasar."""
    try:
        if isinstance(model.input, list) and len(model.input) > 1:
            return model.input[1].shape[1]
    except Exception:
        pass
    return default_dim


def predict_skin_disease(
    image_file, age=None, gender=None, location=None, mc_iter=15
):
    """Prediksi Stacking Ensemble (Akurasi Tinggi) + Monte Carlo Uncertainty."""
    inc_model, res_model, meta_learner = load_all_models()

    if inc_model is None or res_model is None or meta_learner is None:
        return {
            "label": "Vascular Lesions (Simulasi Demo)",
            "description": (
                "File model '.h5' atau 'meta_learner.pkl' belum ditemukan di"
                " folder 'models/'."
            ),
            "confidence": 85.21,
            "uncertainty": 14.79,
        }

    # 1. Load dan Persiapan Gambar
    img = Image.open(image_file).convert("RGB")

    try:
        inc_shape = (
            int(inc_model.input[0].shape[2]),
            int(inc_model.input[0].shape[1]),
        )
    except Exception:
        inc_shape = (224, 224)

    try:
        res_shape = (
            int(res_model.input[0].shape[2]),
            int(res_model.input[0].shape[1]),
        )
    except Exception:
        res_shape = (128, 128)

    # Preprocessing Gambar
    img_inc_raw = np.array(img.resize(inc_shape), dtype=np.float32)
    img_res_raw = np.array(img.resize(res_shape), dtype=np.float32)

    img_inc = PREPROCESS_INC(np.expand_dims(img_inc_raw, axis=0))
    img_res = PREPROCESS_RES(np.expand_dims(img_res_raw, axis=0))

    # Vektor Metadata
    inc_meta_dim = get_meta_dim(inc_model, default_dim=18)
    res_meta_dim = get_meta_dim(res_model, default_dim=17)

    meta_vec_inc = prepare_metadata_vector(
        age, gender, location, expected_dim=inc_meta_dim
    )
    meta_vec_res = prepare_metadata_vector(
        age, gender, location, expected_dim=res_meta_dim
    )

    # ------------------------------------------------------------------------
    # 2. PREDIKSI UTAMA (training=False) -> Menjaga Akurasi Asli (85%)
    # ------------------------------------------------------------------------
    p_inc_main = inc_model([img_inc, meta_vec_inc], training=False).numpy()
    p_res_main = res_model([img_res, meta_vec_res], training=False).numpy()

    x_meta_main = np.hstack((p_inc_main, p_res_main))
    main_probs = meta_learner.predict_proba(x_meta_main)[0]

    pred_class = int(np.argmax(main_probs))
    confidence = float(main_probs[pred_class]) * 100.0

    # ------------------------------------------------------------------------
    # 3. ESTIMASI UNCERTAINTY (Monte Carlo Perturbation)
    # ------------------------------------------------------------------------
    mc_preds = []
    rng = np.random.default_rng(seed=42)

    for _ in range(mc_iter):
        # Penambahan variasi noise kecil pada input gambar untuk simulasi variabilitas MC
        noise_inc = rng.normal(0, 0.02, img_inc.shape).astype(np.float32)
        noise_res = rng.normal(0, 0.02, img_res.shape).astype(np.float32)

        p_inc_mc = inc_model(
            [img_inc + noise_inc, meta_vec_inc], training=False
        ).numpy()
        p_res_mc = res_model(
            [img_res + noise_res, meta_vec_res], training=False
        ).numpy()

        x_meta_mc = np.hstack((p_inc_mc, p_res_mc))
        p_meta_mc = meta_learner.predict_proba(x_meta_mc)[0]
        mc_preds.append(p_meta_mc)

    mc_preds = np.array(mc_preds)
    uncertainty = float(np.std(mc_preds[:, pred_class])) * 100.0

    # Retrieve Detail Penyakit
    disease_info = DISEASE_CLASSES.get(
        pred_class,
        {
            "label": f"Kelas {pred_class}",
            "description": "Deskripsi kondisi belum tersedia.",
        },
    )

    return {
        "label": disease_info["label"],
        "description": disease_info["description"],
        "confidence": round(confidence, 2),
        "uncertainty": round(uncertainty, 2),
    }
