# -*- coding:utf-8 -*-
"""
5.20
降耦合，把功能重新细分出来

"""
import os
import sys
import time
from functools import wraps
import asyncio

sys.path.append('./')
import redis


from my_crawler import InfoCrawler, DetailCrawler, run_crawler
from operateDB import insert_to_detail, insert_to_info
from my_logger import MyLogger



Logger = MyLogger('main')


DETAIL_RULE = {
    'title': '//div[@class="con_top"]/a[3]/text()',
    'chapter': '//div[@class="bookname"]/h1/text()',
    'content': ['//div[@id="content"]', ],
    }
# DETAIL_URLS = [[0, 'http://www.ranwen.org/files/article/56/56048/10973525.html'],
#                [1, 'http://www.ranwen.org/files/article/56/56048/11281440.html'], ]

# INFO_URLS = 'http://www.ranwen.org/files/article/19/19388/'
INFO_RULE = {
    'urls': '//div[@class="box_con"]/div[@id="list"]/dl/dd/a/@href',
    'title': '//div[@id="maininfo"]/div[@id="info"]/h1/text()',
    'author': '//div[@id="maininfo"]/div[@id="info"]/p[1]/text()',
    'status': '//div[@id="maininfo"]/div[@id="info"]/p[2]/text()',
    'category': '//div[@class="con_top"]/a[2]/text()',
    'resume': '//div[@id="maininfo"]/div[@id="intro"]/p[1]/text()',
    'img_url': '//div[@id="fmimg"]/img/@src',
    }


def time_clock(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('start {}'.format(func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        print('all done, it cost {} s'.format(time.time() - start_time))
        return res
    return wrapper


@time_clock
def download_info(info_urls):
    # loop = asyncio.get_event_loop()
    # asyncio.set_event_loop(None)
    # infoc = InfoCrawler(urls=info_urls, parse_rule=INFO_RULE, loop=loop, store_path='./info')
    # loop.run_until_complete(infoc.crawl())
    # infoc.close()
    # loop.close()

    infoc = InfoCrawler(urls=info_urls, parse_rule=INFO_RULE, store_path='./info')
    run_crawler(infoc)
    return infoc.store_path


def download_detail(detail_urls):
    detailc = DetailCrawler(urls=detail_urls, parse_rule=DETAIL_RULE, store_path='./book')
    run_crawler(detailc)
    return detailc.store_path


def insert_info(store_path):
    info_list = os.listdir(store_path)
    for info in info_list:
        insert_to_info(store_path + info, pk=int(info))


def insert_detail(store_path):
    folder_list = os.listdir(store_path)
    for folder in folder_list:  # 这里的逻辑已经是下载完全部一次存完
        folder_path = store_path + folder
        detail_name_list = os.listdir(folder_path)
        # for detail in detail_list:  # 一个文件夹里可能有1000+的文件，不要逐个存入，要一次存入多个
        #     insert_to_detail(folder_path + detail)
        detail_list = [folder_path + '/' + i for i in detail_name_list]
        insert_to_detail(detail_list)


@time_clock
def get_url_from_redis(table_index):  # 这里的逻辑是一次只下载一本
    if isinstance(table_index, list):
        table_index = table_index[0]

    conn = redis.StrictRedis()
    length = conn.llen(table_index)
    items = conn.lrange(table_index, 0, length-1)
    detail_urls = []
    for item in items:
        index, url = str(item).split('!')
        detail_urls.append([index[2:], url[:-1]])
    download_detail(detail_urls)


if __name__ == '__main__':
    import threading

    info_urls = [
        'http://www.ranwen.org/files/article/19/19388/',
        'http://www.ranwen.org/files/article/76/76945/',
        'http://www.ranwen.org/files/article/77/77081/',
        # 'http://www.ranwen.org/files/article/56/56048/',
                 ]

    # download_info(info_urls)
    # t = threading.Thread(target=get_url_from_redis, args=['1'])  # 怎么在线程中调用事件循环好呢
    # t.setDaemon(True)
    # t.start()
    # t.join()

    get_url_from_redis('1')
