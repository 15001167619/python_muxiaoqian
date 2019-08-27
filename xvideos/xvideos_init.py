#coding=utf-8
#!/usr/bin/python
# 导入requests库
import requests
# 导入文件操作库
import os
import bs4
from bs4 import BeautifulSoup

import json
import sys

import random

import you_get
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()



# 越多越好
meizi_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
]
# 给请求指定一个请求头来模拟chrome浏览器
global headers

headers = {'User-Agent': random.choice(meizi_headers)}

xvideos = 'https://www.xvideos.com/?k=china&p='

videos = 'https://www.xvideos.com'
# 定义存储位置
global save_path
save_path = 'G:\Videos'

def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


# 创建文件夹
def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    os.chdir(file_path)

# 获取视频地址
def getTitleName(page_title):
    page_title = str(page_title)
    page_title = page_title.replace('<h2 class="page-title">', '')
    return page_title[0:page_title.index('<span')]


def getVideoApi(videoUrl):
    videoUrl = videoUrl.replace('https://www.xvideos.com/video', '')
    return 'https://www.xvideos.com/video-download/' + videoUrl[0:videoUrl.index('/')]


def initVideosUrl(videosUrls):
    for i in range(0, len(videosUrls)):
        videoUrl = videos + videosUrls[i]
        res = requests.get(videoUrl, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        page_title = soup.find('h2', class_='page-title')
        titleName = getTitleName(page_title)
        print('视频内容：' + titleName)
        videoApiUrl = getVideoApi(videoUrl)
        downloadHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',

            'Cookie': 'pending_thumb=%7B%22t%22%3A%5B%5D%2C%22s%22%3A%5B%5D%2C%22p%22%3A%5B%5D%2C%22r%22%3A%5B%5D%7D; html5_pref=%7B%22SQ%22%3Afalse%2C%22MUTE%22%3Afalse%2C%22VOLUME%22%3A1%2C%22FORCENOPICTURE%22%3Afalse%2C%22FORCENOAUTOBUFFER%22%3Afalse%2C%22FORCENATIVEHLS%22%3Afalse%2C%22PLAUTOPLAY%22%3Atrue%2C%22CHROMECAST%22%3Afalse%2C%22EXPANDED%22%3Afalse%2C%22FORCENOLOOP%22%3Afalse%7D; thumbloadstats_vthumbs=%7B%222%22%3A%5B%7B%22s%22%3A2%2C%22d%22%3A66%7D%5D%2C%22last%22%3A%7B%22s%22%3A2%2C%22v%22%3A%5B66%5D%7D%7D; multi_accounts=81b01dfa31b037bf0svUxV9EzJxFLxQegqJtTg6DIk6KMyx7JYUehSbbNMw91UfdWFHr43wQ-4-TNVrj; X-Backend=2|XWOTe|XWOTM; chat_data_c=; last_views=%5B%2242223859-1566801340%22%2C%2246281955-1566804235%22%2C%2245833535-1566806901%22%2C%2247428105-1566806935%22%2C%2248778547-1566807071%22%5D; chat_deco=0; HEXAVID_LOGIN=b93de85ffcbb27d8QvMFkGB5NsQvWWxr-xAJc_KmRQtPVAUetK6MTpEuTlAO6-GNiAd3MQNFe322nty-D1XFMC_HgV4AQQ2vpfMP4o77Gt3wmA9nShDPo4Lwkm9E82qS9sqhb67JIx9K7dK4gDIkbq7ruTfSiKF5qAwDr3QwTtxRnSM1IwlXy6WUyfF37pmf3eWwCS5q4121uhNze5Lbyi4Ijo-2exww1tmKwO-VrzaiPpsTakuC4J43hNwXafsERXvvPrbE_Ho7DQnca0A4d1JfMSw88DPcC4KEoRBhc7qE95dMR_YdsYtrzUTG9U4dkKWeHuflQerMU5Eqnw1whipcTeOJOToGrhAiet_lzokcO7Pd72FXsb5XxRjfaD-z3vmGA4Qb64Devh92zBc4j8pRTLr_oWpQ8SIQ3qgkyoNU6eAO9torFHAw5RmU3xPSwk3cQ6J3b6du7SgkUXo4koiJxLYehfDULoqMTpcOR1Ad_xmwfwuWuHp0eEoaS2R1leDSJkHHtA4XHYItqCWb1EInjzq-CwuOE8SGVir1IzOWbfWsAHQlcsQq7Rdd_-dzdInPpVaFO6igruqSvifpmyZ6zFV3u6tse-e7n6TIATZi5Qnpmf6IfhTMh3-7o5LopIe3YK5RgWNpu3pm',
            'Host': 'www.xvideos.com',

            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        apiRes = requests.get(videoApiUrl, headers=downloadHeaders)
        apiSoup = BeautifulSoup(apiRes.text, 'html.parser')
        videoDownload = json.loads(str(apiSoup))['URL']
        videoDownloadUrl = str(videoDownload).replace("amp;", "")

        if 'amp;' in videoDownloadUrl:
            videoDownloadUrl = str(videoDownloadUrl).replace("amp;", "")

        print("视频资源下载地址： "+ videoDownloadUrl)
        # 视频输出的位置
        try:
            download(videoDownloadUrl, save_path)
            print(videoDownload)
        except Exception as e:
            print(e)










# 主方法
def main():

    for i in range(2, 100):
        # 获取每页的URL地址
        if i == 1:
            xvideosUrl = xvideos
        else:
            xvideosUrl = xvideos + str(i)
        file = save_path + '\\' + str(i)
        createFile(file)
        # 抓取地址
        print('抓取父页面地址' + xvideosUrl)
        res = requests.get(xvideosUrl, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        hrefs = soup.find(attrs={'class': 'mozaique'}).find_all('a', href=True)
        # 获取视频链接地址
        videosUrls = []

        for a in hrefs:
            hrefUrl = a['href']
            if 'profiles' not in hrefUrl or 'video' in hrefUrl:
                if hrefUrl not in videosUrls:
                    videosUrls.append(hrefUrl)

        initVideosUrl(videosUrls)








if __name__ == '__main__':
    main()


