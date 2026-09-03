# pages_content/konsultasi.py

import streamlit as st
from state import go_to

# Data contoh dokter
DOCTORS = [
    {
        "id": 1,
        "name": "Dr. Reyhan Dewanto, Sp.DVE",
        "specialty": "Spesialis Lesi Kulit & Penyakit Kulit Umum",
        "online": True,
        "rating": 4.9,
        "photo": "👨‍⚕️",
    },
    {
        "id": 2,
        "name": "Dr. Citra Lestari, Sp.DVE",
        "specialty": "Spesialis Dermatologi Pediatrik & Jaringan Kulit",
        "online": True,
        "rating": 4.9,
        "photo": "👩‍⚕️",
    },
    {
        "id": 3,
        "name": "Dr. Andi Budi, Sp.DVE",
        "specialty": "Spesialis Tumor & Kanker Kulit",
        "online": True,
        "rating": 4.9,
        "photo": "👨‍⚕️",
    },
]


def get_auto_reply(user_message: str) -> str:
    msg = user_message.lower()
    if "1" in msg:
        return "Baik, untuk konsultasi umum, silakan ceritakan keluhan Anda secara detail."
    elif "2" in msg:
        return "Untuk konsultasi kulit, saya sarankan Anda mengirimkan foto area kulit yang bermasalah agar bisa saya analisis."
    elif "terima kasih" in msg or "makasih" in msg:
        return "Sama-sama! Jika ada pertanyaan lain, jangan ragu untuk bertanya."
    elif "halo" in msg or "hai" in msg:
        return "Halo! Selamat datang di konsultasi online. Silakan pilih menu:\n1. Konsultasi umum\n2. Konsultasi kulit\n\nKetik angka 1 atau 2 untuk memulai."
    else:
        return "Terima kasih atas pesannya. Saya akan membantu Anda. Silakan pilih:\n1. Konsultasi umum\n2. Konsultasi kulit\n\nKetik angka 1 atau 2."


def render_list():
    """Daftar dokter dengan kartu dan filter."""
    search_query = st.text_input(
        "", placeholder="Cari dokter...", key="search_doctor", label_visibility="collapsed"
    )

    filter_choice = st.session_state.get("filter_doctor", "online")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Online", key="filter_online", type="primary" if filter_choice == "online" else "secondary", use_container_width=True):
            st.session_state.filter_doctor = "online"
            st.rerun()
    with col2:
        if st.button("Terdekat", key="filter_terdekat", type="primary" if filter_choice == "terdekat" else "secondary", use_container_width=True):
            st.session_state.filter_doctor = "terdekat"
            st.rerun()
    with col3:
        if st.button("Rating", key="filter_rating", type="primary" if filter_choice == "rating" else "secondary", use_container_width=True):
            st.session_state.filter_doctor = "rating"
            st.rerun()

    filtered = DOCTORS
    if search_query:
        filtered = [d for d in filtered if search_query.lower() in d["name"].lower() or search_query.lower() in d["specialty"].lower()]

    for doctor in filtered:
        st.markdown(f"""
        <div style="background:#ffffff; border-radius:16px; padding:16px; margin-bottom:12px; border:1px solid rgba(250,213,197,0.6);">
            <p style="color:#4a3525; font-weight:700; font-size:15px; margin:0 0 2px 0;">{doctor['name']}</p>
            <p style="color:#4a3525; font-size:13px; margin:0 0 10px 0; opacity:0.8;">{doctor['specialty']}</p>
        """, unsafe_allow_html=True)

        col_status, col_rating, col_chat = st.columns([1, 1, 1.2])
        with col_status:
            status_text = "🟢 Online" if doctor['online'] else "⚪ Offline"
            st.markdown(f'<p style="color:#4a3525; margin:0;">{status_text}</p>', unsafe_allow_html=True)
        with col_rating:
            st.markdown(f'<p style="color:#4a3525; margin:0;">⭐ {doctor["rating"]}</p>', unsafe_allow_html=True)
        with col_chat:
            if st.button("Chat", key=f"chat_{doctor['id']}", use_container_width=True):
                st.session_state.selected_doctor = doctor
                history_key = f"chat_history_{doctor['id']}"
                if history_key not in st.session_state:
                    st.session_state[history_key] = [{"role": "doctor", "text": "Halo, ada yang bisa saya bantu?"}]
                go_to("konsultasi_chat", push_history=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_chat():
    """Halaman chat dengan bubble, auto-reply, dan teks gelap."""
    # CSS paksa warna gelap
    st.markdown("""
    <style>
    .chat-container, .chat-container * {
        color: #4a3525 !important;
    }
    .chat-container textarea, .chat-container button,
    .chat-container .stTextArea textarea,
    .chat-container .stFormSubmitButton button {
        color: #4a3525 !important;
    }
    .chat-container button {
        background-color: #fad5c5 !important;
        border: 1px solid #fad5c5 !important;
    }
    .sekulit-header-title {
        color: #000000 !important;
    }
    .chat-bubble-doctor, .chat-bubble-doctor * {
        color: #4a3525 !important;
    }
    #chat-header p {
        color: #000000 !important;
    }
    </style>
    <div class="chat-container">
    """, unsafe_allow_html=True)

    doctor = st.session_state.get("selected_doctor")
    if not doctor:
        st.warning("Tidak ada dokter terpilih. Kembali ke daftar.")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    doctor_id = doctor["id"]
    history_key = f"chat_history_{doctor_id}"

    if history_key not in st.session_state:
        st.session_state[history_key] = [{"role": "doctor", "text": "Halo, ada yang bisa saya bantu?"}]

    # Header dokter (nama & spesialisasi) dengan ID khusus
    st.markdown(f"""
        <div id="chat-header" style="color:#000000 !important;">
            <p style="color:#000000 !important; font-weight:700; font-size:16px; margin:0;">{doctor['name']}</p>
            <p style="color:#000000 !important; font-size:14px; margin:0 0 10px 0; opacity:0.7;">{doctor['specialty']}</p>
        </div>
        <hr style="border:1px solid #ecdfd4; margin:10px 0;">
    """, unsafe_allow_html=True)

    # Tampilkan semua bubble
    for msg in st.session_state[history_key]:
        # === PERBAIKAN: ubah newline menjadi <br> ===
        display_text = msg["text"].replace('\n', '<br>')
        if msg["role"] == "user":
            st.markdown(f"""
            <div style="display:flex; justify-content:flex-end; margin-bottom:8px;">
                <div style="background:#fad5c5; color:#4a3525 !important; border-radius:18px 18px 4px 18px; padding:10px 16px; max-width:75%; word-wrap:break-word;">
                    {display_text}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="display:flex; justify-content:flex-start; margin-bottom:8px;">
                <div class="chat-bubble-doctor" style="background:#ffffff; color:#4a3525 !important; border-radius:18px 18px 18px 4px; padding:10px 16px; max-width:75%; word-wrap:break-word; border:1px solid #ecdfd4;">
                    <span style="color:#4a3525 !important;">{display_text}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Form input dengan clear_on_submit
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area("Tulis pesan...", height=80, label_visibility="collapsed")
        submitted = st.form_submit_button("Kirim", use_container_width=True)
        if submitted and user_input.strip():
            st.session_state[history_key].append({"role": "user", "text": user_input.strip()})
            reply = get_auto_reply(user_input.strip())
            st.session_state[history_key].append({"role": "doctor", "text": reply})
            st.rerun()
        elif submitted:
            st.warning("Pesan tidak boleh kosong.")

    st.markdown("</div>", unsafe_allow_html=True)