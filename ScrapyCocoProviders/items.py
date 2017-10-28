import scrapy

class MercadoItem(scrapy.Item): #info de la tienda o vendedor
    seller_name = scrapy.Field()
    seller_URL = scrapy.Field()
    sales_amount = scrapy.Field()
    seller_category = scrapy.Field()
    location = scrapy.Field()
    buyers_feedback_amount = scrapy.Field()
    good_qualification = scrapy.Field()
    neutral_qualification = scrapy.Field()
    bad_qualification = scrapy.Field()
