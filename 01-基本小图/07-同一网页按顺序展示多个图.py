from pyecharts import Page
'''
同一网页按顺序展示多个图：page
pyecharts.Page 可以实现多图展示
from pyecharts import Page
'''

from pyecharts import Bar, Scatter3D
from pyecharts import Page

page = Page()  # step 1

# bar
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
page.add(bar)  # step 2

# scatter3D
import random

data = [
    [random.randint(0, 100),
     random.randint(0, 100),
     random.randint(0, 100)] for _ in range(80)
]
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
page.add(scatter3D)  # step 2

# page.render()  # step 3

page.render(path="./data/07-07按顺序展示多个图.html")
