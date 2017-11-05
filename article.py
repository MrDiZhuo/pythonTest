import hashlib
import time
import os
from lxml import etree
import requests

PC_TIME = time.strftime('%Y-%m-%d',time.localtime(time.time()))
PC_SECOND = time.strftime('%H-%M-%S',time.localtime(time.time()))
PC_WEEK = time.strftime("%w",time.localtime(time.time()))
print(PC_TIME+"----"+PC_WEEK)

'''文本内容'''
TXT_ARTICLE = open(PC_TIME+"_"+PC_SECOND+".txt", "w+", encoding='utf-8')
'''记录url（每个报纸不一样）'''
TXT_URL_themetimes = open("url_themetimes.txt", "a+", encoding='utf-8')
TXT_URL_skysport = open("url_skysport.txt", "a+", encoding='utf-8')
TXT_URL_thesun = open("url_thesun.txt", "a+", encoding='utf-8')
TXT_URL_dailymail = open("url_dailmail.txt", "a+", encoding='utf-8')
TXT_URL_mirror = open("url_mirror.txt", "a+", encoding='utf-8')
TXT_URL_independent = open("url_independent.txt", "a+", encoding='utf-8')
TXT_URL_telegraph = open("url_telegraph.txt", "a+", encoding='utf-8')
TXT_URL_liverpool_manchester = open("url_liverpool_manchester.txt", "a+", encoding='utf-8')
TXT_URL_standard = open("url_standard.txt", "a+", encoding='utf-8')
TXT_URL_reuters = open("url_reuters.txt", "a+", encoding='utf-8')
TXT_URL_worldsoccertalk = open("url_worldsoccertalk.txt", "a+", encoding='utf-8')
TXT_URL_bbc = open("url_bbc.txt", "a+", encoding='utf-8')
TXT_URL_football365 = open("url_football365.txt", "a+", encoding='utf-8')
TXT_URL_guardian = open("url_guardian.txt", "a+", encoding='utf-8')
'''文件夹图片'''
PACKAGE_PHOTO = PC_TIME+"_photo"

'''url——txt读写的集合'''
set_in = set()
set_out = set()

'''报纸url'''
URL_themetimes = 'https://www.thetimes.co.uk'
URL_themetimes_login = r'https://login.thetimes.co.uk/'
URL_skysports_features= "http://www.skysports.com/football/features"
URL_skysports_pundits = "http://www.skysports.com/football/pundits"
URL_thesun_football = "https://www.thesun.co.uk/sport/football/"
URL_theSun_premierleague = "https://www.thesun.co.uk/sport/football/premierleague/"
URL_theSun_premierleague02 = "https://www.thesun.co.uk/sport/football/premierleague/page/2/"
URL_theSun_premierleague03 = "https://www.thesun.co.uk/sport/football/premierleague/page/3/"
URL_dailymail = "http://www.dailymail.co.uk/sport/football/index.html"
URL_mirror = "http://www.mirror.co.uk/sport/football/"
URL_independent = "http://www.independent.co.uk/sport/football"
URL_independent_comment = "http://www.independent.co.uk/sport/football/news-and-comment"
URL_independent_premier = "http://www.independent.co.uk/sport/football/premier-league"
URL_independent_international = "http://www.independent.co.uk/sport/football/international"
URL_independent_european = "http://www.independent.co.uk/sport/football/european"
URL_independent_transfers = "http://www.independent.co.uk/sport/football/transfers"
URL_telegraph_football = "http://www.telegraph.co.uk/football/"
URL_telegraph_premier = "http://www.telegraph.co.uk/premier-league/"
URL_liverpool = "http://www.liverpoolecho.co.uk/all-about/liverpool-fc?all=true"
URL_manchester_united = "http://www.manchestereveningnews.co.uk/all-about/manchester-united-fc?all=true"
URL_manchester_city = "http://www.manchestereveningnews.co.uk/all-about/manchester-city-fc?all=true"
URL_standard = 'https://www.standard.co.uk/sport/football'
URL_reuters = "https://in.reuters.com/news/archive/soccer"
URL_reuters_2 = "https://in.reuters.com/news/archive/soccer?view=page&page=2&pageSize=10"
URL_reuters_3 = "https://in.reuters.com/news/archive/soccer?view=page&page=3&pageSize=10"
URL_worldsoccertalk = 'http://worldsoccertalk.com/category/afp/'
URL_worldsoccertalk_2 = 'http://worldsoccertalk.com/category/afp/page/2/'
URL_worldsoccertalk_3 = 'http://worldsoccertalk.com/category/afp/page/3/'
URL_bbc = "http://www.bbc.com/sport/football"
URL_football365 = "http://www.football365.com/"
URL_football365_2 = "http://www.football365.com/top-story/page/2"
URL_football365_3 = "http://www.football365.com/top-story/page/3"
URL_guardian = "https://www.theguardian.com/football/all"
URL_guardian_2 = "https://www.theguardian.com/football?page=2"

