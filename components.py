"""Komponen UI yang dipakai berulang: header & bottom navigation."""

import config as c
import streamlit as st
from state import go_back, go_to_tab_root


def render_header(page_key: str):
    """Header back navigation."""
    if page_key == "beranda":
        return

    title = c.PAGE_TITLES.get(page_key, "")
    col_back, col_title, col_spacer = st.columns([1, 6, 1])

    with col_back:
        if st.button("‹", key=f"back_{page_key}"):
            go_back()

    with col_title:
        st.markdown(
            f'<p class="sekulit-header-title">{title}</p>',
            unsafe_allow_html=True,
        )

    with col_spacer:
        st.empty()


def render_bottom_nav(active_tab: str):
    """5 tombol navigasi utama di bagian bawah (Khusus Emoji)."""
    cols = st.columns(len(c.NAV_ITEMS))

    for col, (tab_key, label, icon) in zip(cols, c.NAV_ITEMS):
        with col:
            is_active = tab_key == active_tab
            btn_type = "primary" if is_active else "secondary"

            # Tampilkan emoji ikon saja
            if st.button(
                icon,
                key=f"nav_{tab_key}",
                use_container_width=True,
                type=btn_type,
            ):
                if not is_active:
                    go_to_tab_root(c.TAB_ROOT_PAGE[tab_key])


def card_start(accent: bool = False):
    cls = "sekulit-card sekulit-card-accent" if accent else "sekulit-card"
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)


def card_end():
    st.markdown("</div>", unsafe_allow_html=True)
