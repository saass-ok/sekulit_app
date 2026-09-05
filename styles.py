"""Injeksi CSS Global - SEKULIT Mobile Layout & Sticky Nav"""

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

        /* 2. PAKSA KOLOM TETAP SEJAJAR KESAMPING DI HP */
        div[data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            gap: 8px !important;
            align-items: center !important;
        }}

        div[data-testid="stHorizontalBlock"] > div[data-testid="column"],
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
            width: 0 !important;
            min-width: 0 !important;
            flex: 1 1 0% !important;
            padding: 0 !important;
        }}

        /* 3. LAYOUT CONTAINER UTAMA (Margin bottom disiapkan untuk Sticky Nav) */
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
                padding: 16px 14px 75px 14px !important; /* Padding bawah agar konten tidak tertutup nav */
                background-color: {c.COLOR_BG} !important;
                border-radius: 32px !important;
                box-shadow: 0 20px 50px rgba(74, 53, 37, 0.25) !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
                position: relative !important;
            }}

            /* Sticky Nav di Mode Desktop Simulator */
            div[data-testid="stHorizontalBlock"]:has(button[key*="nav_"]) {{
                position: absolute !important;
                bottom: 0 !important;
                left: 0 !important;
                right: 0 !important;
                width: 100% !important;
                background-color: #ffffff !important;
                padding: 10px 12px 14px 12px !important;
                border-top: 1px solid #ecdfd4 !important;
                border-bottom-left-radius: 32px !important;
                border-bottom-right-radius: 32px !important;
                z-index: 99999 !important;
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
                padding: 16px 12px 75px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}

            /* Sticky Nav Layaknya Aplikasi Mobile (Instagram Style) */
            div[data-testid="stHorizontalBlock"]:has(button[key*="nav_"]) {{
                position: fixed !important;
                bottom: 0 !important;
                left: 0 !important;
                right: 0 !important;
                width: 100% !important;
                background-color: #ffffff !important;
                padding: 10px 12px 14px 12px !important;
                border-top: 1px solid #ecdfd4 !important;
                z-index: 99999 !important;
            }}
        }}

        /* 4. FIX HEADER (Bold, Center, Presisi) */
        .sekulit-header-title {{
            font-size: 15px !important;
            font-weight: 700 !important;
            color: #4a3525 !important;
            text-align: center !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            line-height: 32px !important;
            margin: 0 !important;
            padding: 0 !important;
        }}

        /* 5. FIX UPLOAD BUTTON GLITCH */
        [data-testid="stFileUploader"] {{
            background-color: #ffffff !important;
            border-radius: 16px !important;
            padding: 8px !important;
            border: 1px dashed #d0c0b0 !important;
        }}

        [data-testid="stFileUploaderDropzone"] {{
            background-color: transparent !important;
            padding: 12px !important;
        }}

        [data-testid="stFileUploader"] button {{
            width: auto !important;
            min-height: 36px !important;
            height: 36px !important;
            padding: 4px 16px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            background-color: #4a3525 !important;
            color: #ffffff !important;
            border: none !important;
            margin: 0 auto !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}

        [data-testid="stFileUploader"] button * {{
            color: #ffffff !important;
        }}

        /* 6. STYLE TOMBOL BOTTOM NAV & IKON */
        button[key*="nav_"] {{
            min-height: 42px !important;
            height: 42px !important;
            max-height: 42px !important;
            padding: 0 !important;
            border-radius: 12px !important;
            margin: 0 !important;
            width: 100% !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }}

        button[key*="nav_"] [data-testid="stIconMaterial"] {{
            font-size: 22px !important;
            margin: 0 !important;
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
