__author__ = 'CLARK'
# -*- coding:utf-8 -*-

# minimum script
# to crawl a page with a next button with html property:accesskey
# it's easy to customize

from bs4 import BeautifulSoup
import os
import requests


class GetBookCrawler:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.host = 'http://theurlyouwanttocrawl'

    def save(self, html, name):
        file_name = name
        f = open('./book/' + file_name, 'ab')
        f.write(html.content)
        f.close()

    def request(self, url):
        r = requests.get(url, headers=self.headers)
        return r

    def crawl(self, last_url):
        html = self.request(self.host + last_url)
        self.save(html, last_url)
        soup = BeautifulSoup(html.content, 'lxml')
        next_page = soup.find(accesskey="n")

        if(next_page.name == 'a'):
            self.crawl(next_page['href'])
        else:
            exit()

crawler = GetBookCrawler()
crawler.crawl('pr01')
