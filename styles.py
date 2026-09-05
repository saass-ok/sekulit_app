"""Injeksi CSS Global - SEKULIT Precision Mobile Styling"""

import config as c
import streamlit as st


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        /* 1. RESET GLOBAL & SCROLL LOCK */
        *, html, body, .stApp {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            box-sizing: border-box !important;
        }}

        html, body, .stApp, [data-testid="stAppViewContainer"] {{
            max-width: 100vw !important;
            overflow-x: hidden !important;
        }}

        /* Sembunyikan chrome bawaan Streamlit */
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

        /* 2. LAYOUT CONTAINER HP */
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
                padding: 20px 14px 85px 14px !important;
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
                padding: 16px 12px 85px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}
        }}

        /* 3. PERBAIKAN BOTTOM NAVIGATION (UKURAN KECIL & PRESISI) */
        [data-testid="stHorizontalBlock"]:has(button[key*="nav_"]) {{
            position: absolute !important;
            bottom: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100% !important;
            background-color: #ffffff !important;
            padding: 8px 10px 16px 10px !important;
            border-top: 1px solid #ecdfd4 !important;
            z-index: 99999 !important;
            display: flex !important;
            flex-direction: row !important;
            gap: 6px !important;
            margin: 0 !important;
        }}

        /* Tombol Ikon Bottom Nav */
        button[key*="nav_"] {{
            min-height: 40px !important;
            height: 40px !important;
            max-height: 40px !important;
            padding: 0 !important;
            border-radius: 12px !important;
            margin: 0 !important;
            width: 100% !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }}

        /* Ukuran Ikon dalam Navigasi */
        button[key*="nav_"] span {{
            font-size: 20px !important;
        }}

        /* 4. PERBAIKAN ARTIKEL & GAMBAR */
        [data-testid="stImage"] img {{
            border-radius: 12px !important;
            object-fit: cover !important;
            height: 100px !important;
            width: 100% !important;
        }}

        .sekulit-article-title {{
            font-size: 12px !important;
            font-weight: 600 !important;
            color: #4a3525 !important;
            text-align: center !important;
            margin-top: 6px !important;
            line-height: 1.2 !important;
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
