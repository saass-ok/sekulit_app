import os
import streamlit as st

# ===================== DATA 7 PENYAKIT =====================
DISEASES = [
    {
        "id": "melanocytic_nevi",
        "name": "Melanocytic Nevi",
        "icon": "🟤",
        "image_url": "assets/Melanocytic Nevi.jpg",
        "description": "Melanocytic Nevi adalah pertumbuhan jinak pada kulit yang terbentuk dari penumpukan sel pigmen (melanosit), atau yang secara umum dikenal masyarakat sebagai tahi lalat biasa.",
        "obat": "Kondisi ini tidak dapat disembuhkan atau dihilangkan menggunakan obat minum maupun salep topikal. Sangat dilarang menggunakan cairan atau krim penghilang tahi lalat yang dijual bebas di pasaran, karena berisiko tinggi memicu luka bakar kimia, infeksi, hingga kerusakan jaringan kulit permanen.",
        "penanganan": "Jika tahi lalat terasa mengganggu secara estetika atau sering mengalami iritasi akibat gesekan, penanganan terbaik adalah melakukan tindakan medis aman (seperti laser atau bedah minor) oleh dokter spesialis kulit. Untuk perawatan mandiri, cukup gunakan tabir surya (sunscreen) secara rutin guna melindungi tahi lalat dari paparan radiasi UV.",
    },
    {
        "id": "basal_cell_carcinoma",
        "name": "Basal Cell Carcinoma",
        "icon": "🩹",
        "image_url": "assets/Basal Cell Carcinoma.jpg",
        "description": "Basal Cell Carcinoma (BCC) adalah jenis kanker kulit paling umum yang tumbuh lambat dan jarang menyebar ke bagian tubuh lain. Biasanya muncul sebagai benjolan berkilau atau luka yang tidak sembuh-sembuh.",
        "obat": "Pengobatan BCC umumnya melalui tindakan bedah eksisi, krioterapi, atau terapi topikal seperti imiquimod atau fluorouracil untuk kasus superfisial. Konsultasi dengan dokter spesialis kulit sangat dianjurkan.",
        "penanganan": "Deteksi dini sangat penting. Jika menemukan luka yang tidak sembuh dalam 4 minggu, segera periksakan ke dokter. Gunakan sunscreen setiap hari untuk mencegah kekambuhan.",
    },
    {
        "id": "melanoma",
        "name": "Melanoma",
        "icon": "⚫",
        "image_url": "assets/Melanoma.jpg",
        "description": "Melanoma adalah jenis kanker kulit paling serius yang berasal dari sel pigmen (melanosit). Dapat muncul dari tahi lalat yang berubah bentuk, warna, atau ukuran, atau muncul sebagai bintik baru.",
        "obat": "Pengobatan melanoma memerlukan tindakan bedah eksisi luas, imunoterapi, terapi target, atau kemoterapi tergantung stadium. Penanganan harus segera dilakukan oleh ahli onkologi kulit.",
        "penanganan": "Perhatikan tanda ABCDE: Asimetri, Batas tidak rata, Warna tidak merata, Diameter >6mm, Evolusi (berubah). Segera periksa ke dokter jika ada perubahan.",
    },
    {
        "id": "actinic_keratoses",
        "name": "Actinic Keratoses",
        "icon": "🔴",
        "image_url": "assets/Actinic Keratoses.jpg",
        "description": "Actinic Keratoses (AK) adalah bercak bersisik pada kulit akibat paparan sinar matahari jangka panjang. Merupakan lesi pra-kanker yang dapat berkembang menjadi squamous cell carcinoma jika tidak ditangani.",
        "obat": "Pengobatan AK meliputi krioterapi, terapi topikal (5-fluorouracil, imiquimod, atau diclofenac), dan fotodinamik terapi. Konsultasi dokter untuk penanganan terbaik.",
        "penanganan": "Lindungi kulit dari sinar matahari dengan sunscreen SPF 30+, gunakan pakaian pelindung, dan hindari paparan sinar UV berlebihan. Lakukan pemeriksaan kulit rutin.",
    },
    {
        "id": "benign_keratosis",
        "name": "Benign Keratosis",
        "icon": "🟡",
        "image_url": "assets/Benign Keratosis-like Lesions.jpg",
        "description": "Benign Keratosis (BKL) adalah pertumbuhan kulit jinak yang umum terjadi seiring bertambahnya usia. Biasanya muncul sebagai bercak cokelat atau hitam dengan permukaan kasar seperti kutil.",
        "obat": "BKL tidak memerlukan pengobatan khusus karena bersifat jinak. Namun jika mengganggu secara estetika atau sering iritasi, dapat dilakukan krioterapi atau eksisi minor oleh dokter.",
        "penanganan": "Cukup lakukan observasi rutin. Gunakan pelembab untuk menjaga kulit tetap lembab dan hindari menggaruk atau mengiritasi lesi.",
    },
    {
        "id": "vascular_lesions",
        "name": "Vascular Lesions",
        "icon": "🔵",
        "image_url": "assets/Vascular Lesions.jpg",
        "description": "Vascular Lesions (VASC) adalah gangguan pembuluh darah di kulit yang tampak sebagai bercak merah, ungu, atau kemerahan. Contohnya adalah hemangioma, port-wine stain, atau spider angioma. Umumnya bersifat jinak.",
        "obat": "Pengobatan vascular lesions tergantung jenisnya. Laser pulsed dye laser (PDL) adalah terapi utama untuk lesi vaskular. Krim topikal seperti timolol dapat digunakan untuk hemangioma infantile.",
        "penanganan": "Konsultasi dengan dokter kulit untuk diagnosis dan terapi yang tepat. Lindungi kulit dari trauma untuk mencegah perdarahan.",
    },
    {
        "id": "dermatofibroma",
        "name": "Dermatofibroma",
        "icon": "🟠",
        "image_url": "assets/Dermatofibroma.jpg",
        "description": "Dermatofibroma (DF) adalah benjolan jinak di bawah kulit yang keras dan berwarna cokelat. Sering muncul di tungkai bawah dan biasanya tidak menimbulkan gejala, meskipun kadang terasa gatal atau nyeri.",
        "obat": "DF tidak memerlukan pengobatan karena bersifat jinak. Jika menimbulkan gejala atau mengganggu, dapat dilakukan eksisi bedah minor oleh dokter kulit.",
        "penanganan": "Hindari menggaruk atau menekan benjolan. Jika ukuran atau warna berubah, segera periksakan ke dokter untuk memastikan tidak ada keganasan.",
    },
]


