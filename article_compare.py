import matplotlib.pyplot as plt

# ===============================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False
# ===============================
years = list(range(2012, 2025))

china = [8, 12, 11, 9, 4, 8, 7, 8, 7, 10, 22, 19, 8]
japan = [12, 18, 13, 16, 23, 10, 9, 20, 35, 15, 22, 14, 3]

# ===============================
# 绘图
# ===============================
plt.figure(figsize=(10, 10))

# --- 第一幅图：中国文献数量 ---
plt.subplot(2, 1, 1)
plt.plot(years, china, marker='o', linewidth=2, color='orange')
plt.title("中国文献数量", fontsize=14)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)

# --- 第二幅图：日本文献数量 ---
plt.subplot(2, 1, 2)
plt.plot(years, japan, marker='o', linewidth=2, color='orange')
plt.title("日本文献数量", fontsize=14)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
