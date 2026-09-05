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
    """Halaman Deteksi Baru - Input Data dengan pilihan Kamera / Upload File"""

    st.markdown(
        '<p class="sekulit-subheading" style="font-weight:700; margin-bottom: 12px; color:#4a3525;">Input Data Pengguna</p>',
        unsafe_allow_html=True,
    )

    # 1. Pilihan Metode Input Gambar (Upload vs Kamera)
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#4a3525; margin-bottom:4px; margin-top:10px;">Metode Ambil Gambar Lesi Kulit</p>',
        unsafe_allow_html=True,
    )

    metode_input = st.radio(
        "Metode Input Gambar",
        options=["Unggah File", "Kamera Langsung"],
        key="input_metode_gambar",
        horizontal=True,
        label_visibility="collapsed",
    )

    image_source = None

    if metode_input == "Unggah File":
        image_source = st.file_uploader(
            "Unggah Foto Lesi Kulit",
            type=["jpg", "jpeg", "png"],
            key="input_foto_upload",
            label_visibility="collapsed",
        )
    else:
        image_source = st.camera_input(
            "Ambil Foto Lesi Kulit",
            key="input_foto_kamera",
            label_visibility="collapsed",
        )

    # 2. Umur
    st.markdown(
        '<p style="font-size:12px; font-weight:700; color:#4a3525; margin-bottom:2px; margin-top:10px;">Umur</p>',
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
        '<p style="font-size:12px; font-weight:700; color:#4a3525; margin-bottom:2px; margin-top:10px;">Jenis Kelamin</p>',
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
        '<p style="font-size:12px; font-weight:700; color:#4a3525; margin-bottom:2px; margin-top:10px;">Lokasi Lesi</p>',
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

    # 5. Tombol Proses Estimasi & Validasi Gambar
    if st.button(
        "Proses Estimasi",
        type="primary",
        key="btn_proses_estimasi",
        use_container_width=True,
    ):
        # Validasi 1: Jika Pengguna Belum Memasukkan Gambar
        if image_source is None:
            st.toast("⚠️ Harap unggah atau ambil foto terlebih dahulu!")
            return

        with st.spinner("Menganalisis gambar dan data pasien..."):
            estimation_result = predict_skin_disease(
                image_file=image_source,
                age=st.session_state.get("input_usia"),
                gender=st.session_state.get("input_gender"),
                location=st.session_state.get("input_lokasi_lesi"),
            )

            # Validasi 2: Jika Gambar Ditolak oleh AI (Bukan Kulit Bermasalah / Gambar Buram)
            if not estimation_result.get("is_valid", False):
                st.error(
                    "⚠️ **Gambar Tidak Valid / Tidak Terdeteksi!**\n\n"
                    "Sistem tidak mendeteksi area lesi/kelainan kulit pada foto ini. "
                    "Harap unggah atau ambil foto baru yang lebih dekat, jelas, dan fokus pada area kulit bermasalah."
                )
                return

            # Jika Valid, Simpan dan Pindah Halaman
            st.session_state.estimation_result = estimation_result
            go_to("cek_kulit_output")
