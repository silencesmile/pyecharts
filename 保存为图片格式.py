from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot

'''
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 pyecharts-snapshot

pip install pyecharts
保存为图片格式的插件

安装 phantomjs
npm install -g phantomjs-prebuilt

安装 pyecharts-snapshot
pip3 install pyecharts-snapshot
pip3 install pyecharts-snapshot==0.1.7


引入 pyecharts-snapshot
from pyecharts_snapshot.main import make_a_snapshot

调用方法
make_a_snapshot('render.html', 'snapshot.png')

'''

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options()
bar.render(path='snapshot.html')
bar.render(path='snapshot.png')
bar.render(path='snapshot.pdf')

# 编辑图片时会报错
# make_a_snapshot("snapshot.html", "snapshot.png" )