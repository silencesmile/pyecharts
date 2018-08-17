from pyecharts import Funnel, Gauge, Graph

attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 56, 78, 100]
v2 =[55, 60, 16, 20, 15, 80]

# 漏斗图
funnel = Funnel('漏斗图')
funnel.add('商品', attr, v1, is_label_show=True, label_pos='inside', label_text_color="#fff")
funnel.show_config()
funnel.render(path="./data/02-01漏斗图.html")

# 仪表盘
gauge = Gauge("仪表盘")
gauge.add('业务指标', '完成率', 66.66)
gauge.show_config()
gauge.render(path="./data/02-02仪表盘.html")

# 关系图
nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30}, {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 50}, {"name": "结点6", "symbolSize": 40}, {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
links =[]
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})

print(links)
print(nodes)
graph =Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
graph.show_config()
graph.render(path="./data/02-03关系图.html")