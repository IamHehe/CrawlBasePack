# coding=utf-8
# author: dl.zihezhu@gmail.com
# datetime:2020/7/4 19:09

"""
程序说明：
    这是一个爬虫所需的基本功能集合。可以方便以后爬虫的快速调用
    主要基于request和xpath解析进行。
    功能如下：
        1） 构造请求头信息 V
        2） 通过请求，获取网页响应内容 V
        3） 通过确定的xpath位置获取特定内容 V
        4)  记录爬取错误的情况 V
"""
import requests
from lxml import html
import time
import random
from CrawlBasePack.Logger import Logger


class CrawlBase:
    logger = Logger('log.txt', level='info').logger

    def __init__(self, url, headers={}, timeout=20, sleep_time=(8, 15)):
        self.url = url  # 目标网站url
        self.headers = headers  # 头信息
        self.timeout = timeout  # 超出相应时间，默认20s
        self.xhtml = ''  # 设置xhml为空
        self.get_xhtml(sleep_time)  # 获取页面信息


    def get_xhtml(self,sleep_time):
        """
        请求并解析页面，返回xhtml内容
        :return: 解析成xhtml格式的页面信息
        """
        try:
            start, end = sleep_time
            t = random.randint(start, end)  # 随机睡眠时间
            CrawlBase.logger.info('睡眠{0}\t{1}'.format(t, self.url))
            time.sleep(t)  # 设置时间间隔
            html_response = requests.get(self.url, headers=self.headers, timeout=self.timeout)
            self.xhtml = html.etree.HTML(html_response.content.decode("utf-8"))  # 解析网页
        except Exception as e:
            CrawlBase.logger.error('{0}  获取页面错误'.format(self.url))
            CrawlBase.logger.error(e, exc_info=True)  # 可以记录完整报错内容

    def get_content_by_xpath(self, xpath_):
        """
        根据给定的xpath定位，返回定位的内容
        :param xpath: 网页内的定位数据
        :return: content定位内容
        """
        element = []
        try:
            if self.xhtml:
                element = self.xhtml.xpath(xpath_)  #
            else:
                CrawlBase.logger.error('解析页面错误，html页面为空，请检查请求是否成功。\t{0}'.format(self.url))
        except:
            CrawlBase.logger.error('xpath定位元素失败，请检查xpath路径是否正确。t{0}'.format(self.url))
        return element


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': 'uuid_tt_dd=10_29483370930-1582361419816-831826; dc_session_id=10_1582361419816.278624; __gads=ID=28b5af15266f5bc7:T=1582386138:S=ALNI_MaiFCi1P5-79D8ugwFYnEssNZm3NA; UN=qq_33293040; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_29483370930-1582361419816-831826!5744*1*qq_33293040; _ga=GA1.2.1086259409.1582698512; UM_distinctid=170e883645e5c9-08679f6d48739f-4313f6b-146d15-170e883645f730; CNZZDATA1259587897=666137086-1584445206-https%253A%252F%252Fblog.csdn.net%252F%7C1584445206; Hm_ct_68822ecd314ca264253e255a3262d149=5744*1*qq_33293040!6525*1*10_29483370930-1582361419816-831826; __yadk_uid=AEyAvTstr13OvTYlOdaC9PtU4pMnPqAk; Hm_ct_146e5663e755281a5bbe1f3f1c477685=5744*1*qq_33293040!6525*1*10_29483370930-1582361419816-831826; CloudGuest=IgtKd6dPr8WqoJsPyclxhn//7TLyJjFWd/MA+GKI5LVEQxzxrU7S3sB9vywM6c4YbqkGelxSvXKMTGw4xCt36pE+ZD45KYYJXU8ezY/ZHIspJgAFmH9UgFux0C7khsnw1MOQ1wrfv+/u+SbXlMe/ieCIYu2xiJZHrR47SF6G6ulg7ih5/j8LQ0EdK3RZCnYy; Hm_ct_e5ef47b9f471504959267fd614d579cd=5744*1*qq_33293040!6525*1*10_29483370930-1582361419816-831826; Hm_up_68822ecd314ca264253e255a3262d149=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; UserName=qq_33293040; UserInfo=c11ca3cfa58341c8b236462b359b3fa3; UserToken=c11ca3cfa58341c8b236462b359b3fa3; UserNick=%E5%A4%A9%E6%89%8D%E5%B0%8F%E5%91%B5%E5%91%B5; AU=8B3; BT=1590855113150; p_uid=U000000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; Hm_lvt_3d15b54c05cce175f30e9f8e2aeceb64=1591095122; Hm_up_3d15b54c05cce175f30e9f8e2aeceb64=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; Hm_ct_3d15b54c05cce175f30e9f8e2aeceb64=5744*1*qq_33293040!6525*1*10_29483370930-1582361419816-831826; Hm_lvt_68822ecd314ca264253e255a3262d149=1590848185,1591108110; Hm_lvt_244847735f7f8703ad1bce2e52d1f032=1591108180; Hm_up_244847735f7f8703ad1bce2e52d1f032=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; Hm_ct_244847735f7f8703ad1bce2e52d1f032=5744*1*qq_33293040!6525*1*10_29483370930-1582361419816-831826; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1591760617; Hm_up_e5ef47b9f471504959267fd614d579cd=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; Hm_lvt_146e5663e755281a5bbe1f3f1c477685=1591790975; Hm_up_146e5663e755281a5bbe1f3f1c477685=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_33293040%22%2C%22scope%22%3A1%7D%7D; searchHistoryArray=%255B%2522unilm%25E4%25BB%25A3%25E7%25A0%2581%2522%252C%2522unilm%2522%252C%2522unilm%25E5%25AE%259E%25E6%2588%2598%2522%252C%2522soul%2520%25E7%2594%25A8%25E6%2588%25B7%25E7%2594%25BB%25E5%2583%258F%2522%252C%2522soul%2522%252C%2522%25E4%25B8%25AD%25E5%259B%25BD%25E4%25B8%2593%25E5%2588%25A9%25E5%2585%25AC%25E5%25B8%2583%25E5%258F%25B7%2522%252C%2522%25E4%25B8%25AD%25E5%259B%25BD%25E4%25B8%2593%25E5%2588%25A9%25E5%2585%25AC%25E5%25B8%2583%25E5%258F%25B7%2520%25E7%2588%25AC%25E8%2599%25AB%25E4%25B8%2593%25E5%2588%25A9%25E5%258F%25B7%2522%252C%2522LongSumm%2522%252C%2522%25E5%25AD%2590%25E4%25B8%25BB%25E9%25A2%2598%25E6%25B3%25A8%25E6%2584%258F%25E5%258A%259B%25E6%259C%25BA%25E5%2588%25B6%2522%252C%2522dssa%2522%255D; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fcompanyzh%252F5o1Kf1RQ%253Futm_source%253D1593515841%2522%252C%2522announcementCount%2522%253A0%257D; _gid=GA1.2.1464665528.1593862246; dc_sid=4880b851ec61915be57158379d6ee732; TY_SESSION_ID=8ea954a6-b30c-4e36-9c48-f38fa253968d; c_first_ref=www.google.com; c_first_page=https%3A//blog.csdn.net/u010895119/article/details/79470443; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1593862245,1593862246,1593862312,1593876545; c_utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase; dc_tos=qcychh; c_ref=https%3A//blog.csdn.net/qq_33293040; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1593878453',
    }
    cb = CrawlBase(url='https://blog.csdn.net/qq_33293040', headers=headers)
    res = cb.get_content_by_xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a')
    CrawlBase.logger.info('解析获取结果为。\t{0}'.format(res[0].attrib['href']))

