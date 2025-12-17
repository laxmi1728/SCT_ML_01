import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM THEME / CSS ----------------
st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #ffffff;
}
.sub-title {
    font-size: 18px;
    color: #c7d2fe;
}
.card {
    background: linear-gradient(145deg, #0f172a, #020617);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.6);
}
.metric {
    font-size: 36px;
    font-weight: 800;
    color: #34d399;
}
.label {
    color: #94a3b8;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🏠 House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-powered price estimation using Linear Regression</div>', unsafe_allow_html=True)

st.divider()

# ---------------- LOAD DATA & TRAIN MODEL ----------------
df = pd.read_csv("train.csv")

X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']
X = X.fillna(X.mean())

model = LinearRegression()
model.fit(X, y)

# ---------------- SIDEBAR INPUT ----------------
st.sidebar.header("🏡 Property Details")

area = st.sidebar.slider(
    "Living Area (sq ft)",
    min_value=10,
    max_value=10000,
    value=1500,
    step=50
)

bedrooms = st.sidebar.selectbox(
    "Bedrooms",
    [1, 2, 3, 4, 5, 6,7,8,9,10]
)

bathrooms = st.sidebar.selectbox(
    "Bathrooms",
    [1, 2, 3, 4,5,6,7,8,9,10]
)

predict = st.sidebar.button("🔮 Predict Price")

# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([1, 2])

with left:
    st.markdown("### 📊 Model Information")
    st.info("""
    **Algorithm:** Linear Regression  
    **Inputs Used:**
    - Living Area
    - Bedrooms
    - Bathrooms  

    Trained on real housing data.
    """)

with right:
    st.markdown("### 💰 Estimated Valuation")

    if predict:
        user_data = pd.DataFrame({
            'GrLivArea': [area],
            'BedroomAbvGr': [bedrooms],
            'FullBath': [bathrooms]
        })

        price = model.predict(user_data)[0]

        st.markdown(f"""
        <div class="card">
            <div class="label">Predicted House Price</div>
            <div class="metric">₹ {price:,.0f}</div>
            <div class="label">Based on current inputs</div>
        </div>
        """, unsafe_allow_html=True)

        st.metric("Price per sq ft", f"₹ {int(price/area):,}")
    else:
        st.warning("⬅️ Enter property details and click Predict")


