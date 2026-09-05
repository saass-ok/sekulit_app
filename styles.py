"""Injeksi CSS Global - SEKULIT Mobile Frame Responsif (No Horizontal Scroll)"""

import config as c
import streamlit as st


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        /* 1. RESET GLOBAL & MENCEGAH HORIZONTAL SCROLL */
        *, html, body, .stApp, [data-testid="stAppViewContainer"] {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            box-sizing: border-box !important;
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

        /* 2. PAKSA KOLOM SEJAJAR HORIZONTAL & MENYUSUT SAMA RATA */
        [data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            gap: 4px !important;
        }}

        [data-testid="column"] {{
            min-width: 0 !important;
            flex: 1 1 0px !important;
            padding: 0 !important;
        }}

        /* Optimasi tombol di dalam kolom agar tidak meletup melebar */
        [data-testid="column"] button {{
            padding: 4px 2px !important;
            font-size: 11px !important;
            width: 100% !important;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;
            overflow: hidden !important;
        }}

        /* 3. TAMPILAN MODE DESKTOP / LAPTOP (> 600px) - Frame HP Melayang */
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
                padding: 12px 12px 80px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 32px !important;
                box-shadow: 0 20px 50px rgba(74, 53, 37, 0.25) !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
                position: relative !important;
            }}
        }}

        /* 4. TAMPILAN MODE HP ASLI (< 600px) - Full Screen Native */
        @media (max-width: 599px) {{
            .stApp {{
                background-color: {c.COLOR_BG} !important;
            }}

            div.block-container {{
                max-width: 100% !important;
                width: 100% !important;
                height: 100vh !important;
                margin: 0 !important;
                padding: 12px 12px 80px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                box-shadow: none !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}
        }}

        /* Sembunyikan Scrollbar */
        div.block-container::-webkit-scrollbar {{
            width: 0px;
            display: none;
        }}

        /* HEADER JUDUL CENTER & BOLD */
        .sekulit-header-title {{
            font-size: 15px !important;
            font-weight: 700 !important;
            color: #4a3525 !important;
            margin: 0 !important;
            text-align: center !important;
            line-height: 36px !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }}

        button[key*="back_"] {{
            background: transparent !important;
            border: none !important;
            font-size: 20px !important;
            font-weight: bold !important;
            color: #4a3525 !important;
            padding: 0 !important;
            box-shadow: none !important;
        }}

        /* FIX UPLOAD GAMBAR */
        [data-testid="stFileUploader"] {{
            width: 100% !important;
        }}

        [data-testid="stFileUploaderDropzone"] {{
            background-color: #fbebe3 !important;
            border: 2px dashed #f3a88c !important;
            border-radius: 16px !important;
            padding: 12px 6px !important;
            text-align: center !important;
        }}

        /* RADIO BUTTON CENTER */
        div[data-testid="stRadio"] > div[role="radiogroup"] {{
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 12px !important;
            width: 100% !important;
            flex-wrap: wrap !important;
        }}

        .sekulit-card {{
            background-color: #ffffff !important;
            border: 1px solid rgba(250, 213, 197, 0.6);
            border-radius: {c.RADIUS_CARD}px;
            padding: {c.CARD_PADDING}px;
            margin-bottom: 12px;
            width: 100% !important;
            box-sizing: border-box !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
