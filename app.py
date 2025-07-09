import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ✅ macOS set font (optional, for Chinese)
plt.rcParams['font.family'] = 'PingFang TC'
plt.rcParams['axes.unicode_minus'] = False

def f(x):
    return x**3 - 3*x**2 + 2

def df(x):
    return 3*x**2 - 6*x

st.title("Secant vs Tangent")

x0 = st.slider("x₀", min_value=-0.5, max_value=3.5, value=2.0, step=0.1)
h = st.slider("h", min_value=0.01, max_value=2.0, value=1.0, step=0.05)

x1 = x0 + h
y0 = f(x0)
y1 = f(x1)

secant_slope = (y1 - y0) / (x1 - x0)
tangent_slope = df(x0)

x = np.linspace(-1, 4, 300)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='f(x) = x³ - 3x² + 2', color='black')

secant_y = secant_slope * (x - x0) + y0
ax.plot(x, secant_y, '--', color='blue', label=f'Secant (slope = {secant_slope:.2f})')

tangent_y = tangent_slope * (x - x0) + y0
ax.plot(x, tangent_y, '--', color='orange', label=f'Tangent (slope = {tangent_slope:.2f})')

ax.scatter([x0, x1], [y0, y1], color='red', zorder=5)

ax.text(0.05, 0.95, f'Secant slope = {secant_slope:.2f}\nTangent slope = {tangent_slope:.2f}',
        transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Secant vs Tangent (with slopes)')
ax.legend()
ax.grid(True)

st.pyplot(fig)

    
