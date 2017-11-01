# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from ..items import MercadoItem
from scrapy import Request


class MercadoSpider(scrapy.Spider):
    results = []
    item_count = 0

    def parse(self, response):
        for article in response.xpath('//h2[contains(@class,"item__title")]/a/@href'):
            article_link = article.extract()
            yield Request(response.urljoin(article_link), callback=self.parse_item)

        next_page = response.xpath('//li[@class="pagination__next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item(self, response):
        seller_link = response.xpath('//section[@class="ui-view-more vip-section-seller-info new-reputation"]/a/@href').extract_first()
        return Request(response.urljoin(seller_link), callback=self.parse_seller)

    def parse_seller(self, response):
        if self.item_count < self.max_items:
            ml_item = MercadoItem()
            ml_item['seller_name'] = response.xpath('normalize-space(//h3[@id="store-info__name"]/text())').extract_first()
            ml_item['seller_URL'] = response.url
            aux = (response.xpath('normalize-space(//p[@class="sales-amount"]/text())').extract_first()).split(" ")[0]
            ml_item['sales_amount'] = self.convert_to_number(aux)
            ml_item['seller_category'] = (response.xpath('normalize-space(//p[@class="leader-status__message"]/text())').extract_first()).split(",")[0]
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
            self.add_item(ml_item)
            return ml_item
        else:
            raise CloseSpider('item_exceeded')

    def convert_to_number(self, sales):
        digits = len(sales)
        count = 0
        sales = sales.split(".")
        result = " "
        while digits > 0:
            result = result + sales[count]
            count += 1
            digits -= 4
        return int(result)

    def add_item(self, item):
        pos = 0
        for x in range(len(self.results)):
            aux = self.results[x]
            if aux['sales_amount'] > item['sales_amount']:
                pos += 1
            else:
                break
        self.results.insert(pos, item)

