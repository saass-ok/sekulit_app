import streamlit as st

ARTICLES = [
    {
        "id": 1,
        "title": "5 Cara Menjaga Skin Barrier di Cuaca Ekstrem",
        "summary": "Perubahan cuaca ekstrem dapat merusak lapisan pelindung kulit. Berikut 5 cara efektif menjaganya.",
        "image": "🌤️",
        "category": "Perawatan",
    },
    {
        "id": 2,
        "title": "Mengenal Perbedaan Tahi Lalat Normal dan Tidak Normal",
        "summary": "Tahi lalat dapat muncul sejak lahir, namun perlu dikenali tanda-tanda bahayanya.",
        "image": "🔍",
        "category": "Edukasi",
    },
    {
        "id": 3,
        "title": "8 Mitos dan Fakta Tentang Kulit yang Perlu Anda Tahu",
        "summary": "Ada berbagai mitos dan fakta seputar perawatan kulit yang beredar di masyarakat.",
        "image": "📖",
        "category": "Mitos & Fakta",
    },
    {
        "id": 4,
        "title": "Cara Mengatasi Jerawat Batu yang Membandel",
        "summary": "Jerawat batu (cystic acne) membutuhkan penanganan khusus agar tidak meninggalkan bekas.",
        "image": "💊",
        "category": "Pengobatan",
    },
]


def render():
    # ============================================
    # ARTIKEL UNGGULAN (Hot Topic) – kartu dengan aksen
    # ============================================
    featured = ARTICLES[0]
    st.markdown(
        f"""
        <div style="
            background: #fef6f2;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 16px;
            border: 1px solid #fad5c5;
        ">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="font-size: 48px;">{featured['image']}</div>
                <div style="flex: 1;">
                    <p style="color: #c85a32; font-size: 13px; font-weight: 600; margin: 0 0 4px 0;">{featured['category']}</p>
                    <p style="color: #4a3525; font-weight: 700; font-size: 16px; margin: 0 0 4px 0;">{featured['title']}</p>
                    <p style="color: #4a3525; font-size: 13px; opacity: 0.8; margin: 0;">{featured['summary']}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ============================================
    # ARTIKEL LAINNYA – kartu putih standar
    # ============================================
    for article in ARTICLES[1:]:
        st.markdown(
            f"""
            <div style="
                background: #ffffff;
                border-radius: 16px;
                padding: 16px;
                margin-bottom: 12px;
                border: 1px solid rgba(250, 213, 197, 0.6);
            ">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="font-size: 28px;">{article['image']}</div>
                    <div style="flex: 1;">
                        <p style="color: #c85a32; font-size: 11px; font-weight: 600; margin: 0 0 2px 0;">{article['category']}</p>
                        <p style="color: #4a3525; font-weight: 700; font-size: 14px; margin: 0 0 2px 0;">{article['title']}</p>
                        <p style="color: #4a3525; font-size: 12px; opacity: 0.7; margin: 0;">{article['summary']}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )