import streamlit as st

# ==========================
# TIÊU ĐỀ
# ==========================
st.set_page_config(
    page_title="Tính tiền phòng trọ",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 HỆ THỐNG TÍNH CHI PHÍ PHÒNG TRỌ")
st.write("Nhập các thông tin dưới đây để tính tổng chi phí sinh hoạt hàng tháng.")

# ==========================
# TIỀN PHÒNG
# ==========================
st.header("🏠 Tiền phòng")

A = st.number_input(
    "Tiền phòng (đồng)",
    min_value=0.0,
    value=3000000.0,
    step=100000.0
)

# ==========================
# TIỀN ĐIỆN
# ==========================
st.header("⚡ Tiền điện")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Chỉ số đầu tháng",
        min_value=0.0,
        value=100.0
    )

with col2:
    b = st.number_input(
        "Chỉ số cuối tháng",
        min_value=0.0,
        value=150.0
    )

c = st.number_input(
    "Đơn giá điện (đồng/kWh)",
    min_value=0.0,
    value=3500.0
)

# ==========================
# TIỀN NƯỚC
# ==========================
st.header("💧 Tiền nước")

col3, col4 = st.columns(2)

with col3:
    x = st.number_input(
        "Chỉ số đầu tháng",
        min_value=0.0,
        value=20.0
    )

with col4:
    y = st.number_input(
        "Chỉ số cuối tháng",
        min_value=0.0,
        value=30.0
    )

z = st.number_input(
    "Đơn giá nước (đồng/m³)",
    min_value=0.0,
    value=15000.0
)

# ==========================
# WIFI
# ==========================
st.header("📶 Tiền Internet/WiFi")

W = st.number_input(
    "Tiền WiFi (đồng)",
    min_value=0.0,
    value=100000.0,
    step=10000.0
)

# ==========================
# TÍNH TOÁN
# ==========================
if st.button("💰 TÍNH TỔNG CHI PHÍ", use_container_width=True):

    so_dien = b - a
    so_nuoc = y - x

    tien_dien = so_dien * c
    tien_nuoc = so_nuoc * z

    tong = A + tien_dien + tien_nuoc + W

    st.divider()

    st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("⚡ Tiền điện", f"{tien_dien:,.0f} đ")
        st.metric("💧 Tiền nước", f"{tien_nuoc:,.0f} đ")

    with c2:
        st.metric("📶 Tiền WiFi", f"{W:,.0f} đ")
        st.metric("🏠 Tiền phòng", f"{A:,.0f} đ")

    st.success(f"💵 TỔNG CHI PHÍ PHẢI THANH TOÁN: {tong:,.0f} đồng")

    st.balloons()
