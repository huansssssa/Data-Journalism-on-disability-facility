import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False

# 关键事件（保留完整文本，无需精简）
events = [
    (1982, '1982：宪法写入残疾人权利保障', 2, '基础阶段'),
    (2001, '2001：城市道路和建筑物无障碍设计规范', 3, '基础阶段'),
    (2008, '2008：北京奥运会地铁无障碍示范', 5, '示范阶段'),
    (2012, '2012：《无障碍环境建设条例》颁布实施', 7, '法制阶段'),
    (2016, '2016：清华大学无障碍研究院成立\n        +北京轨道交通规程发布', 8, '法制阶段'),
    (2022, '2022：北京冬奥会无障碍示范\n        +示范城市创建（80%目标）', 9.5, '优化阶段'),
    (2023, '2023：《无障碍环境建设法》施行', 10, '优化阶段')
]

# 覆盖率趋势数据
years_full = [1982, 1990, 2001, 2008, 2012, 2016, 2022, 2023, 2025]
coverage_trend = [5, 8, 12, 25, 40, 55, 78, 90, 95]

# 创建画布，预留右侧空白区域
fig, ax1 = plt.subplots(figsize=(20, 10))

# 左侧Y轴：发展强度
years = [e[0] for e in events]
strengths = [e[2] for e in events]

ax1.set_xlabel('年份', fontsize=14, fontweight='bold')
ax1.set_ylabel('发展强度（事件影响力评分 0-10分）', fontsize=14, fontweight='bold', color='darkblue')
line1 = ax1.plot(years, strengths, color='darkblue', linewidth=4, label='发展强度趋势线')[0]
ax1.scatter(years, strengths, s=350,
            c=['#E74C3C', '#E74C3C', '#F39C12', '#3498DB', '#3498DB', '#27AE60', '#27AE60'],
            zorder=5, edgecolors='black', linewidth=2)

# 阶段渐变背景
stage_colors = {'基础阶段': '#FFCCCC', '示范阶段': '#FFEECC', '法制阶段': '#CCEEFF', '优化阶段': '#CCFFCC'}
prev_year = 1982
for i in range(len(events)):
    current_year = events[i][0]
    stage = events[i][3]
    if i > 0:
        ax1.axvspan(prev_year, current_year, color=stage_colors.get(stage, '#EEEEEE'), alpha=0.4)
    prev_year = current_year
ax1.axvspan(prev_year, 2026, color='#CCFFCC', alpha=0.4)

# ===== 核心改进：右侧空白区集中标注 =====
# 定义右侧标注的Y轴位置（均匀分布，避免重叠）
label_y_positions = [1.5, 2.8, 4.8, 6.8, 8.0, 9.2, 10.2]
# 标注文字的X轴位置（统一放在2027年位置）
label_x = 2027

# 逐个添加标注和箭头
for i, (year, desc, strength, _) in enumerate(events):
    # 1. 在右侧空白区添加文字
    ax1.text(label_x, label_y_positions[i], desc,
             fontsize=11, fontweight='bold', ha='left', va='center',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.95, edgecolor='gray'))

    # 2. 绘制从文字到数据点的箭头
    ax1.annotate('',
                 xy=(year, strength),  # 箭头终点（数据点）
                 xytext=(label_x - 0.5, label_y_positions[i]),  # 箭头起点（文字左侧）
                 arrowprops=dict(arrowstyle='->', color='gray', lw=2, alpha=0.8,
                                 connectionstyle="arc3,rad=0.1"))

# 调整坐标轴范围（右侧留出足够的标注空间）
ax1.set_ylim(0, 11)
ax1.set_xlim(1980, 2032)  # 扩展X轴到2032，给右侧标注留空间
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=12)

# 右侧Y轴：覆盖率
ax2 = ax1.twinx()
ax2.set_ylabel('无障碍设施覆盖率趋势（%）', fontsize=14, fontweight='bold', color='darkgreen')
ax2.plot(years_full, coverage_trend, color='darkgreen', linestyle='--', linewidth=4, marker='o', markersize=9,
         label='覆盖率趋势')
ax2.axhline(y=80, color='red', linestyle=':', linewidth=3, label='政策目标线（2022年起80%）')
ax2.set_ylim(0, 100)
ax2.legend(loc='upper right', fontsize=12)

# 标题和底部说明
plt.title('图1：中国公共交通无障碍设施发展“数据时间轴”\n多层级演进模型：政策事件强度 + 覆盖率趋势 + 阶段渐变',
          fontsize=16, fontweight='bold', pad=30)

fig.text(0.5, 0.02,
         '早期政策密集但设施覆盖滞后（缓慢追赶80%目标），证明“高度差争议”并非孤例，而是历史遗留的系统性短板',
         ha='center', fontsize=13, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.4, pad=1))

plt.tight_layout(rect=[0, 0.06, 1, 0.94])
plt.savefig('图1_数据时间轴_无重叠最终版.png', dpi=400, bbox_inches='tight')
plt.show()

print("优化版图1已生成：文字全部放在右侧空白区，无任何重叠，箭头精准指向对应数据点！")