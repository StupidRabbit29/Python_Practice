import scrapy

from test1.items import MyItem #从items.py中引入MyItem对象

class mySpider(scrapy.spiders.Spider):
    name = "bupt"   #爬虫的名字是bupt
    allowed_domains = ["bupt.edu.cn/"]      #允许爬取的网站域名

    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]
    #初始URL，即爬虫爬取的第一个URL

    def parse(self, response):  #解析爬取的内容
        '''
        name1 = response.xpath('/html/body/div[5]/div[2]/div/div[2]/ul')
        name2 = response.xpath('/html/body/div[5]/div[2]/div/div[2]/ul/li[3]/a/span')
        title1 = name1.extract_first()
        title2 = name1.extract_first()
        print("**********",title1)
        print("==========",title2)
        print("****************************************")
'''
        filename = "bupt_schools.html"
        f1 = open(filename, 'w')
        yield (response)
        #f1.write(str(yield(response)))
        #运行之后，如果打印的日志出现[scrapy] INFO: Spider closed(finished)，代表执行完成。 之后当前文件夹中就出现了一个
        #bupt_scholls.html文件，里面就是我们刚刚要爬取的网页的全部源代码信息。

        item = MyItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath("/html/body/div/div[2]/div[2]/div/ul/li[4]/div/*"):
            item['school'] = each.xpath("text()").extract()  #学院名称在span中
            item['link'] =each.xpath("@href").extract()           #学院链接在href中
            if(item['school'] and item['link'] ):   #去掉值为空的数据
                yield(item)                         #返回item数据给到pipelines模块

            '''
        print("--------------------")
        print(MyData.__len__())
        for e1 in (MyData):
            print(e1)


                print(school)
                schools.append(school)

            if(link!=[]):
                print(link)
                links.append(link)
        print("--------------------")
        print(schools)
        print(links)


        quotes = response.css('.clear')
        for quote in (quotes):
            item = QuoteItem()
            item['clear'] = quote.css('.text::title').extract_first()
            #item['main_ul_span lf'] = quote.css('.tags .tag::text').extract()
            print("******************")
            print(item)
         '''


# 获取网站标题


# 提取网站标题


