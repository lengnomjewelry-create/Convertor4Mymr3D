import streamlit as st

# --- 1. SETUP & PAGE CONFIG ---
LOGO_URL = "https://raw.githubusercontent.com/lengnomjewelry-create/Convertor4Mymr3D/main/logo.png"

st.set_page_config(
    page_title="စံ Jewelry Converter", 
    layout="centered", 
    page_icon=LOGO_URL
)

# FIXED CSS: iOS 4 Skeuomorphic Theme
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pyidaungsu:wght@400;700&display=swap');

    /* Global Background - iOS Classic Linen Texture fallback */
    .main {{
        background-color: #c5c9d1;
        background-image: radial-gradient(#d1d5db 0.5px, transparent 0.5px);
        background-size: 4px 4px;
    }}

    /* Results Box - iOS 4 High Gloss Skeuomorphism */
    .result-box {{
        background: linear-gradient(to bottom, #ffffff 0%, #e0e0e0 50%, #d1d1d1 51%, #ebebeb 100%);
        border: 1px solid #a1a1a1;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.8);
        color: #333;
    }}

    /* Professional Gold Display - iOS 4 Style Emboss */
    .yellow-val {{
        color: #2c3e50; 
        font-family: 'Pyidaungsu', sans-serif;
        font-weight: 700;
        font-size: 36px;
        text-shadow: 0 1px 0 rgba(255,255,255,0.8);
    }}

    .unit-text {{
        color: #666;
        font-size: 14px;
        margin-right: 5px;
        font-weight: bold;
    }}

    /* Header Styling - Updated to Yellow Gold */
    .my-logo {{
        color: #FFD700; /* Gold color for the [စံ] logo */
        font-weight: 700;
        font-size: 38px;
        margin-right: 10px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }}
    
    .header-text {{
        color: #FFD700; /* Matching Gold for the Title */
        font-size: 30px;
        font-weight: bold;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }}

    /* iOS 4 Button-like headers for tabs */
    .stTabs [data-baseweb="tab-list"] {{
        background: linear-gradient(to bottom, #7d8e9e 0%, #4a5a6a 100%);
        border-radius: 8px 8px 0 0;
        padding: 4px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        color: white !important;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONSTANTS ---
GRAMS_PER_KYAT = 16.6
GRAMS_PER_CARAT = 0.2
RATTI_RATIO = 0.91  
MM_PER_INCH = 25.4

# --- 3. HEADER ---
st.markdown('<p><span class="my-logo">[စံ]</span> <span class="header-text">Jewelry Converter</span></p>', unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    menu = st.radio("Select Tool", ["ရွှေအလေးချိန် (Gold)", "ကျောက်မျက် (Gems)", "အလျား (Length)", "အသားတင်ရွှေ (Net Gold)"])
    st.markdown("---")
    st.subheader("☕ Buy me a coffee")
    st.write("ဒီ App လေးကို အားလုံးအတွက် အဆင်ပြေအောင် စေတနာနဲ့ အခမဲ့ ဖန်တီးပေးထားတာပါ။ 🙏")
    try:
        st.image("kbzpay.jpg")
    except:
        st.info("Scan KBZPay to support")
    st.info("**Contact:** 09-973145067")

# --- 5. GOLD WEIGHT ---
if menu == "ရွှေအလေးချိန် (Gold)":
    st.header("ရွှေအလေးချိန် တွက်ချက်ရန်")
    t1, t2 = st.tabs(["ဂရမ် မှ ကျပ်ပဲရွေး", "ကျပ်ပဲရွေး မှ ဂရမ်"])
    
    with t1:
        g_in = st.number_input("ဂရမ် (Grams)", value=16.6, format="%.4f", key="gold_g_in", min_value=0.0)
        tk = g_in / GRAMS_PER_KYAT
        k = int(tk)
        p = int((tk - k) * 16)
        y = int(((tk - k) * 16 - p) * 8)
        pt = (((tk - k) * 16 - p) * 8 - y) * 10
        st.markdown(f'<div class="result-box"><span class="yellow-val">{k}</span> <span class="unit-text">ကျပ်</span> <span class="yellow-val">{p}</span> <span class="unit-text">ပဲ</span> <span class="yellow-val">{y}</span> <span class="unit-text">ရွေး</span> <span class="yellow-val">{pt:.2f}</span> <span class="unit-text">Pt</span></div>', unsafe_allow_html=True)

    with t2:
        c1, c2, c3, c4 = st.columns(4)
        k_i = c1.number_input("ကျပ်", value=0, key="gold_k_in", min_value=0)
        p_i = c2.number_input("ပဲ", value=0, key="gold_p_in", min_value=0)
        y_i = c3.number_input("ရွေး", value=0, key="gold_y_in", min_value=0)
        pt_i = c4.number_input("Point", value=0.0, step=0.01, key="gold_pt_in", min_value=0.0)
        tg = (k_i + p_i/16 + y_i/128 + pt_i/1280) * GRAMS_PER_KYAT
        st.markdown(f'<div class="result-box"><p style="margin-bottom:5px; font-weight:bold;">စုစုပေါင်း ဂရမ်</p><span class="yellow-val">{tg:.4f}</span> <span class="unit-text">g</span></div>', unsafe_allow_html=True)

# --- 6. GEMSTONES ---
elif menu == "ကျောက်မျက် (Gems)":
    st.header("ကျောက်မျက် နှင့် ရတီ တွက်ချက်ရန်")
    ct = st.number_input("ကာရက် (Carat)", value=1.3, key="gem_ct_in", min_value=0.0)
    qty = st.number_input("အရေအတွက်", value=100, key="gem_qty_in", min_value=0)
    rt = ct / RATTI_RATIO
    sv = qty / rt if rt > 0 else 0
    st.markdown(f'<div class="result-box"><span class="yellow-val">{rt:.4f}</span> <span class="unit-text">ရတီ</span><br><span class="yellow-val">{sv:.2f}</span> <span class="unit-text">လုံးစီး</span></div>', unsafe_allow_html=True)

# --- 7. LENGTH ---
elif menu == "အလျား (Length)":
    st.header("အလျားတိုင်းတာရန်")
    t3, t4 = st.tabs(["mm to Inch", "Inch to mm"])
    with t3:
        m_in = st.number_input("မီလီမီတာ (mm)", value=25.4, key="len_mm_in", min_value=0.0)
        ti = m_in / MM_PER_INCH
        i, pe, py = int(ti), int((ti-int(ti))*16), ((ti-int(ti))*16-int((ti-int(ti))*16))*4
        st.markdown(f'<div class="result-box"><span class="yellow-val">{i}</span> <span class="unit-text">လက်မ</span> <span class="yellow-val">{pe}</span> <span class="unit-text">ပဲ</span> <span class="yellow-val">{py:.2f}</span> <span class="unit-text">ပြား</span></div>', unsafe_allow_html=True)
    with t4:
        c1, c2, c3 = st.columns(3)
        i_i = c1.number_input("လက်မ", value=1, key="len_i_in", min_value=0)
        pe_i = c2.number_input("ပဲ", value=0, key="len_pe_in", min_value=0)
        py_i = c3.number_input("ပြား", value=0.0, key="len_py_in", min_value=0.0)
        t_mm = (i_i + pe_i/16 + py_i/64) * MM_PER_INCH
        st.markdown(f'<div class="result-box"><p style="margin-bottom:5px; font-weight:bold;">မီလီမီတာ</p><span class="yellow-val">{t_mm:.4f}</span> <span class="unit-text">mm</span></div>', unsafe_allow_html=True)

# --- 8. NET GOLD ---
elif menu == "အသားတင်ရွှေ (Net Gold)":
    st.header("ရွှေအသားတင်အလေးချိန်")
    st.subheader("၁။ ပစ္စည်းတစ်ခုလုံးအလေးချိန်")
    c1, c2, c3, c4 = st.columns(4)
    tk_i = c1.number_input("ကျပ်", value=1, key="net_k", min_value=0)
    tp_i = c2.number_input("ပဲ", value=0, key="net_p", min_value=0)
    ty_i = c3.number_input("ရွေး", value=0, key="net_y", min_value=0)
    tpt_i = c4.number_input("Point", value=0.0, key="net_pt", min_value=0.0)
    st.subheader("၂။ ကျောက်မျက်အလေးချိန်")
    g_ct = st.number_input("ကာရက် (Carat)", value=3.0, key="net_ct", min_value=0.0)
    
    total_g = (tk_i + tp_i/16 + ty_i/128 + tpt_i/1280) * GRAMS_PER_KYAT
    gem_g = g_ct * GRAMS_PER_CARAT
    net_g = total_g - gem_g
    
    ntk = net_g / GRAMS_PER_KYAT
    nk, np, ny = int(ntk), int((ntk-int(ntk))*16), int(((ntk-int(ntk))*16-int((ntk-int(ntk))*16))*8)
    npt = (((ntk-int(ntk))*16-int((ntk-int(ntk))*16))*8 - ny) * 10

    st.markdown(f'<div class="result-box"><span class="yellow-val">{net_g:.4f}</span> <span class="unit-text">g</span><br><span class="yellow-val">{nk}</span><span class="unit-text">ကျပ်</span> <span class="yellow-val">{np}</span><span class="unit-text">ပဲ</span> <span class="yellow-val">{ny}</span><span class="unit-text">ရွေး</span> <span class="yellow-val">{npt:.2f}</span><span class="unit-text">pt</span></div>', unsafe_allow_html=True)