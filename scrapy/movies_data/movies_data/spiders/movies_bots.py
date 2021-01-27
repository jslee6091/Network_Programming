import scrapy
from movies_data.items import MoviesDataItem


def remove_space(descs:list) -> list:
    # 공백 제거
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())
    
    return result

class MoviesBotsSpider(scrapy.Spider):
    name = 'movies_bots'
    allowed_domains = ['naver.com']
    # 마지막에 / 있으면 디렉터리가 되므로 제거했음
    start_urls = ['http://movie.naver.com/movie/point/af/list.nhn']

    def parse(self, response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        stars = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        # descs는 전송되는 데이터에 공백이 매우 많이 있으므로 이를 제거하는 선처리 작업을 해야함
        descs = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        converted_descs = remove_space(descs)

        writers = response.css('.author::text').extract()
        dates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()

        for row in zip(titles, stars, converted_descs, writers, dates):
            item = MoviesDataItem()
            item['title'] = row[0]
            item['star'] = row[1]
            item['desc'] = row[2]
            item['writer'] = row[3]
            item['date'] = row[4]

            yield item

