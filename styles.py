"""Injeksi CSS Global - SEKULIT Precision Mobile Styling"""

import config as c
import streamlit as st


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        /* 1. RESET GLOBAL & MENCEGAH SCROLL SAMPING */
        *, html, body, .stApp {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            box-sizing: border-box !important;
        }}

        html, body, .stApp, [data-testid="stAppViewContainer"] {{
            max-width: 100vw !important;
            overflow-x: hidden !important;
        }}

        /* Sembunyikan header/footer bawaan Streamlit */
        #MainMenu, footer, header, div[data-testid="stToolbar"], div[data-testid="stDecoration"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        [data-testid="stAppViewContainer"],
        [data-testid="stHeader"],
        [data-testid="stVerticalBlock"],
        [data-testid="stVerticalBlockBorderWrapper"],
        .element-container {{
            background-color: transparent !important;
        }}

        .stApp {{
            background-color: #d6cfc7 !important;
        }}

        /* 2. FIX PADDING CONTAINER UTAMA (Agar Header Atas Tidak Kepotong) */
        @media (min-width: 600px) {{
            .stApp {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh !important;
            }}

            div.block-container {{
                max-width: {c.FRAME_WIDTH}px !important;
                width: {c.FRAME_WIDTH}px !important;
                height: {c.FRAME_HEIGHT}px !important;
                max-height: {c.FRAME_HEIGHT}px !important;
                margin: auto !important;
                padding: 24px 16px 80px 16px !important; /* Top padding 24px agar header aman */
                background-color: {c.COLOR_BG} !important;
                border-radius: 32px !important;
                box-shadow: 0 20px 50px rgba(74, 53, 37, 0.25) !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
                position: relative !important;
            }}
        }}

        @media (max-width: 599px) {{
            .stApp {{
                background-color: {c.COLOR_BG} !important;
            }}

            div.block-container {{
                max-width: 100% !important;
                width: 100% !important;
                height: 100vh !important;
                margin: 0 !important;
                padding: 20px 12px 80px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}
        }}

        /* 3. FIX TOMBOL (Bikin Ringkas, Kecil, Pas di Layar) */
        div.stButton > button {{
            min-height: 34px !important;
            height: 34px !important;
            padding: 2px 8px !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            width: 100% !important;
            margin-top: 4px !important;
            margin-bottom: 4px !important;
        }}

        /* Fix Khusus Tombol Back Navigasi Atas */
        button[key*="back_"] {{
            min-height: 32px !important;
            height: 32px !important;
            width: 32px !important;
            background: #ffffff !important;
            border: 1px solid #ecdfd4 !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            color: #4a3525 !important;
            padding: 0 !important;
            box-shadow: none !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }}

        /* 4. FIX TEKS & JUDUL (Bebas Kepotong) */
        .sekulit-header-title {{
            font-size: 16px !important;
            font-weight: 700 !important;
            color: #4a3525 !important;
            margin: 0 !important;
            text-align: center !important;
            line-height: 32px !important;
            white-space: nowrap !important;
        }}

        p, span, h1, h2, h3, h4, label {{
            line-height: 1.3 !important;
        }}

        /* 5. FIX GAMBAR & GRID KOLOM */
        [data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            gap: 8px !important;
        }}

        [data-testid="column"] {{
            min-width: 0 !important;
            flex: 1 1 0px !important;
            padding: 0 !important;
        }}

        /* Proporsi Gambar Kartu Penyakit */
        [data-testid="stImage"] img {{
            border-radius: 12px !important;
            object-fit: cover !important;
            height: 110px !important;
            width: 100% !important;
        }}

        /* Card Styling */
        .sekulit-card {{
            background-color: #ffffff !important;
            border: 1px solid rgba(250, 213, 197, 0.6);
            border-radius: {c.RADIUS_CARD}px;
            padding: {c.CARD_PADDING}px;
            margin-bottom: 12px;
            width: 100% !important;
            box-sizing: border-box !important;
        }}

        /* Hide Scrollbar */
        div.block-container::-webkit-scrollbar {{
            width: 0px;
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