'''泰晤士报纸用户名密码登录'''
values_themetimes = {'gotoUrl': 'https%3A%2F%2Fwww.thetimes.co.uk%2F', 's': '1', 'username': 'loujian@gmail.com', 'password': '13801252354'
    , 'rememberMe': 'on', 'Submit': 'Login'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}


'''url的md5加密和查重复'''
def md5(url,filename,file):
    m = hashlib.md5()
    m.update(url.encode('utf-8'))
    url_md5 = m.hexdigest()
    for line in open(filename, "r"):
        set_out.add(line.replace("\n", ""))
    if (url_md5 in set_out):
        bool = False
    else:
        file.write(url_md5 + "\n")
        bool = True
    return bool

'''打开路径'''
def getSimpleRoot(url):
    html = requests.get(url, headers=headers).content
    root = etree.HTML(html.decode('utf-8', 'ignore'))
    return root

def getRoot(url,s):
    html = s.get(url,headers = headers).content
    root = etree.HTML(html.decode('utf-8','ignore'))
    return root
'''保存图片'''
def savePhoto(url,name):
    if not os.path.exists(PACKAGE_PHOTO):
        os.makedirs(PACKAGE_PHOTO)
    # 循环把图片下载到本地photo路径下
    filename = PC_TIME+"_photo\\" + name + '.jpg'
    try:
        req = requests.get(url).content
        with open(filename, 'wb') as f:
            f.write(req)
    except Exception:
        pass
    return

