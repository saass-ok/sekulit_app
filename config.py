"""
Design tokens untuk aplikasi SEKULIT.
Semua nilai layout, warna, dan tipografi disatukan di sini
supaya konsisten dan gampang diubah di satu tempat.
"""

# ---------- Layout (mengacu ke frame mobile 390x844) ----------
FRAME_WIDTH = 390
FRAME_HEIGHT = 844
MARGIN = 12
CONTENT_WIDTH = 366

HEADER_H = 56
BOTTOM_NAV_H = 72

BTN_PRIMARY_H = 44
BTN_SECONDARY_H = 38
INPUT_H = 42

RADIUS_BUTTON = 12
RADIUS_INPUT = 12
RADIUS_CARD = 14
CARD_PADDING = 12

SPACING = {"xs": 6, "sm": 12, "md": 18, "lg": 24}

# ---------- Tipografi ----------
FS_HEADING = 22
FS_PAGE_TITLE = 17
FS_SUBHEADING = 15
FS_BODY = 13
FS_CAPTION = 11
FS_BUTTON = 13

# ---------- Warna ----------
COLOR_BG = "#faf8f5"          # background utama + teks di atas background gelap
COLOR_DARK = "#4a3525"        # ikon & teks di atas background terang
COLOR_ACCENT = "#fad5c5"      # ikon aksen / highlight

# turunan (biar konsisten, tidak hardcode ulang)
COLOR_CARD_BG = "#ffffff"
COLOR_BORDER = "#ecdfd4"
COLOR_MUTED = "#8a7a6d"

# ---------- Navigasi bottom nav ----------
# key -> (label, material icon, root page yang dituju)
NAV_ITEMS = [
    ("beranda", "Beranda", ":material/home:"),
    ("cek_kulit", "Cek Kulit", ":material/search:"),
    ("konsultasi", "Konsultasi", ":material/chat_bubble:"),
    ("rekomendasi_obat", "Obat", ":material/local_hospital:"),
    ("informasi", "Informasi", ":material/info:"),
]

# Judul header per halaman (yang punya back navigation)
PAGE_TITLES = {
    "cek_kulit_input": "Cek Kulit",
    "cek_kulit_output": "Hasil Estimasi",
    "konsultasi_list": "Konsultasi Dokter",
    "konsultasi_chat": "Chat Dokter",
    "rekomendasi_obat": "Rekomendasi Obat",
    "informasi": "Informasi",
    "informasi_detail": "Artikel",
}

# Halaman yang merupakan "root" dari tiap tab bottom nav
TAB_ROOT_PAGE = {
    "beranda": "beranda",
    "cek_kulit": "cek_kulit_input",
    "konsultasi": "konsultasi_list",
    "rekomendasi_obat": "rekomendasi_obat",
    "informasi": "informasi",
}

# Pemetaan halaman -> tab yang harus ter-highlight di bottom nav
PAGE_TO_TAB = {
    "beranda": "beranda",
    "cek_kulit_input": "cek_kulit",
    "cek_kulit_output": "cek_kulit",
    "konsultasi_list": "konsultasi",
    "konsultasi_chat": "konsultasi",
    "rekomendasi_obat": "rekomendasi_obat",
    "informasi": "informasi",
    "informasi_detail": "informasi",
}
