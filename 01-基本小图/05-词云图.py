from pyecharts import WordCloud


name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud =WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render(path='./data/05-01权重词云.html')


wordcloud2 =WordCloud(width=1300, height=620)
wordcloud2.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud2.show_config()
wordcloud2.render(path='./data/05-02变形词云.html')


# 中文显示
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


words = ['好看', '不错', '人性', '可以', '值得', '真的', '一部', '感觉', '喜欢', '一般', '演技', '还是',
       '剧情', '一出', '有点', '出好', '好戏', '不是', '没有', '非常', '哈哈', '喜剧', '就是', '一个',
       '现实', '什么', '支持', '还行', '但是', '很多', '觉得', '搞笑', '值得一看', '故事', '看好',
       '这部', '哈哈哈', '失望', '最后', '导演', '自己', '演员', '看完', '社会', '特别', '看到', '不好',
       '比较', '表达', '那么', '作品', '个人', '东西', '思考', '这个', '第一', '不过', '情节',
       '哈哈哈哈', '意思', '一直', '推荐', '一般般', '时候', '开始', '般般', '片子', '知道', '处女',
       '期待', '很棒', '影院', '深度', '反应', '无聊', '可能', '一些', '精彩', '爱情', '这么', '希望',
       '一点', '不知', '有些', '还好', '恐怖', '看着', '没看', '还有', '观看', '后面', '真实', '因为',
       '如果', '出来', '部分', '确实', '我们', '意义', '深刻']


new_worlds = " ".join(words)

coloring = np.array(Image.open("./data/huangbo.jpg"))

# simkai.ttf 必填项 识别中文的字体，例：simkai.ttf，
my_wordcloud = WordCloud(background_color="white", max_words=800,
                         mask=coloring, max_font_size=120, random_state=30, scale=2,font_path="./data/simkai.ttf").generate(new_worlds)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片
my_wordcloud.to_file('./data/05-03signature.png')