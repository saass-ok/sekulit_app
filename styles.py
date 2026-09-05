import os
import streamlit as st

# ===================== DATA 7 PENYAKIT (TANPA EMOJI) =====================
DISEASES = [
    {
        "id": "melanocytic_nevi",
        "name": "Melanocytic Nevi",
        "image_url": "assets/Melanocytic Nevi.jpg",
        "description": "Melanocytic Nevi adalah pertumbuhan jinak pada kulit yang terbentuk dari penumpukan sel pigmen (melanosit), atau yang secara umum dikenal masyarakat sebagai tahi lalat biasa.",
        "obat": "Kondisi ini tidak dapat disembuhkan atau dihilangkan menggunakan obat minum maupun salep topikal. Sangat dilarang menggunakan cairan atau krim penghilang tahi lalat yang dijual bebas di pasaran, karena berisiko tinggi memicu luka bakar kimia, infeksi, hingga kerusakan jaringan kulit permanen.",
        "penanganan": "Jika tahi lalat terasa mengganggu secara estetika atau sering mengalami iritasi akibat gesekan, penanganan terbaik adalah melakukan tindakan medis aman (seperti laser atau bedah minor) oleh dokter spesialis kulit. Untuk perawatan mandiri, cukup gunakan tabir surya (sunscreen) secara rutin guna melindungi tahi lalat dari paparan radiasi UV.",
    },
    {
        "id": "basal_cell_carcinoma",
        "name": "Basal Cell Carcinoma",
        "image_url": "assets/Basal Cell Carcinoma.jpg",
        "description": "Basal Cell Carcinoma (BCC) adalah jenis kanker kulit paling umum yang tumbuh lambat dan jarang menyebar ke bagian tubuh lain. Biasanya muncul sebagai benjolan berkilau atau luka yang tidak sembuh-sembuh.",
        "obat": "Pengobatan BCC umumnya melalui tindakan bedah eksisi, krioterapi, atau terapi topikal seperti imiquimod atau fluorouracil untuk kasus superfisial. Konsultasi dengan dokter spesialis kulit sangat dianjurkan.",
        "penanganan": "Deteksi dini sangat penting. Jika menemukan luka yang tidak sembuh dalam 4 minggu, segera periksakan ke dokter. Gunakan sunscreen setiap hari untuk mencegah kekambuhan.",
    },
    {
        "id": "melanoma",
        "name": "Melanoma",
        "image_url": "assets/Melanoma.jpg",
        "description": "Melanoma adalah jenis kanker kulit paling serius yang berasal dari sel pigmen (melanosit). Dapat muncul dari tahi lalat yang berubah bentuk, warna, atau ukuran, atau muncul sebagai bintik baru.",
        "obat": "Pengobatan melanoma memerlukan tindakan bedah eksisi luas, imunoterapi, terapi target, atau kemoterapi tergantung stadium. Penanganan harus segera dilakukan oleh ahli onkologi kulit.",
        "penanganan": "Perhatikan tanda ABCDE: Asimetri, Batas tidak rata, Warna tidak merata, Diameter >6mm, Evolusi (berubah). Segera periksa ke dokter jika ada perubahan.",
    },
    {
        "id": "actinic_keratoses",
        "name": "Actinic Keratoses",
        "image_url": "assets/Actinic Keratoses.jpg",
        "description": "Actinic Keratoses (AK) adalah bercak bersisik pada kulit akibat paparan sinar matahari jangka panjang. Merupakan lesi pra-kanker yang dapat berkembang menjadi squamous cell carcinoma jika tidak ditangani.",
        "obat": "Pengobatan AK meliputi krioterapi, terapi topikal (5-fluorouracil, imiquimod, atau diclofenac), dan fotodinamik terapi. Konsultasi dokter untuk penanganan terbaik.",
        "penanganan": "Lindungi kulit dari sinar matahari dengan sunscreen SPF 30+, gunakan pakaian pelindung, dan hindari paparan sinar UV berlebihan. Lakukan pemeriksaan kulit rutin.",
    },
    {
        "id": "benign_keratosis",
        "name": "Benign Keratosis",
        "image_url": "assets/Benign Keratosis-like Lesions.jpg",
        "description": "Benign Keratosis (BKL) adalah pertumbuhan kulit jinak yang umum terjadi seiring bertambahnya usia. Biasanya muncul sebagai bercak cokelat atau hitam dengan permukaan kasar seperti kutil.",
        "obat": "BKL tidak memerlukan pengobatan khusus karena bersifat jinak. Namun jika mengganggu secara estetika atau sering iritasi, dapat dilakukan krioterapi atau eksisi minor oleh dokter.",
        "penanganan": "Cukup lakukan observasi rutin. Gunakan pelembab untuk menjaga kulit tetap lembab dan hindari menggaruk atau mengiritasi lesi.",
    },
    {
        "id": "vascular_lesions",
        "name": "Vascular Lesions",
        "image_url": "assets/Vascular Lesions.jpg",
        "description": "Vascular Lesions (VASC) adalah gangguan pembuluh darah di kulit yang tampak sebagai bercak merah, ungu, atau kemerahan. Contohnya adalah hemangioma, port-wine stain, atau spider angioma. Umumnya bersifat jinak.",
        "obat": "Pengobatan vascular lesions tergantung jenisnya. Laser pulsed dye laser (PDL) adalah terapi utama untuk lesi vaskular. Krim topikal seperti timolol dapat digunakan untuk hemangioma infantile.",
        "penanganan": "Konsultasi dengan dokter kulit untuk diagnosis dan terapi yang tepat. Lindungi kulit dari trauma untuk mencegah perdarahan.",
    },
    {
        "id": "dermatofibroma",
        "name": "Dermatofibroma",
        "image_url": "assets/Dermatofibroma.jpg",
        "description": "Dermatofibroma (DF) adalah benjolan jinak di bawah kulit yang keras dan berwarna cokelat. Sering muncul di tungkai bawah dan biasanya tidak menimbulkan gejala, meskipun kadang terasa gatal atau nyeri.",
        "obat": "DF tidak memerlukan pengobatan karena bersifat jinak. Jika menimbulkan gejala atau mengganggu, dapat dilakukan eksisi bedah minor oleh dokter kulit.",
        "penanganan": "Hindari menggaruk atau menekan benjolan. Jika ukuran atau warna berubah, segera periksakan ke dokter untuk memastikan tidak ada keganasan.",
    },
]


