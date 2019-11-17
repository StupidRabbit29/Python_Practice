import scrapy
import time

from test3.items import MyItem #从items.py中引入MyItem对象
'''
class mySpider(scrapy.spiders.Spider):
    name = "lianjia"   #爬虫的名字是douban
    allowed_domains = ["www.lianjia.com/"]      #允许爬取的网站域名

    #name = "homelink"
    # 如果没有特别指定其他的url，spider会以start_urls中的链接为入口开始爬取
    start_urls = ["https://m.lianjia.com/cd/loupan/"]
    for page in range(1, 6):
        url = "https://m.lianjia.com/cd/loupan/pg{0}/".format(page)
        start_urls.append(url)
        # parse是scrapy.Spider处理http response的默认入口
        # parse会对start_urls里的所有链接挨个进行处理
        def parse(self, response):
            loupan = response.xpath('//*[@id="root"]/section/div[4]/div[1]/div')
            #loupan = response.xpath("//div[@class='list-view-section-body']")

            print("**********************")
            print(len(loupan))
            item = MyItem()
            #for each in loupan:
            for i in range(20):
                item['name']  = loupan.xpath('div[{}]/div/a/div[2]/h2/span[1]/text()'.format(i)).extract()
                item['score'] = loupan.xpath('div[{}]/div/a/div[2]/div[1]/div/span[1]/text()'.format(i)).extract()
                if (item['name'] and item['score']):  # 去掉值为空的数据
                    yield (item)
                else:
                    print("------------------------",item['name'],item['score'])


    #start_urls = ["https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"]
    #start_urls = ["https://bj.lianjia.com/ershoufang/"]
    #初始URL，即爬虫爬取的第一个URL

    def parse(self, response):  #解析爬取的内容
        item = MyItem()
        #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据

        for each in response.xpath("/html/body/div[3]/div/div[1]/dl[2]/dd/div[1]/div"):
            item['name'] = each.xpath("a")
            item['score']= each.xpath("a")
            if(item['name'] and item['score'] ):   	#去掉值为空的数据
                yield(item)

        "//*[@id="content"]/div[1]"
        "//*[@id="content"]"

                                   '//*[@id="page-0---9d55d829-698e-4d30-78c1-d63e416d785e"]/section/div[3]/div[3]/div/ul[1]'
        for each in response.xpath('//*[@id="page-0---9d55d829-698e-4d30-78c1-d63e416d785e"]/section/div[3]/div[3]'):
            #每个li标签中的数据，就是我们需要的数据

            item['name'] = each.xpath('/*[@id="content"]/div/div[1]/div/div[4]/div/li[1]/div[1]/div[2]/div/a').extract()
            #item['name'] = each.xpath("a/p").extract()
            #电影名称在span中

            #item['score'] =each.xpath("a/p/strong").extract()
            item['score'] =each.xpath("li[1]/div[1]/div[6]/div[1]/span").extract()
            #得分链接在href中

# 定义spider的名字，在调用spider进行crawling的时候会用到：
#   scrapy crawl <spider.name>

"//*[@id="content"]/div[1]/ul/li[1]/div[1]/div[2]/div/a"
"//*[@id="content"]/div[1]/ul/li[2]/div[1]/div[2]/div/a"
"//*[@id="content"]/div[1]/ul/li[31]/div[1]/div[2]/div/a"
'''

class mySpider(scrapy.spiders.Spider):
    name = "lianjia"   #爬虫的名字是douban
    allowed_domains = ["www.lianjia.com/"]      #允许爬取的网站域名


#爬取多页的代码

    start_urls = []
    for page in range(1, 5):
        url = "https://bj.lianjia.com/ershoufang/pg{}/".format(page)

        start_urls.append(url)
        # parse是scrapy.Spider处理http response的默认入口

        def parse(self, response):
            #print("**********************")
            item = MyItem()
            for i in range(32):
                item['name']  = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[2]/div/a/text()'.format(i+1)).extract()
                item['desp']  = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[2]/div/text()'.format(i+1)).extract()
                item['price'] = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[6]/div[1]/span/text()'.format(i+1)).extract()

                if (item['name'] and item['desp'] and item['price']):  # 去掉值为空的数据
                    yield (item)



