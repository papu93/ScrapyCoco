# Scrapy settings for ScrapyCocoProviders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyCocoProviders'

SPIDER_MODULES = ['ScrapyCocoProviders.spiders']
NEWSPIDER_MODULE = 'ScrapyCocoProviders.spiders'

# add test line

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 " \
             "Safari/537.36"

# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS=10
#
# # Configure a delay for requests for the same website (default: 0)
# # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# DOWNLOAD_DELAY=0.2
# # The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=10
# CONCURRENT_REQUESTS_PER_IP=10
# DOWNLOAD_TIMEOUT = 600

CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 10
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600

# Disable cookies (enabled by default)
COOKIES_ENABLED=False
ROBOTSTXT_OBEY=False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED=True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zillow.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'zillow.middlewares.HttpProxySet': 700,
#    # 'newspaper.middlewares.HttpProxyRandom': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

MONGO_URI='127.0.0.1'
MONGO_DATABASE='ScrapyCocoProviders'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ScrapyCocoProviders.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# Configure LOG
LOG_ENABLED = True
# LOG_STDOUT = False
LOG_LEVEL = 'INFO'
