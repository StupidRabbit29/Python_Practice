import scrapy
from test1.items import MyItem

class mySpider(scrapy.spiders.Spider):
    name = "xuetang"    # 爬虫名称
    allowed_domains = ["www.xuetangx.com/"]     # 允许爬取的网站域名
    start_urls = ["http://www.xuetangx.com/partners"]       # 初始URL

    def parse(self, response):  # 解析爬取的内容
        item = MyItem()
        # 生成一个MyItem对象，接收爬取的数据

        # 一共爬取143所大学的课程信息
        for i in range(1, 144):
            item['university'] = response.xpath("/html/body/article[1]/section/ul/li[{}]"
                                                "/a/div[1]/span/img/@title".format(i)).extract()
            item['classnum'] = response.xpath("/html/body/article[1]/section/ul/li[{}]"
                                              "/a/div[2]/p/text()".format(i)).extract()
            if item['university'] and item['classnum']:  # 去掉空值
                yield(item)

