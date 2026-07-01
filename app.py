import streamlit as st

# Tiêu đề ứng dụng
st.title("🏠 TÍNH TIỀN PHÒNG TRỌ HÀNG THÁNG")

# Nhập tiền phòng
A = st.number_input(
    "Nhập số tiền phòng (đồng)",
    min_value=0.0,
    value=300000000.0
)

# Nhập chỉ số điện
st.subheader("⚡ Tiền điện")
a = st.number_input(
    "Nhập số điện đầu tháng",
    min_value=0.0,
    value=100.0
)

b = st.number_input(
    "Nhập số điện cuối tháng",
    min_value=0.0,
    value=150.0
)

c = st.number_input(
    "Nhập đơn giá 1 số điện (đồng)",
    min_value=0.0,
    value=3500.0
)

# Nhập chỉ số nước
st.subheader("💧 Tiền nước")
x = st.number_input(
    "Nhập số nước đầu tháng",
    min_value=0.0,
    value=20.0
)

y = st.number_input(
    "Nhập số nước cuối tháng",
    min_value=0.0,
    value=30.0
)

z = st.number_input(
    "Nhập đơn giá 1 số nước (đồng)",
    min_value=0.0,
    value=15000.0
)

# Nhập tiền WiFi
st.subheader("📶 Tiền WiFi")
W = st.number_input(
    "Nhập tiền WiFi (đồng)",
    min_value=0.0,
    value=100000.0
)

# Nút tính toán
if st.button("Tính tiền phòng trọ"):
    B = (b - a) * c
    C = (y - x) * z
    D = A + B + C + W

    st.success(f"Tổng tiền điện: {B:,.0f} đồng")
    st.success(f"Tổng tiền nước: {C:,.0f} đồng")
    st.success(f"Tiền WiFi: {W:,.0f} đồng")
    st.success(f"Tổng tiền phòng trọ của 1 tháng: {D:,.0f} đồng")
