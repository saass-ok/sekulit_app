"""Injeksi CSS Global - SEKULIT Responsive Header Title & Popup Fix"""

import config as c
import streamlit as st


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0');

        /* 1. RESET GLOBAL & SCROLL LOCK */
        *, html, body, .stApp {{
            box-sizing: border-box !important;
        }}

        html, body, .stApp {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            max-width: 100vw !important;
            overflow-x: hidden !important;
        }}

        /* Font Ikon Material Streamlit */
        [data-testid="stIconMaterial"],
        span[data-testid="stIconMaterial"],
        .material-symbols-outlined {{
            font-family: 'Material Symbols Outlined' !important;
            font-weight: normal !important;
            font-style: normal !important;
            line-height: 1 !important;
            text-transform: none !important;
            letter-spacing: normal !important;
            word-wrap: normal !important;
            white-space: nowrap !important;
            direction: ltr !important;
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

        /* 2. PAKSA KOLOM TETAP SEJAJAR KESAMPING DI HP */
        div[data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            width: 100% !important;
            gap: 6px !important;
            align-items: flex-start !important;
        }}

        div[data-testid="stHorizontalBlock"] > div[data-testid="column"],
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
            width: 0 !important;
            min-width: 0 !important;
            flex: 1 1 0% !important;
            padding: 0 !important;
        }}

        /* 3. LAYOUT CONTAINER UTAMA */
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
                padding: 16px 14px 75px 14px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 32px !important;
                box-shadow: 0 20px 50px rgba(74, 53, 37, 0.25) !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
                position: relative !important;
            }}

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
                padding: 16px 12px 85px 12px !important;
                background-color: {c.COLOR_BG} !important;
                border-radius: 0px !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }}

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

        /* 4. FIX HEADER TITLE */
        .sekulit-header-title {{
            font-size: clamp(12px, 3.8vw, 14.5px) !important;
            font-weight: 700 !important;
            color: #4a3525 !important;
            text-align: center !important;
            white-space: nowrap !important;
            line-height: 32px !important;
            margin: 0 !important;
            padding: 0 !important;
            letter-spacing: -0.3px !important;
        }}

        /* 5. STYLE TOMBOL NAVIGASI BAWAH */
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
            font-size: 24px !important;
            margin: 0 !important;
        }}

        /* 6. FILE UPLOADER FIX */
        [data-testid="stFileUploader"] {
            background-color: #ffffff !important;
            border-radius: 16px !important;
            padding: 8px !important;
            border: 1px dashed #d0c0b0 !important;
        }

        [data-testid="stFileUploaderDropzone"] {
            background-color: #ffffff !important;
            padding: 12px !important;
            border: none !important;
        }

        /* Warna teks petunjuk upload (Drag and drop, limit ukuran, dll) */
        [data-testid="stFileUploaderDropzone"] span,
        [data-testid="stFileUploaderDropzone"] div,
        [data-testid="stFileUploaderDropzone"] small,
        [data-testid="stFileUploaderInstructions"],
        [data-testid="stFileUploaderFileData"] {
            color: #4a3525 !important;
            font-weight: 500 !important;
        }

        /* Tombol Browse Files */
        [data-testid="stFileUploader"] button {
            width: auto !important;
            min-height: 38px !important;
            height: 38px !important;
            padding: 6px 18px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            background-color: #4a3525 !important;
            color: #ffffff !important;
            border: none !important;
            margin: 0 auto !important;
        }

        [data-testid="stFileUploader"] button * {
            color: #ffffff !important;
        }

        /* 7. PAKSA KOTAK JADI RELATIVE & TOMBOL X DIPOSISIKAN ABSOLUT KE POJOK KANAN ATAS */
        [data-testid="stVerticalBlockBorderWrapper"] {{
            position: relative !important;
            padding: 16px 14px !important;
            border-radius: 24px !important;
            background-color: #ffffff !important;
        }}

        [data-testid="stElementContainer"]:has(button[key*="close_detail"]) {{
            position: absolute !important;
            top: 12px !important;
            right: 12px !important;
            width: 28px !important;
            height: 28px !important;
            z-index: 9999 !important;
        }}

        button[key*="close_detail"] {{
            position: absolute !important;
            top: 0 !important;
            right: 0 !important;
            min-height: 28px !important;
            height: 28px !important;
            max-height: 28px !important;
            width: 28px !important;
            max-width: 28px !important;
            padding: 0 !important;
            background-color: #4a3525 !important;
            color: #ffffff !important;
            border-radius: 50% !important;
            font-size: 13px !important;
            font-weight: bold !important;
            border: none !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
        }}

        button[key*="close_detail"] * {{
            color: #ffffff !important;
        }}

        /* 8. KUNCI LIGHT MODE UNTUK SEMUA ELEMENT INPUT & DROPDOWN */
        div[data-baseweb="input"],
        div[data-baseweb="select"] > div,
        div[data-baseweb="popover"],
        ul[role="listbox"],
        li[data-baseweb="option"],
        input,
        select {{
            background-color: #ffffff !important;
            color: #4a3525 !important;
            border-radius: 12px !important;
        }}

        /* Placeholder input */
        input::placeholder,
        textarea::placeholder {{
            color: #a08a75 !important;
            opacity: 1 !important;
        }}

        /* Kunci warna teks label & pilihan radio button */
        div[role="radiogroup"] label p,
        div[data-testid="stMarkdownContainer"] p,
        label[data-testid="stWidgetLabel"] p,
        span[data-baseweb="select"] {{
            color: #4a3525 !important;
        }}

        /* Teks menu pilihan dropdown */
        li[data-baseweb="option"] * {{
            color: #4a3525 !important;
        }}

        /* Style khusus untuk Camera Input Streamlit */
        div[data-testid="stCameraInput"] {{
            background-color: #ffffff !important;
            border-radius: 16px !important;
            padding: 10px !important;
            border: 1px dashed #d0c0b0 !important;
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
