

### 1.设置优先级

- 1.命令行命令中指定的设置
- 2.每个spider中的设置
- 3.scrapy项目中settings.py设置
- 4.命令行命令的默认设置
- 5.scrapy全局的默认设置

1.命令行命令中指定的设置

命令行提供的参数是最优先的参数，覆盖任何其他选项

```
scrapy crawl myspider -s LOG_FILE=scrapy.log
```

2.每个spider中的设置

```
class MySpider(scrapy.Spider):
    name = 'myspider'

    custom_settings = {
        'SOME_SETTING': 'some value',
    }
```

3.scrapy项目中settings.py设置

通过project.settings中修改，下面有详细的配置解释

4.命令行命令的默认设置

每个Scrapy工具命令都可以有自己的默认设置，这些设置会覆盖全局默认设置。这些自定义命令设置default_settings在命令类的属性中指定。

5.scrapy全局的默认设置

全局默认值位于scrapy.settings.default_settings 模块中

### 2.settings设置

#### BOT_NAME

此Scrapy项目名称。这将默认用于构建User-Agent，也用于日志记录。使用该startproject命令创建项目时，它会自动填充项目名称

#### SPIDER_MODULES

#### NEWSPIDER_MODULE

指定使用genspider时创建spider的路径

#### USER_AGENT

爬虫时使用的默认User-Agent，除非被覆盖。默认： `"Scrapy/VERSION (+https://scrapy.org)"`

#### ROBOTSTXT_OBEY

#### CONCURRENT_REQUESTS

#### DOWNLOAD_DELAY

#### CONCURRENT_REQUESTS_PER_DOMAIN

#### CONCURRENT_REQUESTS_PER_IP

#### COOKIES_ENABLED

#### TELNETCONSOLE_ENABLED

#### DEFAULT_REQUEST_HEADERS

#### SPIDER_MIDDLEWARES

#### DOWNLOADER_MIDDLEWARES

#### EXTENSIONS

#### ITEM_PIPELINES

#### AUTOTHROTTLE_ENABLED

#### AUTOTHROTTLE_START_DELAY

#### AUTOTHROTTLE_MAX_DELAY

#### AUTOTHROTTLE_TARGET_CONCURRENCY

#### AUTOTHROTTLE_DEBUG

#### HTTPCACHE_ENABLED

#### HTTPCACHE_EXPIRATION_SECS

#### HTTPCACHE_DIR

#### HTTPCACHE_IGNORE_HTTP_CODES

#### HTTPCACHE_STORAGE

### 3.访问setting

在spider中通过self.settings获取

```
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://example.com']

    def parse(self, response):
        print("Existing settings: %s" % self.settings.attributes.keys())
```

通过from_crawler类方法获取scrapy.crawler.Crawler.settings 中的属性

```
class MyExtension(object):
    def __init__(self, log_is_enabled=False):
        if log_is_enabled:
            print("log is enabled!")

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.getbool('LOG_ENABLED'))
```

可以在spider类、middleware类、pipeline类以及extension使用from_crawler方法

### 4.总结

1.settings.py中的设置是针对整个项目的，可以添加对整个spiders通用的设置

2.custom_settings是spider单独的设置，比如可以设置每个spider用不同的中间件或管道

3.命令行中的设置，最高的优先级，应用场景比如，cmd多开的时候使用不同配置去跑spider，不过一些配置可能会出问题
