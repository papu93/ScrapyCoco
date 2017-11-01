from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from ScrapyCocoProviders.spiders.spider import MercadoSpider
import json

class ScrapyCocoProviders():
    def __init__(self, product):
        ''' Constructor for this class. '''
        self.product = product

    def run_mercado_libre(self):
        MercadoSpider.name = self.product
        MercadoSpider.allowed_domain = ['www.mercadolibre.com.ar']
        MercadoSpider.start_urls = ['http://listado.mercadolibre.com.ar/' + self.product + '_BestSellers_YES']
        self.run(MercadoSpider)

    def run(self,spider):
        configure_logging()
        runner = CrawlerRunner(get_project_settings())

        @defer.inlineCallbacks
        def crawl():
            yield runner.crawl(spider)
            reactor.stop()

        crawl()
        reactor.run()

    def get_results(self):
        dict = {}
        dict['results'] = MercadoSpider.results
        return json.dumps(dict, default=lambda o: o.__dict__, sort_keys=True, indent=4)

