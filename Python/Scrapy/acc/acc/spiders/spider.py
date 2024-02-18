import scrapy
from acc.items import *


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.gxcvuedu.com']
    start_urls = ['http://www.gxcvuedu.com/cyyw/']

    def parse(self, response):
        base_url = 'http://www.gxcvuedu.com'
        # print(response.url)    # 返回页面对应的url
        # print(response.status)  # 状态码
        # print(response.meta)
        # print(response.body)   HTTP请求的返回数据(Json or HTML源码)
        # 使用xpath(),css()选择器解析数据
        next_url = response.xpath('//*[@id="content"]/section[1]/div/a[11]/@href').extract_first()
        # 使用lxml解析html时得到的数据为Selector对象需要调用extract()方法得到真正的数据，返回为一个列表对象
        tiles = response.xpath('//*[@id="content"]/section/ul/li/h3/a/text()').extract()
        # print(tile)
        # 使用meta在Request和Response之间传递数据
        detail_pages = response.xpath('//*[@id="content"]/section/ul/li/h3/a/@href').extract()
        # print(tiles, detail_pages)
        for index in range(len(tiles)):
            detail_page = base_url + detail_pages[index]
            tile = tiles[index]
            # Request构造方法callback,将方法的引用赋给他
            # 将每一页的数据title,和内容urls 构造Request请求 并指定交给parse_detail方法处理
            yield scrapy.Request(detail_page, callback=self.parse_detail,
                                 meta={'title': tile}
                                 )

        # 翻页请求通过下一页的Url构造Request对象，并使用yield方法返回
        yield scrapy.Request(url=base_url + next_url)

    def parse_detail(self, response):
        # 获取response的meta字典
        meta = response.meta
        ps = response.xpath('//*[@id="content"]/section[2]/div[1]/p[1]/text()').extract_first()
        # json = {}
        item=AccItem()
        item["title"]=meta["title"]
        item["text"]=ps
        yield item
        # print(json)
