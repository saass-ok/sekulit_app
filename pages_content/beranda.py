# pages_content/beranda.py
import streamlit as st
import streamlit.components.v1 as components
from state import go_to
import os

def render():
    # HEADER - SEKULIT lebih besar
    st.markdown(
        """
        <div style="margin-bottom:6px;">
            <p style="font-size:30px; font-weight:900; margin:0; color:#4A3525; letter-spacing:1px;">SEKULIT</p>
            <h2 style="font-size:20px; font-weight:800; margin:6px 0 0 0; color:#4A3525;">Halo, Selamat Datang !!!</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # HERO (isolated iframe, tanpa scrollbar internal)
    hero_html = r"""
    <html><head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        html,body{margin:0;padding:0;overflow-y:hidden;font-family:Plus-Jakarta,system-ui,Arial;color:#4A3525;}
        .hero-carousel{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding:6px 0;}
        .hero-card{flex:0 0 100%;min-width:100%;scroll-snap-align:start;background:#4A3121;color:#fff;border-radius:14px;padding:12px;box-sizing:border-box;display:flex;gap:12px;align-items:center;min-height:120px;max-height:150px;overflow:hidden;box-shadow:0 6px 18px rgba(74,49,33,0.06);}
        .hero-title{font-weight:800;font-size:14px;margin:0;}
        .hero-desc{font-size:11px;color:#E8D7CB;margin-top:8px;line-height:1.25; -webkit-line-clamp:4; display:-webkit-box; -webkit-box-orient:vertical; overflow:hidden;}
        .illus{width:60px;flex-shrink:0;text-align:right;}
        .illus img{width:48px;border-radius:8px;background:rgba(255,255,255,0.03);padding:6px;display:block;}
        .dots{text-align:center;margin-top:8px;}
        .dots .big{display:inline-block;width:18px;height:4px;background:#4A3121;border-radius:4px;margin-right:8px;}
        .dots .small{display:inline-block;width:6px;height:6px;background:#FCD5C3;border-radius:50%;margin-right:6px;}
      </style>
    </head><body>
      <div class="hero-carousel" role="region" aria-label="hero-carousel">
        <div class="hero-card">
          <div style="flex:1">
            <div class="hero-title">Kenali dan Jaga Kesehatan Kulitmu !!!</div>
            <div class="hero-desc">Kenali kondisi kulitmu sejak dini bersama SEKULIT. Sistem estimasi kondisi kulit yang dirancang secara digital untuk membantu memantau kesehatan lesi kulit secara praktis, cepat, dan terpercaya.</div>
          </div>
          <div class="illus"><img src="https://cdn-icons-png.flaticon.com/512/3209/3209074.png" alt="illus1"/></div>
        </div>

        <div class="hero-card">
          <div style="flex:1">
            <div class="hero-title">Deteksi Dini Lesi Abnormal</div>
            <div class="hero-desc">Analisis foto lesi/tahi lalat menggunakan AI ensemble presisi tinggi untuk membantu deteksi lebih cepat.</div>
          </div>
          <div class="illus"><img src="https://cdn-icons-png.flaticon.com/512/2818/2818228.png" alt="illus2"/></div>
        </div>

        <div class="hero-card">
          <div style="flex:1">
            <div class="hero-title">Konsultasi & Penanganan</div>
            <div class="hero-desc">Panduan perawatan awal serta rujukan ke fasilitas kesehatan terdekat jika diperlukan.</div>
          </div>
          <div class="illus"><img src="https://cdn-icons-png.flaticon.com/512/387/387561.png" alt="illus3"/></div>
        </div>
      </div>

      <div class="dots" aria-hidden="true">
        <span class="big"></span><span class="small"></span><span class="small"></span>
      </div>
    </body></html>
    """
    components.html(hero_html, height=150, scrolling=False)

    # History card (native streamlit)
    st.markdown(
        """
        <div style="margin-top:8px;">
          <div style="border:1.5px solid #FCD5C3; border-radius:12px; padding:10px; display:flex; align-items:center; justify-content:space-between; background:#fff; box-shadow:0 6px 18px rgba(74,49,33,0.05);">
            <div style="display:flex; gap:12px; align-items:center;">
              <div style="width:44px; height:44px; border-radius:10px; background:#FCD5C3; display:flex; align-items:center; justify-content:center; font-size:18px; color:#4A3525;">🕒</div>
              <div>
                <div style="font-weight:700; font-size:13px; color:#4A3525;">Riwayat Cek Terakhir</div>
                <div style="font-size:11px; color:#7A6859; margin-top:4px;">20 Juni 2026</div>
              </div>
            </div>
            <div style="font-size:20px; color:#4A3525;">›</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # CTA (di atas artikel)
    st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)
    if st.button("🔍  Mulai Cek Kulit Sekarang", key="home_cek_kulit"):
        go_to("cek_kulit_input")

    # Section title
    st.markdown('<div style="margin-top:8px; margin-bottom:6px;"><strong style="font-size:13px; color:#4A3525;">Artikel Kesehatan Kulit Terpopuler</strong></div>', unsafe_allow_html=True)

    # ==================== ARTIKEL ====================
    # Gunakan st.image() untuk menampilkan gambar, lalu bungkus dengan link HTML

    # Path gambar
    img1_path = "assets/kelembaban kulit.jpg"
    img2_path = "assets/kulit jari mengelupas.jpg"

    # Fallback jika file tidak ada
    if not os.path.exists(img1_path):
        img1_path = "https://via.placeholder.com/400x200/FCD5C3/4A3525?text=Kelembaban"
    if not os.path.exists(img2_path):
        img2_path = "https://via.placeholder.com/400x200/FCD5C3/4A3525?text=Kulit+Jari"

    # URL artikel
    url1 = "https://www.healthline.com/health/beauty-skin-care/hydrate-dry-skin"
    url2 = "https://www.webmd.com/skin-problems-and-treatments/what-know-about-peeling-skin-desquamation"

    col1, col2 = st.columns(2, gap="small")

    with col1:
        # Tampilkan gambar dengan st.image (lebih andal)
        st.image(img1_path, use_container_width=True)
        # Tulis label di bawah gambar, dengan link
        st.markdown(f'<a href="{url1}" target="_blank" style="text-decoration:none; color:#4A3525; font-weight:700; font-size:13px; display:block; text-align:center; margin-top:4px;">Kelembapan Kulit</a>', unsafe_allow_html=True)

    with col2:
        st.image(img2_path, use_container_width=True)
        st.markdown(f'<a href="{url2}" target="_blank" style="text-decoration:none; color:#4A3525; font-weight:700; font-size:13px; display:block; text-align:center; margin-top:4px;">Kulit Jari Mengelupas</a>', unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)