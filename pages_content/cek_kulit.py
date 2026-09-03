import streamlit as st
from model_helper import predict_skin_disease
from state import go_to

LOKASI_LESI_OPTIONS = {
    "abdomen": "abdomen: Perut",
    "acral": "acral: Bagian ujung/ekstremitas (seperti jemari, telinga, hidung)",
    "back": "back: Punggung",
    "chest": "chest: Dada",
    "ear": "ear: Telinga",
    "face": "face: Wajah",
    "foot": "foot: Kaki",
    "genital": "genital: Area kelamin / Genital",
    "hand": "hand: Tangan",
    "lower extremity": "lower extremity: Anggota gerak bawah (tungkai / kaki bawah)",
    "neck": "neck: Leher",
    "scalp": "scalp: Kulit kepala",
    "trunk": "trunk: Batang tubuh (termasuk dada, perut, dan punggung)",
    "unknown": "unknown: Tidak diketahui",
    "upper extremity": "upper extremity: Anggota gerak atas (lengan / tangan atas)",
}


def render_input():
    """Halaman Deteksi Baru - Input Data dengan teks gelap"""
    # ===== CSS lokal untuk memaksa semua teks gelap =====
    st.markdown(
        """
        <style>
        /* Container utama */
        .cek-kulit-container {
            color: #000000 !important;
        }
        /* Semua label, teks, div di dalam container */
        .cek-kulit-container label,
        .cek-kulit-container .stNumberInput label,
        .cek-kulit-container .stRadio label,
        .cek-kulit-container .stSelectbox label,
        .cek-kulit-container .stFileUploader label,
        .cek-kulit-container .stMarkdown p,
        .cek-kulit-container .stMarkdown div,
        .cek-kulit-container span,
        .cek-kulit-container .stFileUploader div,
        .cek-kulit-container .stRadio div[role="radiogroup"] label,
        .cek-kulit-container .stFileUploader span {
            color: #FFFFFF !important;
        }
        /* Placeholder text */
        .cek-kulit-container input::placeholder,
        .cek-kulit-container textarea::placeholder {
            color: #000000 !important;
            opacity: 0.7 !important;
        }
        /* Teks di file uploader (ukuran file, batas) */
        .cek-kulit-container .stFileUploader div[data-testid="stFileUploaderDropzone"] p,
        .cek-kulit-container .stFileUploader div[data-testid="stFileUploaderDropzone"] span,
        .cek-kulit-container .stFileUploader div[data-testid="stFileUploaderDropzone"] small {
            color: #000000 !important;
        }
        /* Teks di radio button options */
        .cek-kulit-container .stRadio div[role="radiogroup"] label div p {
            color: #000000 !important;
        }
        /* Selectbox options */
        .cek-kulit-container .stSelectbox div[data-baseweb="select"] {
            color: #000000 !important;
        }
        /* Number input */
        .cek-kulit-container .stNumberInput input {
            color: #000000 !important;
        }
        </style>
        <div class="cek-kulit-container">
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="sekulit-subheading" style="font-weight:700; margin-bottom: 12px; color:#000000;">Input Data Pengguna</p>',
        unsafe_allow_html=True,
    )

    # 1. Upload gambar
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#000000; margin-bottom:2px; margin-top:10px;">Unggah Foto Lesi Kulit</p>',
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        "Unggah Foto Lesi Kulit",
        type=["jpg", "jpeg", "png"],
        key="input_foto",
        label_visibility="collapsed",
    )

    # 2. Umur
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#000000; margin-bottom:2px; margin-top:10px;">Umur</p>',
        unsafe_allow_html=True,
    )
    st.number_input(
        "Umur",
        key="input_usia",
        min_value=0,
        max_value=120,
        value=None,
        placeholder="Angka",
        label_visibility="collapsed",
    )

    # 3. Jenis Kelamin
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#000000; margin-bottom:2px; margin-top:10px;">Jenis Kelamin</p>',
        unsafe_allow_html=True,
    )
    st.radio(
        "Jenis Kelamin",
        options=["Laki-Laki", "Perempuan"],
        key="input_gender",
        horizontal=True,
        label_visibility="collapsed",
    )

    # 4. Lokasi Lesi
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#000000; margin-bottom:2px; margin-top:10px;">Lokasi Lesi</p>',
        unsafe_allow_html=True,
    )
    st.selectbox(
        "Lokasi Lesi",
        options=list(LOKASI_LESI_OPTIONS.keys()),
        format_func=lambda x: LOKASI_LESI_OPTIONS[x],
        placeholder="Wajah, Lengan, Kaki, dll.",
        index=None,
        key="input_lokasi_lesi",
        label_visibility="collapsed",
    )

    st.write("")

    # 5. Tombol Proses Estimasi
    if st.button(
        "Proses Estimasi",
        type="primary",
        key="btn_proses_estimasi",
        use_container_width=True,
    ):
        if uploaded_file is None:
            st.toast("Silakan unggah foto lesi kulit terlebih dahulu!", icon="⚠️")
            return

        with st.spinner("Menganalisis gambar dan data pasien..."):
            estimation_result = predict_skin_disease(
                image_file=uploaded_file,
                age=st.session_state.get("input_usia"),
                gender=st.session_state.get("input_gender"),
                location=st.session_state.get("input_lokasi_lesi"),
            )
            st.session_state.estimation_result = estimation_result
            go_to("cek_kulit_output")

    st.markdown("</div>", unsafe_allow_html=True)  # tutup container


def render_output():
    """Halaman Hasil Estimasi"""
    result = st.session_state.get("estimation_result") or {
        "label": "Vascular Lesions",
        "description": "Vascular Lesions adalah kondisi terkait gangguan atau kelainan pada pembuluh darah di kulit, seperti tanda lahir merah atau pelebaran pembuluh darah yang umumnya bersifat jinak.",
        "confidence": 85.21,
        "uncertainty": 14.79,
    }

    # Card Judul Estimasi
    st.markdown(
        f"""
        <div class="sekulit-card" style="text-align: center; padding: 18px 12px; border-radius: 16px;">
            <h3 style="margin: 0; font-size: 20px; font-weight: 700; color: #000000;">{result["label"]}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Deskripsi Penyakit
    st.markdown(
        f"""
        <p style="font-size: 11px; color: #000000; line-height: 1.4; text-align: justify; margin: 10px 0 14px 0;">
            {result["description"]}
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Bar Confidence Score
    st.markdown(
        '<p style="font-size: 12px; font-weight: 700; color: #000000; margin-bottom: 4px;">Confidence Score</p>',
        unsafe_allow_html=True,
    )
    conf_val = result["confidence"]
    st.markdown(
        f"""
        <div style="background-color: #e8ded5; border-radius: 12px; height: 32px; width: 100%; position: relative; overflow: hidden; margin-bottom: 12px;">
            <div style="background-color: #f3a88c; width: {conf_val}%; height: 100%; border-radius: 12px; display: flex; align-items: center; padding-left: 12px;">
                <span style="font-size: 12px; font-weight: 700; color: #000000;">{conf_val:.2f}%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bar Uncertainty Level
    st.markdown(
        '<p style="font-size: 12px; font-weight: 700; color: #000000; margin-bottom: 4px;">Uncertainty Level</p>',
        unsafe_allow_html=True,
    )
    uncert_val = result["uncertainty"]
    st.markdown(
        f"""
        <div style="background-color: #e8ded5; border-radius: 12px; height: 32px; width: 100%; position: relative; overflow: hidden; margin-bottom: 14px;">
            <div style="background-color: #f3a88c; width: {uncert_val}%; height: 100%; border-radius: 12px; display: flex; align-items: center; padding-left: 12px;">
                <span style="font-size: 12px; font-weight: 700; color: #000000;">{uncert_val:.2f}%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card Saran
    st.markdown(
        '<p style="font-size: 12px; font-weight: 700; color: #000000; margin-bottom: 6px;">Saran Berdasarkan Hasil Estimasi</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="sekulit-card" style="padding: 12px; border-radius: 16px; margin-bottom: 12px;">
            <p style="font-size: 11px; color: #000000; margin: 0; line-height: 1.4;">
                Hindari memanipulasi atau mengobati sendiri area kulit tersebut, dan konsultasikan ke dokter spesialis kulit guna mendapatkan pemeriksaan yang akurat.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Box Peringatan Medis
    st.markdown(
        """
        <div style="background-color: #fce8cc; border: 1px solid #f7d098; border-radius: 14px; padding: 10px 12px; display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
            <span style="font-size: 20px;">⚠️</span>
            <p style="font-size: 10px; color: #000000; margin: 0; line-height: 1.3;">
                <b>Penting:</b> Hasil ini merupakan estimasi dini berbasis analisis machine learning dan bukan merupakan diagnosis medis mutlak.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tombol Aksi Bawah
    col1, col2 = st.columns(2, gap="small")
    with col1:
        if st.button("Simpan Hasil", key="out_simpan", use_container_width=True):
            st.toast("Hasil berhasil disimpan!")
    with col2:
        if st.button(
            "Konsultasi Dokter",
            type="primary",
            key="out_ke_konsultasi",
            use_container_width=True,
        ):
            go_to("konsultasi_list")