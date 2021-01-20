import scrapy
from myfirstscraper.items import MyfirstscraperItem
from scrapy.http import Request
import sys

URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20210119&page=%s'
start_page = 1

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]

    def start_requests(self):
        for i in range(2): # 0, 1
            yield Request(url=URL % (i + start_page), callback=self.parse) # yield = 생성자 반환

    def parse(self, response):
        # titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        # scores = response.css('.st_on::text').extract()
        # reviews = response.css('.report::text').extract()
        # writers = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/a/text()').extract()
        # dates = response.css('.br::text').extract()

        # items 에 xpath, css를 통해 추출한 데이터를 저장
        items = []
        """ 내코드
        items.append(titles)
        items.append(writers)
        items.append(previews)
        """

        for idx in range(len(titles)):
            item = MyfirstscraperItem()
            item['title'] = titles[idx]
            # item['score'] = scores[idx]
            # item['review'] = reviews[idx]
            item['writer'] = writers[idx]
            # item['date'] = dates[idx]

            items.append(item)
        
        return items
