import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# macOS 字型 (optional)
plt.rcParams['font.family'] = 'PingFang TC'
plt.rcParams['axes.unicode_minus'] = False

def f(x):
    return x**3 - 3*x**2 + 2

def df(x):
    return 3*x**2 - 6*x

st.title("Secant to Tangent Animation")

# 選 x0
x0 = st.slider("Choose x₀", min_value=-0.5, max_value=3.5, value=2.0, step=0.1)

# 啟動動畫按鈕
start_anim = st.button("Start Animation")

if start_anim:
    x = np.linspace(-1, 4, 300)
    y = f(x)

    h_values = np.linspace(1.5, 0.01, 30)  # h 從大到小

    for h in h_values:
        x1 = x0 + h
        y0 = f(x0)
        y1 = f(x1)

        delta_x = x1 - x0
        delta_y = y1 - y0

        secant_slope = delta_y / delta_x
        tangent_slope = df(x0)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label='f(x) = x³ - 3x² + 2', color='black')

        # 割線
        secant_y = secant_slope * (x - x0) + y0
        ax.plot(x, secant_y, '--', color='blue', label=f'Secant (slope = {secant_slope:.2f})')

        # 切線
        tangent_y = tangent_slope * (x - x0) + y0
        ax.plot(x, tangent_y, '--', color='orange', label=f'Tangent (slope = {tangent_slope:.2f})')

        # 點
        ax.scatter([x0, x1], [y0, y1], color='red', zorder=5)

        # Δx arrow
        ax.annotate("", xy=(x1, y0), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle='<->', color='green', linewidth=2))
        ax.text((x0 + x1) / 2, y0 - 5, f"Δx = {delta_x:.2f}", ha='center', va='top', fontsize=12, color='green')

        # Δy arrow
        ax.annotate("", xy=(x1, y1), xytext=(x1, y0),
                    arrowprops=dict(arrowstyle='<->', color='purple', linewidth=2))
        ax.text(x1 + 0.1, (y0 + y1) / 2, f"Δy = {delta_y:.2f}", va='center', fontsize=12, color='purple')

        # 說明
        ax.text(0.05, 0.95,
                f'Secant slope = {secant_slope:.2f}\nTangent slope = {tangent_slope:.2f}',
                transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Secant Approaching Tangent')
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
        time.sleep(0.3)  # 控制動畫速度
