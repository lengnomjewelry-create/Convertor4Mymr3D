import streamlit as st

# --- CONSTANTS ---
GRAMS_PER_KYAT = 16.6
GRAMS_PER_CARAT = 0.2
RATTI_RATIO = 0.91  
MM_PER_INCH = 25.4

st.set_page_config(page_title="Jewelry & Gold Converter", layout="centered")
st.title("💎 Jewelry & Gold Converter")
st.markdown("---")

menu = st.sidebar.radio(
    "Select Conversion Tool",
    ["ရွှေအလေးချိန် (Gold Weight)", "ကျောက်မျက်ရတနာ (Gemstones)", "အလျားတိုင်းတာခြင်း (Length)", "စုစုပေါင်းအလေးချိန် (Combined)"]
)

# --- 1. GOLD WEIGHT CONVERTER ---
if menu == "ရွှေအလေးချိန် (Gold Weight)":
    st.header("ရွှေအလေးချိန် တွက်ချက်ရန်")
    tab1, tab2 = st.tabs(["ဂရမ် မှ ကျပ်ပဲရွေး", "ကျပ်ပဲရွေး မှ ဂရမ်"])

    with tab1:
        grams = st.number_input("ဂရမ် (Grams) ထည့်ပါ", value=16.6, step=0.01, format="%.4f")
        total_kyat = grams / GRAMS_PER_KYAT
        kyat = int(total_kyat)
        rem_pe = (total_kyat - kyat) * 16
        pe = int(rem_pe)
        rem_ywe = (rem_pe - pe) * 8
        ywe = int(rem_ywe)
        points = (rem_ywe - ywe) * 10
        
        st.subheader("ရလဒ်")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("ကျပ်", kyat)
        col2.metric("ပဲ", pe)
        col3.metric("ရွေး", ywe)
        # Updated to 2 decimal places
        col4.metric("Point", f"{points:.2f}")

    with tab2:
        colA, colB, colC, colD = st.columns(4)
        k_in = colA.number_input("ကျပ်", min_value=0, value=1)
        p_in = colB.number_input("ပဲ", min_value=0, max_value=15, value=0)
        y_in = colC.number_input("ရွေး", min_value=0, max_value=7, value=0)
        # Updated: step 0.01 and format %.2f
        pt_in = colD.number_input("Point", min_value=0.0, max_value=9.99, value=0.0, step=0.01, format="%.2f")
        
        total_k = k_in + (p_in/16) + (y_in/128) + (pt_in/1280)
        total_g = total_k * GRAMS_PER_KYAT
        st.success(f"စုစုပေါင်း ဂရမ်: **{total_g:.4f} g**")

# --- 2. GEMSTONE CONVERTER ---
elif menu == "ကျောက်မျက်ရတနာ (Gemstones)":
    st.header("ကျောက်မျက် နှင့် ရတီ တွက်ချက်ရန်")
    col1, col2 = st.columns(2)
    with col1:
        carat = st.number_input("ကာရက် (Carat)", value=1.3, step=0.01, format="%.2f")
        ratti = carat / RATTI_RATIO
        st.metric("ရတီ (Ratti)", f"{ratti:.4f}")
    with col2:
        amount = st.number_input("အရေအတွက် (Amount)", value=100, min_value=1)
        st.metric("တစ်လုံးချင်းအလေးချိန်", f"{(carat/amount):.4f} ct")

    st.divider()
    sieve = amount / ratti if ratti > 0 else 0.0
    st.metric("လုံးစီး (Sieve Size)", f"{sieve:.2f}")

# --- 3. LENGTH CONVERTER ---
elif menu == "အလျားတိုင်းတာခြင်း (Length)":
    st.header("အလျားတိုင်းတာရန် (လက်မ ပဲ ပြား)")
    tab3, tab4 = st.tabs(["မီလီမီတာ မှ လက်မ", "လက်မ မှ မီလီမီတာ"])

    with tab3:
        mm = st.number_input("မီလီမီတာ (mm) ထည့်ပါ", value=25.4, step=0.1)
        total_inch = mm / MM_PER_INCH
        inches = int(total_inch)
        rem_pe_len = (total_inch - inches) * 16
        pe_len = int(rem_pe_len)
        pya = (rem_pe_len - pe_len) * 4
        
        st.subheader("ရလဒ်")
        c1, c2, c3 = st.columns(3)
        c1.metric("လက်မ", inches)
        c2.metric("ပဲ", pe_len)
        # Updated to 2 decimal places
        c3.metric("ပြား", f"{pya:.2f}")

    with tab4:
        c_i, c_p, c_py = st.columns(3)
        in_v = c_i.number_input("လက်မ", value=1)
        pe_v = c_p.number_input("ပဲ", value=0, max_value=15)
        # Updated: step 0.01 and format %.2f
        py_v = c_py.number_input("ပြား", value=0.0, max_value=3.99, step=0.01, format="%.2f")
        
        total_in = in_v + (pe_v/16) + (py_v/64)
        res_mm = total_in * MM_PER_INCH
        st.success(f"စုစုပေါင်း မီလီမီတာ: **{res_mm:.4f} mm**")

# --- 4. COMBINED WEIGHT ---
elif menu == "စုစုပေါင်းအလေးချိန် (Combined)":
    st.header("ရွှေ နှင့် ကျောက် စုစုပေါင်းအလေးချိန်")
    st.subheader("ရွှေအလေးချိန်")
    col_k, col_p, col_y, col_pt = st.columns(4)
    gk = col_k.number_input("ကျပ်", value=1, key="comb_k")
    gp = col_p.number_input("ပဲ", value=0, key="comb_p")
    gy = col_y.number_input("ရွေး", value=0, key="comb_y")
    # Updated: step 0.01 and format %.2f
    gpt = col_pt.number_input("Point", value=0.0, step=0.01, format="%.2f", key="comb_pt")
    
    gold_g = (gk + gp/16 + gy/128 + gpt/1280) * GRAMS_PER_KYAT
    
    st.subheader("ကျောက်အလေးချိန်")
    gem_ct = st.number_input("စုစုပေါင်း ကာရက် (Carat)", value=3.0, step=0.01, format="%.2f")
    gem_g = gem_ct * GRAMS_PER_CARAT
    
    st.divider()
    st.metric("စုစုပေါင်းအလေးချိန် (ဂရမ်)", f"{gold_g + gem_g:.4f} g")

# --- SIDEBAR SUPPORT SECTION ---
st.sidebar.markdown("---")
st.sidebar.subheader("☕ Support the Developer")
st.sidebar.write("If this tool helps you, feel free to **buy me a coffee!**")

# Display the QR Code
try:
    # Ensure you have your KBZPay QR image saved as 'kbzpay.jpg' in your folder
    st.sidebar.image("kbzpay.jpg", caption="Scan to Tip via KBZPay")
except:
    st.sidebar.info("📷 [KBZPay QR Code Placeholder]")

st.sidebar.markdown("""
**How to support:**
1. Open KBZPay app.
2. Scan the QR code above.
3. Enter any amount you like!
""")

# Optional: Add a contact button
st.sidebar.markdown("---")
if st.sidebar.button("📞 Contact for Support"):
    st.sidebar.write("Viber/Phone: **09-973145067**")