def render():
    """Halaman rekomendasi obat – detail kartu rapi, presisi & proporsional."""

    selected_id = st.session_state.get("selected_disease")
    if selected_id:
        selected = next((d for d in DISEASES if d["id"] == selected_id), None)
        if selected:
            # Space atas agar tidak mepet ke header
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

            with st.container(border=True):
                # 1 & 2. HEADER: Judul di Tengah (Center), Tombol X Presisi di Pojok Kanan
                col_spacer, col_title, col_close = st.columns([1, 8, 1])
                
                with col_title:
                    st.markdown(
                        f'<h3 style="color:#4a3525; margin:0; font-size:16px; font-weight:700; text-align:center; line-height:28px;">{selected["name"]}</h3>',
                        unsafe_allow_html=True,
                    )
                with col_close:
                    if st.button("✕", key="close_detail", help="Tutup detail"):
                        st.session_state.selected_disease = None
                        st.rerun()

                st.markdown(
                    "<hr style='margin: 10px 0 14px 0; border: none; border-top: 1px solid #ecdfd4;'>",
                    unsafe_allow_html=True,
                )

                # BARIS 1: Gambar (Kiri) & Deskripsi (Kanan)
                col_img, col_desc = st.columns([1, 1])

                with col_img:
                    if os.path.exists(selected["image_url"]):
                        st.image(selected["image_url"], use_container_width=True)
                    else:
                        st.markdown(
                            '<div style="text-align:center; color:#8a7a6d; padding:20px 0;">[ Gambar ]</div>',
                            unsafe_allow_html=True,
                        )

                with col_desc:
                    st.markdown(
                        '<h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px; font-weight:700;">Deskripsi</h4>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11.5px; line-height:1.35;">{selected["description"]}</p>',
                        unsafe_allow_html=True,
                    )

                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

                # BARIS 2: Rekomendasi Obat & Penanganan Tepat (Dibuat Sejajar Menggunakan Top Alignment)
                col_obat, col_penanganan = st.columns([1, 1])

                with col_obat:
                    st.markdown(
                        '<h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px; font-weight:700;">Rekomendasi Obat</h4>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11.5px; line-height:1.35;">{selected["obat"]}</p>',
                        unsafe_allow_html=True,
                    )

                with col_penanganan:
                    st.markdown(
                        '<h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px; font-weight:700;">Penanganan Tepat</h4>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11.5px; line-height:1.35;">{selected["penanganan"]}</p>',
                        unsafe_allow_html=True,
                    )

            # Space bawah agar tidak menabrak tombol navigasi
            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
            return

    # ---- Grid 2 Kolom Utama (Katalog) ----
    st.markdown(
        "<p style='text-align:center; color:#8a7a6d; margin-bottom:16px;'>Pilih penyakit untuk melihat rekomendasi</p>",
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for idx, disease in enumerate(DISEASES):
        col = cols[idx % 2]
        with col:
            if os.path.exists(disease["image_url"]):
                st.image(disease["image_url"], use_container_width=True)
            else:
                st.markdown(
                    '<div style="text-align:center; color:#8a7a6d; padding:20px 0;">[ Gambar ]</div>',
                    unsafe_allow_html=True,
                )

            st.markdown(
                f"<p style='color:#4a3525; font-weight:600; text-align:center; margin:4px 0 8px 0; font-size:13px;'>{disease['name']}</p>",
                unsafe_allow_html=True,
            )

            if st.button(
                "Pilih",
                key=f"btn_{disease['id']}",
                use_container_width=True,
                type="secondary",
            ):
                st.session_state.selected_disease = disease["id"]
                st.rerun()

            st.markdown("<div style='margin-bottom:16px;'></div>", unsafe_allow_html=True)
