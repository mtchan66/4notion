import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ✅ macOS 設定中文字型
# plt.rcParams['font.family'] = 'PingFang TC'
# plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Heiti TC'  

# 定義函數 f(x) 與其導數 f'(x)
def f(x):
    return x**3 - 3*x**2 + 2

def df(x):
    return 3*x**2 - 6*x

st.title("割線 vs 切線（Streamlit 互動版）")

# Streamlit 用 slider
x0 = st.slider("x₀", min_value=-0.5, max_value=3.5, value=2.0, step=0.1)
h = st.slider("h", min_value=0.01, max_value=2.0, value=1.0, step=0.05)

x1 = x0 + h
y0 = f(x0)
y1 = f(x1)

# 割線斜率
secant_slope = (y1 - y0) / (x1 - x0)

# 切線斜率
tangent_slope = df(x0)

x = np.linspace(-1, 4, 300)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='f(x) = x³ - 3x² + 2', color='black')

# 畫割線
secant_y = secant_slope * (x - x0) + y0
ax.plot(x, secant_y, '--', color='blue', label=f'割線 (斜率={secant_slope:.2f})')

# 畫切線
tangent_y = tangent_slope * (x - x0) + y0
ax.plot(x, tangent_y, '--', color='orange', label=f'切線 (斜率={tangent_slope:.2f})')

# 標示兩點
ax.scatter([x0, x1], [y0, y1], color='red', zorder=5)

# 顯示斜率文字
ax.text(0.05, 0.95, f'割線斜率 = {secant_slope:.2f}\n切線斜率 = {tangent_slope:.2f}',
        transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('割線 vs 切線（顯示斜率）')
ax.legend()
ax.grid(True)

st.pyplot(fig)
    
