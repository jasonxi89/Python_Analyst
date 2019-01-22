#分析习大大的新年贺词
#Analyst Chair Xi's 2019 new year greetings
#Using Jieba to cut words. Using wordcloud to make analyst
#The greetings url:http://www.xinhuanet.com/politics/2018-12/31/c_1123931806.htm
import jieba
import jieba.analyse
import requests
from bs4 import BeautifulSoup
import tools as t
import re
from PIL import Image
import config as c
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
import matplotlib.pyplot as plt
from scipy.misc import imread

myurl = "http://www.xinhuanet.com/politics/2018-12/31/c_1123931806.htm"
#re to ignore all the punctuations
punctuation_pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
#output the words to txt file
words_file = "words.txt"

#get the article
def get_article(url):
    re = ""
    resp = requests.get(url).content
    if resp is not None:
        soup = BeautifulSoup(resp,"lxml")
        ps = soup.select('p')
        for p in ps[:-1]:
            print(p.text)
            re += p.text
    return re
#generate words cloud
def generate_wc(content):
    #font path for MAC only
    font_path = "/System/Library/fonts/PingFang.ttc"
    wc = WordCloud(font_path=font_path, background_color="black", margin=5, width=500, max_words=50, max_font_size=400)
    wc = wc.generate(content)
    wc.to_file('result.png')



if __name__ == '__main__':
    result = punctuation_pattern.sub("",get_article(myurl))
    words = [word for word in jieba.cut(result, cut_all=False) if len(word) >= 2]
    #data cleaning with unmeaning words
    exclude_words = ["一年", "一位", "他们", "新华社", "前夕", "主席", "习近平", "中央", "广播电视", "总台", "长江", "不会",
                     "正在", "这些", "新年贺词", "看到", "隆重庆祝", "多万", "发表"]

    for num in range(len(words)-1,-1,-1):
        if words[num] in exclude_words:
            print("移除非关键字"+words[num])
            del words[num]

    c = Counter(words)
    for word_freq in c.most_common(50):
        word,freq = word_freq
        print(word, freq)
    data = r' '.join(words)
    generate_wc(data)

    image = Image.open("result.png")
    image.show()


