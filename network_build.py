import pandas as pd
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False
# ============================================================
# 1. 读取论文数据（格式：title, year, keywords）
# ============================================================
df = pd.read_csv("paper.csv")  # 请替换为你的文件路径

# 将关键词字符串转成列表
df["keywords"] = df["keywords"].apply(
    lambda x: [k.strip() for k in x.replace(",", ";").split(";") if k.strip()]
)

# ============================================================
# 2. 构建关键词共现边（co-occurrence edges）
# ============================================================
G = nx.Graph()

for _, row in df.iterrows():
    year = row["year"]
    kws = row["keywords"]

    # 同一篇论文的所有关键词两两共现
    for kw1, kw2 in itertools.combinations(kws, 2):
        if G.has_edge(kw1, kw2):
            G[kw1][kw2]["weight"] += 1
        else:
            G.add_edge(kw1, kw2, weight=1)

    # 保存节点年份用于着色
    for kw in kws:
        if "years" not in G.nodes[kw]:
            G.nodes[kw]["years"] = []
        G.nodes[kw]["years"].append(year)

# ============================================================
# 3. 分配节点颜色（按时间平均值染色）
# ============================================================
all_years = sorted(df["year"].unique())
year_min, year_max = min(all_years), max(all_years)

def year_to_color(year):
    norm = (year - year_min) / (year_max - year_min)
    return cm.rainbow(norm)

node_colors = [
    year_to_color(np.mean(G.nodes[n]["years"]))
    for n in G.nodes
]

# ============================================================
# 4. 绘制共现网络
# ============================================================
plt.figure(figsize=(14, 12))

# 使用力导向布局
pos = nx.spring_layout(G, k=0.5, iterations=100)

# 绘制节点
nx.draw_networkx_nodes(
    G, pos,
    node_size=300,
    node_color=node_colors,
    alpha=0.9
)

# 绘制边
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]["weight"] * 0.3 for u, v in G.edges()],
    alpha=0.5
)

# 绘制标签
nx.draw_networkx_labels(G, pos, font_family="SimHei", font_size=10)

# 颜色条（对应年份）
sm = plt.cm.ScalarMappable(cmap=cm.rainbow,
                           norm=plt.Normalize(vmin=year_min, vmax=year_max))
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label("年份", fontsize=12)

plt.title("关键词共现网络（Python 实现类 CiteSpace 效果）", fontsize=16)
plt.axis("off")
plt.show()
