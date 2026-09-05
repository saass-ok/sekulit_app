"""Komponen UI yang dipakai berulang: header & bottom navigation."""

import config as c
import streamlit as st
from state import go_back, go_to_tab_root

ICON_ONLY = True


def render_header(page_key: str):
    """Header back navigation: posisi tengah presisi & teks bold."""
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
    """5 tombol navigasi utama di bagian bawah."""
    cols = st.columns(len(c.NAV_ITEMS))

    for col, (tab_key, label, icon) in zip(cols, c.NAV_ITEMS):
        with col:
            is_active = tab_key == active_tab

            # Format otomatis string nama ikon menjadi sintaks Material Icon Streamlit
            formatted_icon = icon
            if (
                icon
                and not icon.startswith(":")
                and not any(ord(char) > 127 for char in icon)
            ):
                formatted_icon = f":material/{icon}:"

            display_label = label if not ICON_ONLY else ""

            btn_kwargs = {
                "key": f"nav_{tab_key}",
                "use_container_width": True,
                "type": "primary" if is_active else "secondary",
            }

            if formatted_icon.startswith(":material/"):
                btn_kwargs["icon"] = formatted_icon
            elif ICON_ONLY:
                display_label = formatted_icon
            else:
                display_label = f"{formatted_icon}\n{label}"

            if st.button(display_label, **btn_kwargs):
                if not is_active:
                    go_to_tab_root(c.TAB_ROOT_PAGE[tab_key])


def card_start(accent: bool = False):
    cls = "sekulit-card sekulit-card-accent" if accent else "sekulit-card"
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)


def card_end():
    st.markdown("</div>", unsafe_allow_html=True)
