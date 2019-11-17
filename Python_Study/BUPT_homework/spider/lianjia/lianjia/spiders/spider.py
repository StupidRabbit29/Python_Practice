import scrapy
from lianjia.items import MyItem

class mySpider(scrapy.spiders.Spider):
    name = "lianjia"
    # 爬虫名称
    allowed_domains = ["bj.fang.lianjia.com/"]
    # 允许爬取的网站域名
    start_urls = ["https://bj.fang.lianjia.com/loupan/nhs1/"]
    # 初始URL
    for page in range(1, 6):
        url = "https://bj.fang.lianjia.com/loupan/nhs1pg{0}/".format(page)
        start_urls.append(url)

    def parse(self, response):  # 解析爬取的内容
        house = "/html/body/div[4]/ul[2]/"
        item = MyItem()
        # 生成一个MyItem对象，接收爬取的数据
        for i in range(1, 11):
            item['name'] = response.xpath(house + "li[{0}]/div/div[1]/a/text()".format(i)).extract()
            item['price'] = response.xpath(house + "li[{0}]/div/div[6]/div[1]/span/text()".format(i)).extract()
            item['area'] = response.xpath(house + "li[{0}]/div/div[3]//span/text()".format(i)).extract()
            # if item['university'] and item['classnum']:  # 去掉空值
            yield(item)




