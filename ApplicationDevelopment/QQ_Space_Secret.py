#（1）导入time,selenium,lxml模块。输入QQ账号，密码，以及要爬取的好友QQ账号
import time
from selenium import webdriver
from lxml import etree
friend = '771626423'
user = '2963192844'
pw = 'zwt13966603401'

#（2）调用浏览器，实现自动登入和访问好友空间
driver = webdriver.Firefox() #打开浏览器
driver.maximize_window() #浏览器窗口最大化
driver.get("http://i.qq.com") #浏览器定向为登入界面
driver.switch_to.frame("login_frame") #这里需要选中一下frame，否则找不到下面需要的网页元素
driver.find_element("switcher_plogin").click() #自动单机账号登入方式
driver.find_element("u").send_keys(user) #在账号框输入已知账号
driver.find_element("p").send_keys(pw) #在密码框输入已知密码
driver.find_element("login_button").click() #自动单击登入按钮
driver.switch_to.default_content() #让webdriver操纵当前页
driver.get("http://user.qzone.qq.com/"+"xxx"+"/311")
#(3)利用while循环实现所有页面的获取，跳出循环条件直到最后一页。利用自动化循环程序实现自动下拉滚动条，让浏览器加载内容，通过网页标签匹配目标信息
#并保存到自定义的txt文件。
next_num = 0 #初始”下一页“的id
while True:
    #下拉滚动条，使浏览器加载内容
    #从1开始，到6借宿，分5次加载完每页数据
    for i in range(1,6):
        heigth = 2000 * 1 #每次滑动20000像素
        strWord = "window.scrollBy(0,"+str(heigth)+")"
        driver.execute_script(strWord)
        time.sleep(4)

    #网页由多个<frame>或<iframe>组成，webdriver默认的是最外层的frame
    #所以这里需要选中一下说说所在的frame,否则找不到下面需要的网页元素
    driver.switch_to.frame("app_canvas_frame")
    selector = etree.HTML(driver.page_source)
    divs = selector.xpath('//*[@id="msgList"]/li/div[3]')

    #这里使用a表示内容可以连续写入
    with open('qq_word.txt','a') as f:
        for div in divs:
            qq_name = div.xpath('./div[2]/a/text()')
            qq_time = div.xpath('./div[4]/div[1]/span/a/text()')
            qq_content = div.xpath('./div[2]/pre/text()')
            qq_name = qq_name[0] if len(qq_name) > 0 else ''
            qq_content = qq_content[0] if len(qq_content) > 0 else ''
            qq_time = qq_time[0] if len(qq_name) > 0 else ''
            print(qq_name,qq_time,qq_content)
            f.write(qq_content+"\n")

#(4)说说加载到尾页就停止，否则就要单机”下一页“按钮，并将再下一页的id进行记录，然后跳转到外层标签，进行下一次的循环读取说说。
    #当已经到了尾页， ”下一页“这个按钮就没有id了，可以结束了
    if driver.page_source.find('page_next_' + str(next_num)) == -1:
        break
    # 找到”下一页“按钮， 需要动态记录一下
    driver.find_element('page_next_' + str(next_num)).click()
    #"下一页"的id
    next_num += 1
    #因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
    driver.switch_to.parent_frame()

#(5)导入相关模块，生成词云。创建词云函数，并设置各项参数。利用Matplotlib库将词云可视化
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
#生成词云
def create_word_cloud(filename):
    text = open("qq_word.txt".format(filename)).read()
    #结巴分词
    wordlist = jieba.cut(text, cut_all=True)
    wl = " ".join(wordlist)
    #设置词云
    wc = WordCloud(
        #设置背景颜色
        background_color="white",
        #设置最大显示的词云数
        max_words=2000,
        #一般路径
        font_path="simfang.ttf",
        height=1200,
        width=1600,
        #设置字体最大值
        max_font_size=100,
        #设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )

    myword = wc.generate(wl) #生成词云
    #展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('py_book.png')

if __name__ == '__main__':
    create_word_cloud('word_py')