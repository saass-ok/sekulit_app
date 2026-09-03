import config as c
from components import render_bottom_nav, render_header
from pages_content import (
    beranda,
    cek_kulit,
    informasi,
    konsultasi,
    rekomendasi_obat,
)
from state import init_state
import streamlit as st
from styles import inject_css

st.set_page_config(
    page_title="SEKULIT",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed",
)

init_state()

# Inisialisasi state hasil estimasi agar tidak error saat halaman dimuat
if "estimation_result" not in st.session_state:
    st.session_state.estimation_result = None

inject_css()

page = st.session_state.page

# ---------- Header (back navigation, tidak muncul di Beranda) ----------
render_header(page)

# ---------- Routing konten halaman ----------
if page == "beranda":
    beranda.render()
elif page == "cek_kulit_input":
    cek_kulit.render_input()
elif page == "cek_kulit_output":
    cek_kulit.render_output()
# Di dalam app.py (bagian routing)
elif page == "konsultasi_list":
    konsultasi.render_list()
elif page == "konsultasi_chat":
    konsultasi.render_chat()
elif page == "rekomendasi_obat":
    rekomendasi_obat.render()
elif page == "informasi":
    informasi.render()
else:
    st.write("Halaman tidak ditemukan.")

# ---------- Bottom navigation (5 tombol utama) ----------
active_tab = c.PAGE_TO_TAB.get(page, "beranda")
render_bottom_nav(active_tab)