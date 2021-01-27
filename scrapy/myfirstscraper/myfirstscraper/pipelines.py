# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyfirstscraperPipeline:
    def process_item(self, item, spider):
        return item
    
    """
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        self.storeInDb(item)
        return item

    def setupDBcon(self):

    def createTables(self):

    def storeInDb(self.item):
        self.cur.execute("INSERT INTO News(title,writer,preview) VALUES(?,?,?)",(item.get('title',''),item.get('writer',''), item.get('preview','')))
        print('-------------------------')
        print('Data Stored in Database')
        print('-------------------------')
        self.con.commit()
    """
