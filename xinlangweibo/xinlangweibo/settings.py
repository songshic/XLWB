# -*- coding: utf-8 -*-

# Scrapy settings for xinlangweibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xinlangweibo'

SPIDER_MODULES = ['xinlangweibo.spiders']
NEWSPIDER_MODULE = 'xinlangweibo.spiders'

MONGO_URL = "localhost"
MONGO_DB = 'xlweibo'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xinlangweibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_T_WM=0c0093cb2aabfdbbee5d7e9b10d55547; SSOLoginState=1515817830; ALF=1518409830; SCF=AmhR2zuekXmoQ0X9ICBM5PZKfjMCpVOgpX-FeILMsyn2AxQjRRtZX-1EU7v_Xl420dLn5b5_rlLYw3ZCgKlbWnw.; SUB=_2A253Xfs2DeRhGeNI7VQU8inMwzWIHXVUoYV-rDV6PUNbktAKLXGikW1NSFesgj3FLwc84SGCaunqopXLGMmG5xME; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W58z5DgED7LN_GUCqTjaccW5JpX5KMhUgL.Fo-cSoqfeoM71h.2dJLoIEXLxKMLB.zL1hqLxKnL1h-LB.zLxKnL1h5L12eLxKBLB.eL1-qLxK-LBKBLBKMt; SUHB=0auAu1qcEtI8L_; H5_INDEX_TITLE=%E7%BB%86%E8%85%BB%E8%80%8C%E4%BC%9F%E5%A4%A7; H5_INDEX=0_all; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E7%2594%25B5%25E5%25BD%25B1%26fid%3D100103type%253D60%2526q%253D%25E7%2594%25B5%25E5%25BD%25B1%26uicode%3D10000011; WEIBOCN_FROM=1110006030',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    'X-Requested-With':'XMLHttpRequest'
}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xinlangweibo.middlewares.XinlangweiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xinlangweibo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xinlangweibo.pipelines.XlweiboPipeline': 300,
    'xinlangweibo.pipelines.MongoPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
