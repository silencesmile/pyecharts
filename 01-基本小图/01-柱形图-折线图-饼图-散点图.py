from pyecharts import Line, Bar, Pie, EffectScatter
'''
http://pyecharts.org/#/zh-cn/prepare  官方中文文档

'''

attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]

# 柱形图
bar = Bar('柱形图', '库存量')
bar.add('服装', attr, v1,  is_label_show=True)
bar.show_config()
bar.render(path='./data/01-01柱形图.html')

bar2 = Bar("显示标记线和标记点")
bar2.add('商家A', attr, v1, mark_point=['avgrage'])
bar2.add('商家B', attr, v2, mark_point=['min', 'max'])
bar2.show_config()
bar2.render(path='./data/01-02标记点柱形图.html')

bar3 = Bar("水平显示")
bar3.add('商家A', attr, v1)
bar3.add('商家B', attr, v2, is_convert=True)
bar3.show_config()
bar3.render(path='./data/01-03水平柱形图.html')

# 折线图
# 折线图
line = Line('折线图')
line.add('商家A', attr, v1, mark_point=['max'])
line.add('商家B', attr, v2, mark_point=['min'], is_smooth=True)
line.show_config()
line.render(path='./data/01-04折线图.html')

# 阶梯折线图
line2 = Line('阶梯折线图')
line2.add('商家A', attr, v1,  is_step=True, is_label_show=True)
line2.show_config()
line2.render(path='./data/01-05阶梯折线图.html')

# 面积折线图
line3 =Line("面积折线图")
line3.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None, mark_point=['max'])
line3.add("商家B", attr, v2, is_fill=True, area_color='#a3aed5', area_opacity=0.3, is_smooth=True)
line3.show_config()
line3.render(path='./data/01-06面积折线图.html')

# 柱形图-折线图
from pyecharts import Bar, Line, Overlap

att = ['A', 'B', 'C', 'D', 'E', 'F']
v3 = [10, 20, 30, 40, 50, 60]
v4 = [38, 28, 58, 48, 78, 68]

bar = Bar("柱形图-折线图")
bar.add('bar', att, v3)
line = Line()
line.add('line', att, v4)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.show_config()
overlap.render(path='./data/01-066柱形图-折线图.html')


# 饼图
pie = Pie('饼图')
pie.add('芝麻饼', attr, v1, is_label_show=True)
pie.show_config()
pie.render(path='./data/01-07饼图.html')

# 玫瑰饼图
pie2 = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie2.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
pie2.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
pie2.show_config()
pie2.render(path='./data/01-08玫瑰饼图.html')

# 动态散点图
es =EffectScatter("动态散点图")

# v1 x坐标 v2 y坐标
es.add("商家", v1, v2)
es.show_config()
es.render('./data/01-09散点图.html')

# 动态散点图各种图形
es = EffectScatter("动态散点图各种图形")
es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.show_config()
es.render(path = "./data/01-10动态散点图各种图形.html")