def render():
    """Halaman rekomendasi obat – grid gambar tanpa bubble, detail lebih rapi."""

    # ---- Jika ada penyakit yang dipilih, tampilkan detail ----
    selected_id = st.session_state.get("selected_disease")
    if selected_id:
        selected = next((d for d in DISEASES if d["id"] == selected_id), None)
        if selected:
            # Container Kartu
            st.markdown(
                """
                <div style="
                    background: #ffffff;
                    border-radius: 16px;
                    padding: 16px;
                    border: 1px solid rgba(250,213,197,0.6);
                    margin-bottom: 12px;
                ">
                """,
                unsafe_allow_html=True,
            )

            # === HEADER KARTU: Judul & Tombol Close (✕) di Pojok Kanan ===
            col_title, col_close = st.columns([7, 1])
            with col_title:
                st.markdown(
                    f'<h3 style="color:#4a3525; margin:0; font-size:18px;">{selected["name"]}</h3>',
                    unsafe_allow_html=True,
                )
            with col_close:
                if st.button("✕", key="close_detail", help="Tutup detail"):
                    st.session_state.selected_disease = None
                    st.rerun()

            st.markdown(
                "<hr style='margin: 8px 0 12px 0; border: none; border-top: 1px solid #ecdfd4;'>",
                unsafe_allow_html=True,
            )

            # === BARIS ATAS: Gambar (Kiri) & Deskripsi (Kanan) ===
            col_img, col_desc = st.columns([1, 1])

            with col_img:
                if os.path.exists(selected["image_url"]):
                    st.image(selected["image_url"], use_container_width=True)
                else:
                    st.markdown(
                        f'<div style="font-size:60px; text-align:center;">{selected["icon"]}</div>',
                        unsafe_allow_html=True,
                    )

            with col_desc:
                st.markdown(
                    """
                    <h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px;">📋 Deskripsi</h4>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11px; line-height:1.3;">{selected["description"]}</p>',
                    unsafe_allow_html=True,
                )

            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

            # === BARIS BAWAH: Rekomendasi Obat (Kiri) & Penanganan Tepat (Kanan) ===
            col_obat, col_penanganan = st.columns([1, 1])

            with col_obat:
                st.markdown(
                    """
                    <h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px;">💊 Rekomendasi Obat</h4>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11px; line-height:1.3;">{selected["obat"]}</p>',
                    unsafe_allow_html=True,
                )

            with col_penanganan:
                st.markdown(
                    """
                    <h4 style="color:#4a3525; margin:0 0 4px 0; font-size:13px;">🏥 Penanganan Tepat</h4>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p style="color:#4a3525; opacity:0.9; margin:0; font-size:11px; line-height:1.3;">{selected["penanganan"]}</p>',
                    unsafe_allow_html=True,
                )

            st.markdown("</div>", unsafe_allow_html=True)
            return

    # ---- Grid 2 kolom tanpa bubble ----
    st.markdown(
        "<p style='text-align:center; color:#8a7a6d; margin-bottom:16px;'>Pilih penyakit untuk melihat rekomendasi</p>",
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for idx, disease in enumerate(DISEASES):
        col = cols[idx % 2]
        with col:
            # Gambar
            if os.path.exists(disease["image_url"]):
                st.image(disease["image_url"], use_container_width=True)
            else:
                st.markdown(
                    f'<div style="font-size:60px; text-align:center;">{disease["icon"]}</div>',
                    unsafe_allow_html=True,
                )

            # Nama penyakit
            st.markdown(
                f"<p style='color:#4a3525; font-weight:600; text-align:center; margin:4px 0 8px 0;'>{disease['name']}</p>",
                unsafe_allow_html=True,
            )

            # Tombol Pilih
            if st.button(
                "Pilih",
                key=f"btn_{disease['id']}",
                use_container_width=True,
                type="secondary",
            ):
                st.session_state.selected_disease = disease["id"]
                st.rerun()

            st.markdown(
                "<div style='margin-bottom:16px;'></div>",
                unsafe_allow_html=True,
            )
