#from scrapy import signals
'''
class Mercado(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        #file = open('%s_items.csv' % spider.name, 'w+b')
        #self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = ['seller_name', 'seller_URL', 'sales_amount', 'seller_category',
                                          'location',
                                          'buyers_feedback_amount', 'good_qualification', 'neutral_qualification',
                                          'bad_qualification']
        self.exporter.start_exporting()


    def spider_closed(self, spider):
        #self.exporter.finish_exporting()
        #file = self.files.pop(spider)
        #file.close()

        self.client.close()

    def process_item(self, item, spider):
        #self.db[self.collection_name].insert(dict(item))
        #print('insertando')
        #self.files.append(item)
        #self.files['sellers'].insert(0, item)
        #print('ya inserto')
        #self.exporter.export_item(item)
        return item
'''