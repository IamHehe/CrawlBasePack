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
from Logger import Logger
# from CrawlBasePack.Logger import Logger   # 用于选择


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
        'Cookie': 'Use your cookie to replace.'}
    cb = CrawlBase(url='https://blog.csdn.net/qq_33293040', headers=headers)
    res = cb.get_content_by_xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a')
    CrawlBase.logger.info('解析获取结果为。\t{0}'.format(res[0].attrib['href']))