def ThemeTimes(url,flag,s_theme):
    if(url[:15] == "/edition/sport/"):
        url = "https://www.thetimes.co.uk/" + url
        if (md5(url, "url_themetimes.txt", TXT_URL_themetimes)):
            TXT_ARTICLE.write(
                "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
            root = getRoot(url,s_theme)
            article = root.xpath('//article[@id = "article-main"]')[0]
            title = article.xpath('//h1/text()')[0]
            time = article.xpath('//time/text()')[0]
            TXT_ARTICLE.write("标题：" + title + "\n" + "时间：" + time + "\n" )
            writer = article.xpath('//strong/text()')
            if(len(writer) > 0):
                TXT_ARTICLE.write("作者："+writer[0]+"\n")
            i = 0
            for src in article.xpath('//figure//img/@src'):
                savePhoto("https:" + src, "theme_" + str(flag) + "_" + str(i))
                i = i + 1
            TXT_ARTICLE.write("正文：\n")
            body_1 = article.xpath('//div[@class = "Article-content has-dropCap"]//p')
            for p in body_1:
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            body_2 = article.xpath('//div[@class = "Article-content "]//p')
            for p in body_2:
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            keyFacts = article.xpath('//div[@class="Article-keyFacts KeyFacts"]')
            if (len(keyFacts) > 0):
                TXT_ARTICLE.write("阵容：\n")
                for key in keyFacts:
                    TXT_ARTICLE.write(key.xpath('//h3[@class = "KeyFacts-title"]/text()')[0] + "\n")
                    for p in key.xpath('.//ul/li'):
                        TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
    return

def SkySport(url,flag):
    if(url[34:38] == "news"):
        if (md5(url, "url_skysport.txt", TXT_URL_skysport)):
            TXT_ARTICLE.write(
                "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
            root = getSimpleRoot(url)
            article = root.xpath('//div[@itemprop = "articleBody"]')[0]
            title = article.xpath('//h1[@class = "article__title"]/@data-short-title')[0]
            time = article.xpath('//p[@class = "article__header-date-time"]/text()')[0]
            TXT_ARTICLE.write("标题："+title+"\n"+"时间："+time+"\n")
            writer = article.xpath('//h3[@class = "article__writer-name"]')
            if(len(writer) > 0 ):
                TXT_ARTICLE.write("作者："+writer[0].xpath('string(.)')+"\n")
            TXT_ARTICLE.write("正文：\n")
            for p in article.xpath('//div[@class = "article__body article__body--lead"]//p'):
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            TXT_ARTICLE.write("表格：\n")
            table = article.xpath('//div[@class = "article__body article__body--lead"]//div[@class = "widge-table"]')
            for i in range(len(table)):
                print(table[i].xpath('.//h2/text()')[0])
                for th in table[i].xpath('.//thead//th/text()'):
                    print("                                                "+th)
                for tr in table[i].xpath('.//tbody//tr'):
                    print(tr.xpath('string(.)'))
            i = 0
            for src in article.xpath('//div[@class = "article__body article__body--lead"]//figure[@class = "widge-figure"]//img/@data-src'):
                savePhoto(src, "skyspot_" + str(flag) + "_" + str(i))
                i = i+1
    return

def TheSun_url(root , flag):
    for url in root.xpath(
            '//section[@class = "football football--landing theme-football"]//a[@class = "teaser-anchor"]/@href'):
        flag = flag + 1
        TheSun(url, flag)
    for url in root.xpath(
            '//section[@class = "football football--landing theme-football"]//a[@class = "rail__item-anchor"]/@href'):
        flag = flag + 1
        TheSun(url, flag)
    return

def TheSun(url,flag):
    if(url[25:30] == "sport"):
        if(md5(url,"url_thesun.txt",TXT_URL_thesun)):
            TXT_ARTICLE.write(
                "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
            root = getSimpleRoot(url)
            article = root.xpath('//section//article[@class = "article"]|//article[@class = "article article-full"]')[0]
            title = article.xpath('//h1[@class = "article__headline"]/text()')[0]
            subtitle = article.xpath('//div[@class = "article__subdeck theme__border-color"]')[0].xpath('string(.)')
            writer = article.xpath('//div[@class = "article__author"]')[0].xpath('string(.)')
            time_1 = article.xpath('//div[@class = "article__published"]')[0].xpath('string(.)')
            time_2 = article.xpath('//div[@class = "article__updated"]')[0].xpath('string(.)')
            TXT_ARTICLE.write("标题："+title+"\n"+"副标题："+subtitle+"作者："+writer+"\n"+"时间："+time_1+time_2+"\n")
            TXT_ARTICLE.write("正文：\n")
            for p in article.xpath('//div[@class = "article__content"]//p/text()'):
                TXT_ARTICLE.write(p + "\n")
            i = 0
            for src in article.xpath( '//figure//img/@src'):
                savePhoto(src, "thesun_" + str(flag) + "_" + str(i))
                i = i + 1
    return

def DailMail(url,flag):
    url = "http://www.dailymail.co.uk"+url
    if(md5(url,"url_dailmail.txt",TXT_URL_dailymail)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//div[@id = "js-article-text"]')[0]
        title = article.xpath('//h1/text()')
        if(len(title) > 0):
            TXT_ARTICLE.write("标题：" + title[0] +"\n")
        TXT_ARTICLE.write("副标题：\n")
        for subtitle in article.xpath('//ul[@class = "mol-bullets-with-font"]/li/strong/text()'):
            TXT_ARTICLE.write(subtitle+"\n")
        writer = article.xpath('//p[@class = "author-section byline-plain"]/a/text()')
        if(len(writer) > 0):
            TXT_ARTICLE.write("作者："+writer[0]+"\n")
        time = article.xpath('//p[@class = "byline-section"]')[0].xpath('string(.)').replace("\n"," ")
        TXT_ARTICLE.write("时间："+time+"\n正文：\n")
        for p in article.xpath('//p[@class = "mol-para-with-font"]'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
        #src = article.xpath('//div[@class = "image-wrap"]/img/@data-src')
        #if(len(src) > 0):
        #    print(src[0])
        #    savePhoto(src[0], "dailmail_" + str(flag))
    return

def Mirror(url,flag):
    if(url[24:29] == "sport"):
        if(md5(url,"url_mirror.txt",TXT_URL_mirror)):
            TXT_ARTICLE.write(
                "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
            root = getSimpleRoot(url)
            article = root.xpath('//main//article')[0]
            title = article.xpath('//h1/text()')[0]
            subTitle = article.xpath('//p/text()')[0]
            writer = article.xpath('//div[@class = "author"]')[0].xpath('string(.)')
            time = article.xpath('//ul[@class = "time-info"]')[0].xpath('string(.)')
            TXT_ARTICLE.write("标题："+title+"\n副标题："+subTitle+"\n作者："+writer+"\n时间："+time+"\n正文：\n")
            for p in article.xpath('//div[@class = "article-body"]//p'):
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            i = 0
            for src in article.xpath('//div[@class = "article-body"]//figure[@class = "in-article-image"]//img/@data-src'):
                savePhoto(src, "mirror_" + str(flag) + "_" + str(i))
                i = i + 1
    return

def independent(url , flag):
    if(url[:4] !="http"):
        url = "http://www.independent.co.uk/" + url
        if(md5(url,"url_independent.txt",TXT_URL_independent)):
            TXT_ARTICLE.write(
                "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
            root = getSimpleRoot(url)
            article = root.xpath('//div[@id = "content"]//article')[0]
            title = article.xpath('//h1[@itemprop = "headline"]/text()')[0]
            subTitle = article.xpath('//div[@class = "intro"]/p/text()')[0]
            writer = article.xpath('//li[@class = "author"]')[0].xpath('string(.)').replace(" ","")
            time = article.xpath('//time/text()')[0]
            TXT_ARTICLE.write("标题："+title+"\n副标题："+subTitle+"\n作者："+writer+"\n时间："+time+"\n正文：\n")
            i= 0
            figure = article.xpath('//itemprop[@class ="associatedMedia image"]//meta[@class = "url"]/@content')
            if(len(figure) > 0):
                savePhoto(figure[0], "independent_" + str(flag) + "_" + str(i))
                i = i + 1
            for p in article.xpath('//div[@class = "text-wrapper"]//p'):
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            for src in article.xpath('//div[@class = "image"]//img/@src'):
                savePhoto(src, "independent_" + str(flag) + "_" + str(i))
                i = i + 1
    return

def Telegraph_url(root,flag):
    for li in root.xpath('//section[@class = "p_hub__section_1 container"]//article[@class = "col col_1"]//li//h3/a/@href'):
        flag = flag + 1
        Telegraph(li,flag)
    for li in root.xpath('//section[@class = "p_hub__section_2 container"]//div[@class = "list-of-entities component version-6 list-of-entities--premium "]//li//h3/a/@href'):
        flag = flag +1
        Telegraph(li,flag)
    for li in root.xpath('//section[@class = "p_hub__section_2 container"]//div[@class = "splitter section"]//div[@class = "splitter__slot splitter__slot--2"]//ol//li//h3/a/@href'):
        flag = flag +1
        Telegraph(li,flag)
    return
def Telegraph(url , flag):
    url = "http://www.telegraph.co.uk"+url
    if(md5(url,"url_telegraph.txt",TXT_URL_telegraph)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article =root.xpath('//div[@class="main-content"]//main//div[@class="js-article-inner"]')[0]
        title = article.xpath('//h1[@itemprop="headline name"]/text()')[0]
        i = 0
        img = article.xpath('//figure[@class="lead-asset__figure"]//img/@src')
        if(len(img) > 0 ):
            src = img[0]
            if(img[0][:4] != "http"):
                src = "http://www.telegraph.co.uk"+src
                i = i + 1
            savePhoto(src, "telegraph_" + str(flag) + "_" + str(i))
        time = article.xpath('//time/text()')[0]
        TXT_ARTICLE.write("标题：" + title + "\n时间：" + time + "\n")
        for writer in article.xpath('//span[@class = "byline__author-name"]/a/text()'):
            TXT_ARTICLE.write("作者："+writer+" ")
        TXT_ARTICLE.write("\n正文：\n")
        for p in article.xpath('//article[@itemprop="articleBody"]//p'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
        for src in article.xpath('//article[@itemprop="articleBody"]//figure//img/@src'):
            savePhoto("http://www.telegraph.co.uk" + src, "telegraph_" + str(flag) + "_" + str(i))
            i = i + 1
    return
def Liverpool_Manchester(url,flag,name):
    if(md5(url,"url_liverpool_manchester.txt",TXT_URL_liverpool_manchester)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//main//article')[0]
        title = article.xpath('//h1[@itemprop="headline name"]/text()')[0]
        TXT_ARTICLE.write("标题："+title+"\n")
        subtitle = article.xpath('//p[@itemprop="description"]/text()')
        if(len(subtitle) > 0 ):
            TXT_ARTICLE.write("副标题："+subtitle[0]+"\n")
        writer = article.xpath('//div[@class = "author"]')[0].xpath('string(.)')
        time = article.xpath('//ul[@class = "time-info"]')[0].xpath('string(.)')
        TXT_ARTICLE.write("\n作者："+writer+"\n时间："+time+"\n正文：\n")
        i=0
        figure = article.xpath('//figure[@class = "in-article-image lead-article-image"]//img/@content')
        if(len(figure) > 0):
            savePhoto(figure[0], name + str(flag) + "_" + str(i))
            i = i + 1
        for p in article.xpath('//div[@class = "article-body"]//p'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
        for src in article.xpath('//div[@class = "article-body"]//figure//img/@content'):
            savePhoto(src, name + str(flag) + "_" + str(i))
            i = i + 1
    return
def standard(url,flag):
    url = "https://www.standard.co.uk"+url
    if(md5(url,"url_standard.txt",TXT_URL_standard)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//article[@id = "full-article"]')[0]
        title = article.xpath('//h1[@class = "headline"]/text()')[0]
        time = article.xpath('//li[@class = "publish-date"]')[0]
        TXT_ARTICLE.write("标题：" + title +"\n时间：" + time.xpath( 'string(.)').replace("\n", "").replace(" ", "") + "\n")
        writer = article.xpath('//li[@class = "author author-last"]')
        if(len(writer) > 0):
            TXT_ARTICLE.write("作者："+writer[0].xpath('string(.)').replace("\n","").replace(" ","")+"\n")
        i = 0
        img = article.xpath('//figure/amp-img/@src')
        if(len(img) > 0):
            savePhoto("https://www.standard.co.uk"+img[0],"standard_"+str(flag)+"_"+str(i))
            i = i+1
        TXT_ARTICLE.write("正文：\n")
        for p in article.xpath('//div[@class = "body-content"]//p'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
        for src in article.xpath('//div[@class = "body-content"]//figure/amp-img/@src'):
            savePhoto("https://www.standard.co.uk" + src, "standard_" + str(flag) + "_" + str(i))
            i = i + 1
    return

def WorldSoccertalk(url,flag):
    if(md5(url,"url_worldsoccertalk.txt",TXT_URL_worldsoccertalk)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//div[@class = "single_post"]')[0]
        title = article.xpath('//header/h1/text()')[0]
        writer = article.xpath('//span[@class = "theauthor"]//a/text()')[0]
        time = article.xpath('//span[@class = "thetime date updated"]//span/text()')[0]
        TXT_ARTICLE.write("标题："+title+"\n作者："+writer+"\n时间："+time+"\n正文：\n")
        for p in article.xpath('//div[@class = "thecontent"]/p'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
    return

def Bbc(url,flag):
    if(md5(url,"url_bbc.txt",TXT_URL_bbc)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//article[@class = "component component--default story"]')
        if(len(article) > 0 ):
            title = article[0].xpath('//h1/text()')[0]
            time = article[0].xpath('//time')[0].xpath('string(.)')
            TXT_ARTICLE.write("标题：" + title + "\n时间：" + time + "\n")
            writer = article[0].xpath('//p[@class = "gel-long-primer"]/text()')
            if (len(writer) > 0):
                TXT_ARTICLE.write("作者：" + writer[0] + "\n正文：\n")
            for p in article[0].xpath('//div[@id = "story-body"]/p'):
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            i = 0
            for src in article[0].xpath('//div[@id = "story-body"]/figure//img/@src'):
                if (len(src) > 0 and src[0:4] == 'http'):
                    savePhoto(src, "bbc" + "_" + str(flag) + "_" + str(i))
                    i = i + 1
    return
def footbal365_getUrl_1(root,flag):
    for url in root.xpath('//figure[@class = "hero__figure"]/a/@href'):
        flag = flag +1
        footbal365(url,flag)
    for url in root.xpath('//section[@class = "hero"]//li/figure/a/@href'):
        flag = flag + 1
        footbal365(url, flag)
    footbal365_getUrl_2(root,flag)
    return
def footbal365_getUrl_2(root,flag):
    for url in root.xpath('//section[@class = "articleList newslist_widget"]//li/a/@href'):
        flag = flag + 1
        footbal365(url, flag)
    return
def footbal365(url,flag):
    if(url[7:31] == "www.football365.com/news" and md5(url,"url_football365.txt" , TXT_URL_football365)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//article[@class = "article"]')[0]
        title = article.xpath('//header[@class = "article__header"]//h1/text()')[0]
        time = article.xpath('//header[@class = "article__header"]//p/text()')[0]
        TXT_ARTICLE.write("标题："+title+"\n时间："+time+"\n正文：\n")
        i= 0
        img = article.xpath('//span[@class = "article__imgWrapper"]/img/@src')
        if(len(img) > 0):
            savePhoto(img[0], "football365_" + str(flag) + "_" + str(i))
            i = i + 1
        for p in article.xpath('//section[@class = "article__body"]/p'):
            TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
    return

def guardian(url,flag):
    if(md5(url,"url_guardian.txt",TXT_URL_guardian)):
        TXT_ARTICLE.write(
            "\n""===============++++++++++++++++" + str(flag) + "++++++++++==============" + "\n" + url + "\n")
        root = getSimpleRoot(url)
        article = root.xpath('//article[@id = "article"]')
        if(len(article) >0):
            title = article[0].xpath('.//header//h1/text()')[0]
            TXT_ARTICLE.write("标题：" + title)
            subtitle = article[0].xpath('.//meta[@itemprop = "description"]/text()')
            if (len(subtitle) > 0):
                TXT_ARTICLE.write("副标题：" + subtitle[0] + "\n")
            i = 0
            img = article[0].xpath(
                './/div[@class = "content__main-column content__main-column--article js-content-main-column "]/figure/meta[@itemprop = "url"]/@content')
            if (len(img) > 0):
                savePhoto(img[0], "guardian_" + str(flag) + "_" + str(i))
                i = i + 1
            writer = article[0].xpath('.//p[@class = "byline"]//span[@itemprop = "name"]/text()')
            if (len(writer) > 0):
                TXT_ARTICLE.write("作者：" + writer[0] + "\n")
            time = article[0].xpath('.//p[@class = "content__dateline"]/time[@itemprop = "datePublished"]/text()')[0]
            TXT_ARTICLE.write("时间：" + time + "\n")
            TXT_ARTICLE.write("正文：\n")
            for p in article[0].xpath('.//div[@class = "content__article-body from-content-api js-article__body"]/p'):
                TXT_ARTICLE.write(p.xpath('string(.)') + "\n")
            for src in article[0].xpath(
                    './/div[@class = "content__article-body from-content-api js-article__body"]/figure/meta[@itemprop = "url"]/@content'):
                savePhoto(src, "guardian_" + str(flag) + "_" + str(i))
                i = i + 1
            TXT_ARTICLE.write("评论：\n")
            for aside in article[0].xpath(
                    './/div[@class = "content__article-body from-content-api js-article__body"]/aside//p[@class = "pullquote-paragraph"]/text()'):
                TXT_ARTICLE.write(aside + "\n")

    return


TXT_ARTICLE.write("--------------------------------------------泰晤士报----------------------------------------"+"\n")
flag = 0
s_theme = requests.session()
f= s_theme.post(URL_themetimes_login,data=values_themetimes,headers = headers)
root = getRoot(URL_themetimes,s_theme)
for url_sport in root.xpath('//section[@id = "section-sport"]//h3/a/@href'):
    flag = flag + 1
    ThemeTimes(url_sport,flag,s_theme)
if(PC_WEEK == 1):
    for url_game in root.xpath('//section[@id = "section-theGame"]//h3/a/@href'):
        flag = flag + 1
        ThemeTimes(url_game, flag,s_theme)
TXT_URL_themetimes.close()


TXT_ARTICLE.write("--------------------------------------------天空体育----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_skysports_features)
for url_feature in root.xpath('//div[@class = "news-list block "]//div[@class = "news-list__item news-list__item--show-thumb-bp30"]//h4[@class = "news-list__headline"]/a/@href')[0:20]:
    flag = flag +1
    SkySport(url_feature,flag)
root = getSimpleRoot(URL_skysports_pundits)
for url_pundits in root.xpath('//div[@class = "news-list block "]//div[@class = "news-list__item news-list__item--show-thumb-bp30"]//h4[@class = "news-list__headline"]/a/@href')[0:20]:
    flag = flag +1
    SkySport(url_pundits,flag)
TXT_URL_skysport.close()

TXT_ARTICLE.write("--------------------------------------------卫报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_guardian)
for url in root.xpath('//div[@class = "fc-container__inner"]//li//div[@class= "fc-item__container"]/a/@href'):
    flag = flag +1
    guardian(url,flag)
root = getSimpleRoot(URL_guardian_2)
for url in root.xpath('//div[@class = "fc-container__inner"]//li//div[@class= "fc-item__container"]/a/@href'):
    flag = flag +1
    guardian(url, flag)

TXT_ARTICLE.write("--------------------------------------------太阳报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_thesun_football)
TheSun_url(root,flag)
root = getSimpleRoot(URL_theSun_premierleague)
TheSun_url(root,flag)
root = getSimpleRoot(URL_theSun_premierleague02)
TheSun_url(root,flag)
root = getSimpleRoot(URL_theSun_premierleague03)
TheSun_url(root,flag)
TXT_URL_thesun.close()

TXT_ARTICLE.write("--------------------------------------------邮报----------------------------------------"+"\n")
flag = 0

root = getSimpleRoot(URL_dailymail)
for url in root.xpath('//h2[@class = "linkro-darkred"]//a/@href'):
    flag = flag+1
    DailMail(url,flag)
for url in root.xpath('//div[@class = "puff cleared"]//ul[@class ="link-bogr2 linkro-wocc"]//li/a/@href'):
    flag = flag + 1
    DailMail(url, flag)
for url in root.xpath('//div[@id = "automated-articles"]//div[@class = "article article-card"]//h2[@class="headline linkro-darkred"]/a/@href'):
    flag = flag +1
    DailMail(url, flag)
TXT_URL_dailymail.close()

TXT_ARTICLE.write("--------------------------------------------镜报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_mirror)
for url in root.xpath('//main[@class = "mod-pancakes"]//strong/a/@href'):
    flag = flag+1
    Mirror(url,flag)
for url in root.xpath('//main[@class = "mod-pancakes"]//h2/a/@href'):
    flag = flag+1
    Mirror(url, flag)
TXT_URL_mirror.close()

TXT_ARTICLE.write("--------------------------------------------独立报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_independent)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]//h1/a/@href'):
    flag = flag +1
    independent(url,flag)
root = getSimpleRoot(URL_independent_comment)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]//h1/a/@href'):
    flag = flag +1
    independent(url,flag)
root = getSimpleRoot(URL_independent_european)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]/h1/a/@href'):
    flag = flag +1
    independent(url,flag)

TXT_ARTICLE.write("--------------------------------------------电讯报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_telegraph_football)
Telegraph_url(root,flag)
root = getSimpleRoot(URL_telegraph_premier)
Telegraph_url(root,flag)
TXT_URL_telegraph.close()

TXT_ARTICLE.write("--------------------------------------------回声报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_liverpool)
for url in root.xpath('//main//div[@class = "inner"]//strong/a/@href'):
    flag = flag+1
    Liverpool_Manchester(url,flag,"liverpool")

TXT_ARTICLE.write("--------------------------------------------曼彻斯特晚报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_manchester_united)
for url in root.xpath('//main//div[@class = "inner"]//strong/a/@href'):
    flag = flag+1
    Liverpool_Manchester(url,flag,"manchester")
root = getSimpleRoot(URL_manchester_city)
for url in root.xpath('//main//div[@class = "inner"]//strong/a/@href'):
    flag = flag+1
    Liverpool_Manchester(url,flag,"manchester")
TXT_URL_liverpool_manchester.close()

TXT_ARTICLE.write("--------------------------------------------旗帜晚报----------------------------------------"+"\n")
flag = 0
try:
    root = getSimpleRoot(URL_standard)
    for url in root.xpath('//section[@class = "section-content"]//div[@class = "article-hero"]/a/@href'):
        flag = flag + 1
        standard(url, flag)
    for url in root.xpath(
            '//section[@class = "section-content"]//div[@class = "articles"]//div[@class = "article"]/a/@href'):
        flag = flag + 1
        standard(url, flag)
    for url in root.xpath(
            '//section[@class = "section-content"]//div[@class = "article"]/div[@class = "text"]/a/@href'):
        flag = flag + 1
        standard(url, flag)
    TXT_URL_standard.close()
except Exception:
    pass

#TXT_ARTICLE.write("--------------------------------------------路透社----------------------------------------"+"\n")
#flag = 0
#root = getSimpleRoot(URL_reuters)
#print(etree.tostring(root))
#for url in root.xpath(
#        '//div[@class = "news-headline-list  "]//article[@class = "story "]//div[@class = "story-content"]/a/@href'):
#    flag = flag + 1
#    print(str(flag) + "  " + url)
#TXT_URL_reuters.close()

TXT_ARTICLE.write("--------------------------------------------法新社----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_worldsoccertalk)
for url in root.xpath('//div[@id = "content_box"]//article/header/h2/a/@href'):
    flag = flag+1
    WorldSoccertalk(url,flag)
root = getSimpleRoot(URL_worldsoccertalk_2)
for url in root.xpath('//div[@id = "content_box"]//article/header/h2/a/@href'):
    flag = flag+1
    WorldSoccertalk(url,flag)
root = getSimpleRoot(URL_worldsoccertalk_3)
for url in root.xpath('//div[@id = "content_box"]//article/header/h2/a/@href'):
    flag = flag+1
    WorldSoccertalk(url,flag)
TXT_URL_worldsoccertalk.close()

TXT_ARTICLE.write("--------------------------------------------bbc----------------------------------------"+"\n")
flag = 0
try:
    root = getSimpleRoot(URL_bbc)
    for url in root.xpath(
            '//div[@class = "layout__primary-col layout__primary-col--1280"]/section[not(@id = "audio-video")]//article/a[@class = "faux-block-link__overlay"]/@href'):
        if (len(url) > 15 and url[7:11] != "live" and len(url) < 26):
            flag = flag + 1
            Bbc("http://www.bbc.com" + url, flag)
    TXT_URL_bbc.close()
except Exception:
    pass

TXT_ARTICLE.write("--------------------------------------------足球365----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_football365)
footbal365_getUrl_1(root,flag)
TXT_URL_football365.close()

TXT_ARTICLE.write("--------------------------------------------独立报----------------------------------------"+"\n")
flag = 0
root = getSimpleRoot(URL_independent_premier)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]//h1/a/@href'):
    flag = flag +1
    independent(url,flag)
root = getSimpleRoot(URL_independent_transfers)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]//h1/a/@href'):
    flag = flag +1
    independent(url,flag)
root = getSimpleRoot(URL_independent_international)
for url in root.xpath('//div[@id = "content"]//div[@class = "content"]/div[@class = "row"]//article//div[@class = "content"]//h1/a/@href'):
    flag = flag +1
    independent(url,flag)
TXT_URL_independent.close()

TXT_ARTICLE.close()