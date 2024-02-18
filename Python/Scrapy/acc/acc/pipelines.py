import pymongo


# 数据保存到数据库中，重写3个方法
# open_spider(self,spider)  创建数据库链接
# process_item(self, item, spider) 将数据保存到数据库中
# close_spider(self,spider) 关闭数据库链接
class AccPipeline(object):

    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        # db_name 数据库名称
        self.db = self.conn.db_name
        self.stu = self.db.stu

    def process_item(self, item, spider):
        self.stu.insert({
            "title": item['title'],
            "text":item['text']
        })
        # print(item)
        return item

    def close_spider(self, spider):
        self.conn.close()