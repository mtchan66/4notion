# requirements.txt
# streamlit
# scikit-learn
# numpy
# matplotlib
# pandas


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

st.title("📈 實驗數據推論 App")

st.markdown("""
這個 app 可以幫助你根據「時間 vs 溫度」的數據，自動推論出最佳函數模型，並畫出圖表。
""")

# 數據輸入
st.subheader("🔢 輸入數據（時間與溫度）")

data_input = st.text_area(
    "每行一筆，格式: 時間, 溫度\n例如:\n0,20\n1,22\n2,25", 
    "0,20\n1,22\n2,25\n3,28\n4,30\n5,33"
)

lines = data_input.strip().split('\n')
x_list, y_list = [], []
for line in lines:
    parts = line.split(',')
    if len(parts) == 2:
        x_list.append(float(parts[0].strip()))
        y_list.append(float(parts[1].strip()))

x = np.array(x_list)
y = np.array(y_list)

if len(x) < 2:
    st.warning("請至少輸入兩筆以上的數據")
    st.stop()

# 選擇模型
model_type = st.radio("選擇模型類型", ["線性回歸", "多項式回歸"])

# 多項式階數
degree = 1
if model_type == "多項式回歸":
    degree = st.slider("多項式階數", min_value=2, max_value=5, value=2)

# 模型訓練
x_reshape = x.reshape(-1, 1)

if model_type == "線性回歸":
    model = LinearRegression()
    model.fit(x_reshape, y)
    y_pred = model.predict(x_reshape)
    coef = model.coef_[0]
    intercept = model.intercept_
    st.write(f"**推論結果:** y = {coef:.2f} * x + {intercept:.2f}")
else:
    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(x_reshape)
    model = LinearRegression()
    model.fit(x_poly, y)
    coef_list = model.coef_
    intercept = model.intercept_
    eq_text = "y = "
    for i, c in enumerate(coef_list):
        if i == 0:
            continue  # 常數項由 intercept 表示
        eq_text += f"{c:.2f} * x^{i} + "
    eq_text += f"{intercept:.2f}"
    st.write(f"**推論結果:** {eq_text}")

# 畫圖
x_line = np.linspace(min(x) - 1, max(x) + 1, 200).reshape(-1, 1)
if model_type == "線性回歸":
    y_line = model.predict(x_line)
else:
    x_line_poly = poly.transform(x_line)
    y_line = model.predict(x_line_poly)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, color='red', label='實驗數據')
ax.plot(x_line, y_line, color='blue', label='擬合曲線')
ax.set_xlabel("時間")
ax.set_ylabel("溫度")
ax.set_title("實驗數據與擬合結果")
ax.legend()
ax.grid(True)

st.pyplot(fig)
