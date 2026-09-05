"""Injeksi CSS Global - SEKULIT Fixed Mobile Layout"""

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

        /* 2. PAKSA SEMUA KOLOM Tetap Sejajar Kesamping DI HP (Dilarang Numpuk Vertikal) */
        div[data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            gap: 8px !important;
        }}

        div[data-testid="stHorizontalBlock"] > div[data-testid="column"],
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
            width: 0 !important;
            min-width: 0 !important;
            flex: 1 1 0% !important;
            padding: 0 !important;
        }}

        /* 3. LAYOUT CONTAINER HP */
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
                padding: 20px 14px 80px 14px !important;
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
                padding: 16px 12px 80px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}
        }}

        /* 4. PERBAIKAN BOTTOM NAVIGATION */
        div[data-testid="stHorizontalBlock"]:has(button[key*="nav_"]) {{
            position: fixed !important;
            bottom: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100% !important;
            max-width: {c.FRAME_WIDTH}px !important;
            margin: 0 auto !important;
            background-color: #ffffff !important;
            padding: 8px 6px 12px 6px !important;
            border-top: 1px solid #ecdfd4 !important;
            z-index: 99999 !important;
        }}

        button[key*="nav_"] {{
            min-height: 42px !important;
            height: 42px !important;
            padding: 0 !important;
            font-size: 18px !important;
            border-radius: 12px !important;
            width: 100% !important;
        }}

        /* 5. GAMBAR ARTIKEL SEJAJAR 2 KOLOM */
        [data-testid="stImage"] img {{
            border-radius: 12px !important;
            object-fit: cover !important;
            height: 100px !important;
            width: 100% !important;
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
