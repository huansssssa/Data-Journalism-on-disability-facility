import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ======== 数据 ========
categories = ['盲道', '楼梯和台阶', '升降平台', '轮椅坡道', '无障碍通道', '文字信息辅助服务']
values = [66, 73, 73, 73, 72, 72]           # 满意度（%）
problems = ['占用、损坏严重\n改进需求17%', '天桥过街困难\n改进需求17%', '接入困难\n改进需求14%',
            '安全隐患', '使用不便', '覆盖不足']
colors = ['#C0392B', '#E74C3C', '#E67E22', '#F39C12', '#16A085', '#27AE60']

# ======== 雷达图基础设置 ========
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
values_closed = values + values[:1]      # 闭合
angles_closed = angles + angles[:1]

fig = plt.figure(figsize=(11, 11))
ax = fig.add_subplot(111, polar=True)

# 绘制渐变填充区域（逐个扇区）
for i in range(len(categories)):
    ax.fill([angles[i], angles[i], angles_closed[i+1], angles_closed[i+1]],
            [0, values[i], values_closed[i+1], 0],
            color=colors[i], alpha=0.3)
    # 半透明渐变扇区
    ax.plot([angles[i], angles[i]], [0, values[i]], color=colors[i], linewidth=5)

# 绘制外轮廓线
ax.plot(angles_closed, values_closed, color='#2C3E50', linewidth=6, label='满意度轮廓')

# ======== 美化 ========
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=12, color='gray')
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=18, fontweight='bold', color='#2C3E50')
ax.grid(color='gray', linestyle='-', alpha=0.3)
ax.set_theta_direction(-1)      # 顺时针
ax.set_theta_offset(np.pi/2)    # 12点钟方向开始

# ======== 核心：警示气泡 + 问题文字 ========
for angle, val, problem, col in zip(angles, values, problems, colors):
    # 圆形气泡显示百分比
    ax.text(angle, val + 8, f'{val}%', ha='center', va='center',
            fontsize=20, fontweight='bold', color='white',
            bbox=dict(boxstyle='circle,pad=0.8', facecolor=col, edgecolor='white', linewidth=3))
    # 问题文字向外延伸
    ax.text(angle, val + 22, problem, ha='center', va='center',
            fontsize=11, fontweight='bold', color=col,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9))

# ======== 标题与结论 ========
plt.title('广州2022年公共场所无障碍设施满意度雷达警示图',
          fontsize=20, fontweight='bold', pad=60, color='#2C3E50', loc='center')

fig.text(0.5, 0.06,
         '盲道、台阶、升降平台满意度低于75%，为当前最突出痛点，',
         ha='center', fontsize=15, fontweight='bold',
         bbox=dict(facecolor='#FFF3CD', edgecolor='#F39C12', boxstyle='round,pad=1'))

plt.tight_layout()
plt.savefig('广州无障碍设施满意度_雷达美图_完美版.png', dpi=500, bbox_inches='tight', facecolor='#f8f9fa')
plt.show()