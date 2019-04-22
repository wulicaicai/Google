# 谷歌翻译
# 导入类库
from googletrans import Translator
# 创建实例化对象
translator = Translator(service_urls=['translate.google.cn'])
# 客户端输入
while True:
    source=input('请输入其他国家语言:')
    # source = "King Athamus of northern Greece had two children， Phrixus and Helle．After he left his first wife and mar ried Ino，a wicked woman，the two children received all the cruel treatment that a stepmother coulddevise ，At one timethe kingdom was ruined by a famine．"
    # 判断客户输入的是什么语言
    judge = translator.detect(source).lang


    # 取出翻译后的内容 src 表示客户输入的哪国语言 dest是翻译成哪国的语言
    text = translator.translate(source,src=judge,dest='zh-cn').text

    # text = translator.translate(source,src='zh-cn',dest='en').text
    print(text)
