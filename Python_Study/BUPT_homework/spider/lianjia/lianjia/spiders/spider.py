import scrapy
from lianjia.items import MyItem
import re


class mySpider(scrapy.spiders.Spider):
    name = "lianjia"
    # 爬虫名称
    allowed_domains = ["bj.fang.lianjia.com/"]
    # 允许爬取的网站域名
    start_urls = ["https://bj.fang.lianjia.com/loupan/nhs1/"]
    # 初始URL
    # 对于有多页的网站，可以查看其网址是否使用page=的方式，用下列方式将要爬取的网站URL全部存好
    # 对于存好的URL，spider会自动全部爬取下来
    for page in range(1, 6):
        url = "https://bj.fang.lianjia.com/loupan/nhs1pg{0}/".format(page)
        start_urls.append(url)

    def parse(self, response):  # 解析爬取的内容
        # house在HTML网页中对应的Xpath
        house = "/html/body/div[4]/ul[2]/"
        item = MyItem()
        # 生成一个MyItem对象，接收爬取的数据
        # 一页有10个house
        for i in range(1, 11):
            # 在house的Xpath基础上添加各属性的Xpath，进而爬取各项属性
            item['name'] = response.xpath(house + "li[{0}]/div/div[1]/a/text()".format(i)).extract()

            # 价格分为数字和单位两部分
            temp = response.xpath(house + "li[{0}]/div/div[6]/div[1]/span/text()".format(i)).extract()
            # temp会是一个列表，有两个字符串，因为上述Xpath下有两个文本
            temp_s = temp[0] + temp[1]      # 字符串合并
            # 剔除两个字符串之间的空白字符\xa0，并将其转换到列表中
            item['price'] = re.sub(u"[\u00a0]", "", temp_s).split()

            item['area'] = response.xpath(house + "li[{0}]/div/div[3]//span/text()".format(i)).extract()
            if item['name'] and item['price'] and item['area']:       # 去掉空值
                yield(item)


