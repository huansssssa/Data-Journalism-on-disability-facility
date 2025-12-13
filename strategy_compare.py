import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import table

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 表1完整数据（按国家分组，年份排序）
data_china = [
    ("1982", "《宪法》导入“国家和社会帮助安排权”等"),
    ("1989", "《方便残疾人使用的城市道路和建筑物设计规范（试行）》"),
    ("1990", "《残疾人保障法》"),
    ("1994", "《残疾人教育条例》"),
    ("2000", "《民用机场疏散站区无障碍设施设备配置标准》"),
    ("2001", "修订为《城市道路和建筑物无障碍设计规范》"),
    ("2003", "《上海无障碍设施设计标准》"),
    ("2005", "《铁路旅客车站无障碍设计规范》"),
    ("2008", "修订《残疾人保障法》提出“推进信息交流无障碍”"),
    ("2009", "实施《标志用公共信息图形符号标准第9部分:无障碍设施符号》"),
    ("2012", "发布新版《无障碍设计规范》"),
    ("2016", "制定《中国残疾人事业“十三五”发展纲要》"),
    ("2017", "修订《残疾人教育条例》")
]

data_canada = [
    ("1944", "安大略省政府引入《残障人士歧视法》"),
    ("1977", "出台《加拿大人权法案》"),
    ("1982", "《加拿大人权宪章》"),
    ("1986", "出台《平等就业法》"),
    ("1996", "修正《加拿大人权法案》"),
    ("2004", "《多伦多无障碍设计指南》"),
    ("2005", "《安大略省残疾人无障碍法》"),
    ("2010", "《加拿大国家建筑规范》第3.6节为无障碍设计"),
    ("2012", "《无障碍设计指南》为《加拿大国家建筑规范》第3.8节的补充"),
    ("2014", "《残疾人税收抵免促进指南制法》"),
    ("2019", "《加拿大无障碍法案》")
]

data_ireland = [
    ("1952", "《社会福利法》"),
    ("1953", "《健康法》"),
    ("1981", "《社会福利(整合)法》"),
    ("1993", "《社会福利(残疾津贴)条例》"),
    ("1997", "《建筑法规》M部分规定建筑物为残障人士提供便利"),
    ("1998", "《教育法》提出为每个人提供受教育的机会 《就业平等法》"),
    ("2000", "《平等地位法》以促进平等,禁止歧视"),
    ("2003", "《社会福利(残疾津贴)条例》"),
    ("2004", "颁布《特殊教育需要者教育法》"),
    ("2005", "《残疾人》为公共服务的可及性提供了法律基础"),
    ("2007", "《建筑控制法》规定了残障人士出入权限"),
    ("2010", "修订《建筑法规》M部分,扩大适用建筑范围"),
    ("2012", "《为所有人打造:通用设计方法》"),
    ("2014", "《爱尔兰人权与平等委员会法》"),
    ("2015", "《爱尔兰房屋通用设计准则》")
]

fig, ax = plt.subplots(figsize=(18, 14))
ax.axis('off')

# 标题
ax.text(0.5, 0.98, '表1可视化：中加爱三国无障碍法规发展对比表\n（彩色分层 + 年份热力渐变 + 完整事件，信息丰富且直观）',
        ha='center', va='center', fontsize=18, fontweight='bold')

# 表格数据组合（国家 | 年份 | 事件）
table_data = []
row_colors = []

# 中国（红色系）
for year, event in data_china:
    table_data.append(['中国', year, event])
    row_colors.append('#FFCCCC')

# 加拿大（蓝色系）
for year, event in data_canada:
    table_data.append(['加拿大', year, event])
    row_colors.append('#CCEEFF')

# 爱尔兰（绿色系）
for year, event in data_ireland:
    table_data.append(['爱尔兰', year, event])
    row_colors.append('#CCFFCC')

# 绘制表格
tbl = ax.table(cellText=table_data, colLabels=['国家', '年份', '法规事件'],
               cellLoc='left', loc='center', colWidths=[0.1, 0.1, 0.8])

tbl.auto_set_font_size(False)
tbl.set_fontsize(10)

# 表头样式
for i in range(3):
    tbl[(0, i)].set_facecolor('#4A4A4A')
    tbl[(0, i)].set_text_props(weight='bold', color='white')

# 行颜色 + 年份热力渐变（年份越新越深）
for i in range(len(table_data)):
    for j in range(3):
        cell = tbl[(i+1, j)]
        cell.set_facecolor(row_colors[i])
        if j == 1:  # 年份列热力渐变
            year = int(table_data[i][1])
            intensity = (year - 1940) / (2020 - 1940)
            base_color = row_colors[i][:7]  # 取基础色
            cell.set_facecolor(base_color.replace('#', '#') + f'{int(255*(1-intensity)):02X}')

tbl.scale(1, 2.5)  # 行高放大，便于阅读长事件

# 底部说明
fig.text(0.5, 0.02, '中国事件密集（13项）、加拿大权益导向（11项）、爱尔兰通用设计领先（15项），中国可借鉴加爱精细化标准',
         ha='center', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.3))

plt.tight_layout()
plt.savefig('表1_法规发展创新表格.png', dpi=400, bbox_inches='tight')
plt.show()

print("创新彩色表格已生成：信息完整、视觉分层、年份热力渐变！")