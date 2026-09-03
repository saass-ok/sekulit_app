"""
Pengelolaan navigasi & state aplikasi.
Karena Streamlit tidak native mendukung pola "back navigation" ala mobile app,
kita simulasikan pakai stack (list) sederhana di session_state.
"""

import streamlit as st


def init_state():
    defaults = {
        "page": "beranda",
        "history": [],          # stack untuk tombol back di header
        "selected_doctor": None,  # dipakai halaman konsultasi -> chat
        "estimation_result": None,  # dipakai halaman cek kulit -> hasil
        "selected_article": None,   # dipakai halaman informasi -> detail
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def go_to(page_name: str, push_history: bool = True):
    """Pindah ke halaman baru. push_history=True akan menyimpan
    halaman saat ini ke stack supaya tombol back di header bisa kembali."""
    if push_history and st.session_state.page != page_name:
        st.session_state.history.append(st.session_state.page)
    st.session_state.page = page_name
    st.rerun()


def go_to_tab_root(page_name: str):
    """Khusus untuk klik tombol bottom nav: pindah tab dan reset history,
    karena pindah tab dianggap 'mulai baru', bukan drill-down."""
    st.session_state.history = []
    st.session_state.page = page_name
    st.rerun()


def go_back():
    """Tombol back di header: kembali ke halaman sebelumnya di stack."""
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
    else:
        st.session_state.page = "beranda"
    st.rerun()
