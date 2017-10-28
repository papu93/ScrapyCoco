# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from ..items import MercadoItem
from scrapy import Request

class MercadoSpider(scrapy.Spider):
    #name = 'mercadoLibre'
    item_count = 0
    #allowed_domain = ['www.mercadolibre.com.ar']
    #product = 'celulares'
    #start_urls = ['http://listado.mercadolibre.com.ar/' + product + '_BestSellers_YES']

    def parse(self,response):
        for article in response.xpath('//h2[contains(@class,"item__title")]/a/@href'):
            articleLink = article.extract()
            yield Request(response.urljoin(articleLink), callback=self.parse_item)

        next_page = response.xpath('//li[@class="pagination__next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item(self, response):
        sellerLink = response.xpath('//section[@class="ui-view-more vip-section-seller-info new-reputation"]/a/@href').extract_first()
        return Request(response.urljoin(sellerLink), callback=self.parse_seller)

    def parse_seller(self, response):
        if self.item_count < 20:
            ml_item = MercadoItem()
            # info de la tienda o vendedor
            ml_item['seller_name'] = response.xpath('normalize-space(//h3[@id="store-info__name"]/text())').extract_first()
            ml_item['seller_URL'] = response.url
            ml_item['sales_amount'] = response.xpath('normalize-space(//p[@class="sales-amount"]/text())').extract_first()
            ml_item['seller_category'] = \
            (response.xpath('normalize-space(//p[@class="leader-status__message"]/text())').extract_first()).split(",")[0]
            ml_item['location'] = response.xpath(
                'normalize-space(//p[@class="location__description"]/text())').extract_first()
            ml_item['buyers_feedback_amount'] = response.xpath(
                'normalize-space(//span[@class="total"]/text())').extract_first()
            ml_item['good_qualification'] = response.xpath(
                'normalize-space(//a[@class="buyers-feedback-bar__items buyers-feedback-bar--positive"]/li/span[2]/text())').extract_first()
            ml_item['neutral_qualification'] = response.xpath(
                'normalize-space(//a[@class="buyers-feedback-bar__items buyers-feedback-bar--neutral"]/li/span[2]/text())').extract_first()
            ml_item['bad_qualification'] = response.xpath(
                'normalize-space(//a[@class="buyers-feedback-bar__items buyers-feedback-bar--negative"]/li/span[2]/text())').extract_first()

            self.item_count += 1
            print(ml_item)
            return ml_item
        else:
            raise CloseSpider('item_exceeded')