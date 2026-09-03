"""Injeksi CSS Global - SEKULIT Mobile Frame (390x844 px)"""

import config as c
import streamlit as st


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        /* 1. Mencegah font kustom merusak font Ikon Material bawaan Streamlit */
        *:not(span[data-testid="stIconMaterial"]):not(i):not(.material-symbols-outlined) {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            box-sizing: border-box !important;
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

        /* Outer Canvas */
        .stApp {{
            background-color: #d6cfc7 !important;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh !important;
        }}

        /* Frame HP Utama (390 x 844 px) – flex column agar bottom nav di bawah */
        div.block-container {{
            max-width: {c.FRAME_WIDTH}px !important;
            width: {c.FRAME_WIDTH}px !important;
            height: {c.FRAME_HEIGHT}px !important;
            max-height: {c.FRAME_HEIGHT}px !important;
            margin: 20px auto !important;
            padding: 16px 16px 0px 16px !important;
            background-color: {c.COLOR_BG} !important;
            border-radius: 32px !important;
            box-shadow: 0 20px 50px rgba(74, 53, 37, 0.25) !important;
            overflow-y: auto !important;
            position: relative !important;
            display: flex !important;
            flex-direction: column !important;
            padding-bottom: 80px !important;  /* ruang untuk bottom nav */
        }}

        div.block-container::-webkit-scrollbar {{
            width: 0px;
        }}

        /* HEADER JUDUL CENTER & BOLD */
        .sekulit-header-title {{
            font-size: 16px !important;
            font-weight: 700 !important;
            color: #4a3525 !important;
            margin: 0 !important;
            text-align: center !important;
            line-height: 36px !important;
            white-space: nowrap !important;
        }}

        button[key*="back_"] {{
            background: transparent !important;
            border: none !important;
            font-size: 22px !important;
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
            padding: 16px 8px !important;
            text-align: center !important;
        }}

        /* RADIO BUTTON CENTER */
        div[data-testid="stRadio"] > div[role="radiogroup"] {{
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 20px !important;
            width: 100% !important;
        }}

        .sekulit-card {{
            background-color: #ffffff !important;
            border: 1px solid rgba(250, 213, 197, 0.6);
            border-radius: {c.RADIUS_CARD}px;
            padding: {c.CARD_PADDING}px;
            margin-bottom: 12px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )