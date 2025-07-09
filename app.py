import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# macOS font setting (optional)
plt.rcParams['font.family'] = 'PingFang TC'
plt.rcParams['axes.unicode_minus'] = False

def f(x):
    return x**3 - 3*x**2 + 2

def df(x):
    return 3*x**2 - 6*x

st.title("Secant vs Tangent (with Δx and Δy)")

x0 = st.slider("x₀", min_value=-0.5, max_value=3.5, value=2.0, step=0.1)
h = st.slider("h", min_value=0.01, max_value=2.0, value=1.0, step=0.05)

x1 = x0 + h
y0 = f(x0)
y1 = f(x1)

delta_x = x1 - x0
delta_y = y1 - y0

secant_slope = delta_y / delta_x
tangent_slope = df(x0)

x = np.linspace(-1, 4, 300)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='f(x) = x³ - 3x² + 2', color='black')

# Secant line
secant_y = secant_slope * (x - x0) + y0
ax.plot(x, secant_y, '--', color='blue', label=f'Secant (slope = {secant_slope:.2f})')

# Tangent line
tangent_y = tangent_slope * (x - x0) + y0
ax.plot(x, tangent_y, '--', color='orange', label=f'Tangent (slope = {tangent_slope:.2f})')

# Points
ax.scatter([x0, x1], [y0, y1], color='red', zorder=5)

# Vertical and horizontal helper lines
ax.vlines([x0, x1], 0, [y0, y1], linestyles='dotted', colors='gray')
ax.hlines([y0, y1], -1, [x0, x1], linestyles='dotted', colors='gray')

# Add Δx arrow
ax.annotate(
    "", xy=(x1, y0), xytext=(x0, y0),
    arrowprops=dict(arrowstyle='<->', color='green', linewidth=2)
)
ax.text((x0 + x1) / 2, y0 - 5, f"Δx = {delta_x:.2f}", ha='center', va='top', fontsize=12, color='green')

# Add Δy arrow
ax.annotate(
    "", xy=(x1, y1), xytext=(x1, y0),
    arrowprops=dict(arrowstyle='<->', color='purple', linewidth=2)
)
ax.text(x1 + 0.1, (y0 + y1) / 2, f"Δy = {delta_y:.2f}", va='center', fontsize=12, color='purple')

# Text annotation for slopes
ax.text(0.05, 0.95, f'Secant slope = {secant_slope:.2f}\nTangent slope = {tangent_slope:.2f}',
        transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Secant vs Tangent (with Δx and Δy)')
ax.legend()
ax.grid(True)

st.pyplot(fig)
