import scrapy
from myfirstscraper.items import MyfirstscraperItem
from scrapy.http import Request
import sys

URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20210119&page=%s'
start_page = 1

def remove_space(descs:list) -> list:
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())

    return result

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]

    def start_requests(self):
        for i in range(2): # 0, 1 ~ 9 -> 1 ~ 10
            yield Request(url=URL % (i + start_page), callback=self.parse) # yield = 생성자 반환

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt/a/text()').extract()
        titles_convert = remove_space(titles)
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        

        # items 에 xpath, css를 통해 추출한 데이터를 저장
        items = []

        for idx in range(len(titles_convert)):
            item = MyfirstscraperItem()
            item['title'] = titles_convert[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)
        
        return items
