from pyecharts import Liquid, Polar, Radar, Scatter

liquid =Liquid("水球图")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render(path='./data/03-01水球.html')

# 圆形水球
liquid2 =Liquid("水球图示例")
liquid2.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid2.show_config()
liquid2.render(path='./data/03-02圆形水球.html')

# 菱形水球
liquid3 =Liquid("水球图示例")
liquid3.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid3.show_config()
liquid3.render(path='./data/03-03菱形水球.html')

# 极坐标
radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
polar.show_config()
polar.render(path='./data/03-04极坐标.html')

# 雷达图
schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
radar =Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
radar.show_config()
radar.render(path='./data/03-05雷达图.html')

# 散点图
v1 =[10, 20, 30, 40, 50, 60]
v2 =[10, 20, 30, 40, 50, 60]
scatter =Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
scatter.show_config()
scatter.render(path='./data/03-06散点图.html')

# 散点打印Pyecharts字体 白底图片
scatter =Scatter("散点图示例")
v1, v2 = scatter.draw("./data/one.jpg")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.show_config()
scatter.render(path='./data/03-06打印字体.html')