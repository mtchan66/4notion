import streamlit as st

st.title("Hello, World!")
st.write("這是我第一個 Streamlit App 🤗🎉")

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# 定義函數 f(x) 與其導數 f'(x)
def f(x):
    return x**3 - 3*x**2 + 2

def df(x):
    return 3*x**2 - 6*x

# 畫圖函式
def plot_secant_tangent(x0=2.0, h=1.0):
    x1 = x0 + h
    y0 = f(x0)
    y1 = f(x1)

    # 割線斜率
    secant_slope = (y1 - y0) / (x1 - x0)

    # 切線斜率
    tangent_slope = df(x0)

    # 畫圖區間
    x = np.linspace(-1, 4, 300)
    y = f(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x) = x³ - 3x² + 2', color='black')

    # 畫割線
    secant_y = secant_slope * (x - x0) + y0
    plt.plot(x, secant_y, '--', color='blue', label=f'割線 (斜率={secant_slope:.2f})')

    # 畫切線
    tangent_y = tangent_slope * (x - x0) + y0
    plt.plot(x, tangent_y, '--', color='orange', label=f'切線 (斜率={tangent_slope:.2f})')

    # 標示兩點
    plt.scatter([x0, x1], [y0, y1], color='red', zorder=5)

    # 顯示斜率文字
    plt.text(0.05, 0.95, f'割線斜率 = {secant_slope:.2f}\n切線斜率 = {tangent_slope:.2f}',
             transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('割線 vs 切線（顯示斜率）')
    plt.legend()
    plt.grid(True)
    plt.show()
