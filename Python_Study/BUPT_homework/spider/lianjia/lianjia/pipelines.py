# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv


class MyPipeline(object):
    def open_spider(self, spider):
        # 存储文件
        try:
            self.file = open('MyData.csv', "w", encoding="GB18030", newline='')
            # self.file = open('MyData.json', "w", encoding="utf-8")
            self.headers = ['name', 'loc1', 'loc2', 'loc3', 'housetype', 'area', 'avgprice', 'tolprice']
            self.writer = csv.DictWriter(self.file, fieldnames=self.headers)
            self.writer.writeheader()
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        # dict_item = dict(item)  # 生成字典对象
        # json_str = json.dumps(dict_item, ensure_ascii=False) + "\n"  # 生成json串
        # self.file.write(json_str)  # 将json串写入文件中
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()



