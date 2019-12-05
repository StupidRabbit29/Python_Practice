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
            findarea = False
            findtol = False
            # 在house的Xpath基础上添加各属性的Xpath，进而爬取各项属性
            # 房源名字
            item['name'] = response.xpath(house + "li[{0}]/div/div[1]/a/text()".format(i)).extract()
            if item['name']:
                item['name'] = item['name'][0].strip()

            # 房源的地理位置，分三个字段，分别抓取
            item['loc1'] = response.xpath(house + "li[{0}]/div/div[2]/span[1]/text()".format(i)).extract()
            item['loc2'] = response.xpath(house + "li[{0}]/div/div[2]/span[2]/text()".format(i)).extract()
            item['loc3'] = response.xpath(house + "li[{0}]/div/div[2]/a/text()".format(i)).extract()
            if item['loc1']:
                item['loc1'] = item['loc1'][0].strip()
            if item['loc2']:
                item['loc2'] = item['loc2'][0].strip()
            if item['loc3']:
                item['loc3'] = item['loc3'][0].strip()

            # 房源的最小房型
            item['housetype'] = response.xpath(house + "li[{0}]/div/a/span[1]/text()".format(i)).extract()
            if item['housetype']:
                item['housetype'] = int(re.sub(r'[^0-9]', '', item['housetype'][0]))
            else:
                item['housetype'] = ''

            # 获取最小面积
            item['area'] = response.xpath(house + "li[{0}]/div/div[3]//span/text()".format(i)).extract()
            if item['area']:
                # 先去除非数字或-的所有字符，再取字符串开头的第一个数字，即最小面积
                item['area'] = re.sub(r'[^-0-9]', '', item['area'][0])
                item['area'] = int(re.findall(r'\A\d+', item['area'])[0])
                findarea = True
            else:
                item['area'] = ''

            # 获取总价
            item['tolprice'] = response.xpath(house + "li[{0}]/div/div[6]/div[2]/text()".format(i)).extract()
            if item['tolprice']:
                # 去除所有非数字字符得到总价
                item['tolprice'] = int(re.sub(r'[^0-9]', '', item['tolprice'][0]))
                findtol = True
            else:
                item['tolprice'] = ''

            # 价格分为数字和单位两部分
            temp = response.xpath(house + "li[{0}]/div/div[6]/div[1]/span/text()".format(i)).extract()
            # temp会是一个列表，有两个字符串，因为上述Xpath下有两个文本
            # temp_s = temp[0] + temp[1]      # 字符串合并
            if temp[0]:
                temp_p = temp[0]
                if re.findall(r'均价', temp[1]) != []:
                    # 网页上均价位置确实存放了均价，转换单位，并修改总价
                    item['avgprice'] = round(int(temp_p) / 10000, 4)
                    if findarea:
                        item['tolprice'] = int(item['avgprice'] * item['area'])
                else:
                    # 网页上显示的是总价，用总价除最小面积得到均价
                    if findarea and findtol:
                        item['avgprice'] = round(item['tolprice'] / item['area'], 4)
            else:
                item['avgprice'] = ''

            # 剔除两个字符串之间的空白字符\xa0，并将其转换到列表中
            # item['avgprice'] = re.sub(u"[\u00a0]", "", temp_s).split()

            yield (item)
