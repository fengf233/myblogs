

###  

### 一.常见命令

```
全局命令：                项目命令：
startproject             crawl
genspider                check
settings                 list
runspider                edit
shell                    parse
fetch                    bench
view
version
```

1.创建项目

```
scrapy startproject <project_name> [project_dir]

示例: scrapy startproject douban
```

2.在项目中创建spiders

```
scrapy genspider [-t template] <name> <domain>

示例: scrapy genspider douban www.douban.com

<name>是spiders名字
<domain>是所爬取网站域名，文件中会根据这个生成allowed_domains和start_urls
[-t template]可以根据模板来创建，有basic crawl  csvfeed xmlfeed等
```

3.启动爬虫

```
scrapy crawl <spider>

-o 可以指定输出格式
--nolog 可以关闭打印log
```

4.查看所有爬虫

```
scrapy list
```

5.打印响应

```
scrapy fetch <url>

--nolog 不打印log 只显示content
--headers 打印响应头部
```

6.调试shell

```
scrapy shell [url]

进入命令行调试，可以使用response.css xpath这些方法来检测数据，打印源码等
```

7.显示项目的设置

```
scrapy settings --get BOT_NAME

BOT_NAME默认为项目名，可以在settings.py改
```

8.不创建项目运行spiders

```
scrapy runspider <spider_file.py>
```

### 二.Spider类

```
name  #爬虫名称，是定义Spider名字的字符串，在项目中唯一

allowed_domains  #允许爬取的域名，是可选配置，不在此范围的链接不会被跟进爬取

start_urls  #起始URL列表，没有实现start_requests()方法时，默认会从这个列表开始抓取

custom_settings  #spider专属设置，会覆盖全局设置

crawler  #crawler对象与spider的绑定，代表的是本Spider类对应的Crawler对象(有点懵的东西)

setttings  #运行此蜘蛛的配置。这是一个 Settings实例

logger  #指定Spider创建的Python logger name。可以使用它来发送日志消息
```

2.类方法

```
from_crawler(cls, crawler, *args, **kwargs)
#类方法，用于实例化某个对象（中间件，模块），将之绑定到spider类上

start_requests(self)
#生成器，返回由 URL 构造的 Request，作为入口在爬虫启动时自动运行。实现了本方法，则忽略start_urls。当然，方法内使用start_urls另说。

parse(self, response)
#默认 Response 解析函数（request默认回调函数）,此方法以及任何其他Request回调必须返回可迭代的Request和/或dicts或Item对象

closed(self, reason)
#爬虫关闭时自动运行，实现了spider_closed信号绑定
```

### 三.request对象

scrapy使用内置的scrapy.http.Request与Response对象去请求网络资源与响应的处理

**PS :在我们写spider的时候，主要是import scrapy， 然后Spider类与request类的引用路径则是scrapy.Spider与scrapy.Request。与我们在官网看见的文档不同，这是因为在源码scrapy/__init__.py中**

**增加了缩写**

```
scrapy/__init__.py

# Declare top-level shortcuts
from scrapy.spiders import Spider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from scrapy.item import Item, Field
```

#### Request对象

参数解析

```
url( string )  #请求的URL

callback  #回调函数，请求下载完成后，调用的方法，response对象为第一参数

method（string） #请求的HTTP方法。默认为'GET'

meta（dict） #元数据，表示要携带或者传递的信息，可用户自定义从Request到Response传递参数，这个参数一般也可在middlewares中处理

body（str或unicode）#请求主体body，就是HTTP报文请求头后面的内容

headers（dict）#请求头，字典格式

cookie（dict或list） #cookie，字典或者多个字典的list

encoding（string）#编码，默认utf-8

priority（int）#请求的优先级（默认为0）。调度器使用优先级来定义用于处理请求的顺序。具有较高优先级值的请求将较早执行。允许负值以指示相对低优先级

dont_filter（boolean）#如果需要多次提交表单，且url一样，那么就必须设置参数dont_filter = True，防止被当成重复网页过滤掉了,默认false

errback（callable）#在处理请求时引发任何异常时将调用的函数

flags（list）#发送到请求的标志，可用于日志记录或类似目的

cb_kwargs（dict）#一个带有任意数据的字典，它将作为关键字参数传递给Request的回调。
```

属性与方法

```
url  #请求url

method  #请求方法

headers  #请求头，字典类型

body  #请求主体str

meta  #可用户自定义从Request到Response传递参数，这个参数一般也可在middlewares中处理

cb_kwargs  #与参数一样

copy（） #返回副本

replace （参数） #替换对应参数，返回新的request
```

#### FormRequest对象

FormRequest类扩展了基础Request，具有处理HTML表单的功能,比Request增加formdata参数

1. **scrapy.http.FormRequest（url [，formdata，... ] ）**

```
formdata（元组的dict或iterable） #是包含HTML表单数据的字典（或（key，value）元组的可迭代的），它将被url编码并分配给请求的主体。
```

模拟表单POST发送，formdata的 参数值 value 必须是unicode , str 或者 bytes object，不能是整数

```
return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name': 'John Doe', 'age': '27'},
                    callback=self.after_post)]
```

2. **from_response()方法**

网站通常通过<input type =hidden>元素提供预先填充的表单字段，例如会话相关数据或身份验证令牌（用于登录页面）。 在抓取时，希望自动预先填充这些字段，并仅覆盖其中的一些字段，例如用户名和密码。 可以使用FormRequest.from_response（）方法，示例如下

```
import scrapy

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
```

如果想要请求的界面HTML中有表单信息 表单元素from_response()方法就可以自动识别里面的表单，并将参数传入表单

但实际from_response()能做的，FormRequest也能做，建议用FormRequest

#### JSONRequest对象

JSONRequest类增加了两个新的参数构造函数。其余参数与Request类相同。使用JSONRequest将设置Content-Type标头application/json 和Accept标头application/json, text/javascript, */*; q=0.01

```
data（JSON可序列化对象） #是任何需要JSON编码并分配给body的JSON可序列化对象。如果Request.body提供了参数，则将忽略此参数。如果Request.body未提供参数且提供的数据参数Request.method将'POST'自动设置。

dumps_kwargs（dict） #将传递给基础json.dumps方法的参数，该方法用于将数据序列化为JSON格式。
```

示例

```
data = {
    'name1': 'value1',
    'name2': 'value2',
}
yield JSONRequest(url='http://www.example.com/post/action', data=data)
```

### 四.Response对象

Response类用于http下载返回信息的类，它有几个子类：TextResponse 、 HtmlResponse 、 XmlResponse。关系如下：

```
Response　-TextResponse
　　 -HtmlResponse
　　 -XmlResponse
```

一般情况下，当一个页面下载完成时，下载器依据HTTP响应头部中的Content-Type信息创建某个Response的子类对象，通常一般是HtmlResponse子类，并通过response的形参传入request的回调函数进行我们的提取数据操作

#### Response基类

**scrapy.http.Response（url [，status = 200，headers = None，body = b''，flags = None，request = None ] ）**

参数与request对象差不多，而且使用Response属性与方法较多，这里省略参数，具体可以官网查看[https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request)

对象属性

```
url #响应的url字符串，(不一定是请求的地址，需考虑重定向)

status  #响应的HTTP状态的整数。示例：200， 404

headers  #响应头，字典类型，若要获取特定的值用get('keyname') getlist('keyname')；get('keyname') ： 获取指定key的第一个value值 返回str；getlist('keyname') ： 获取指定key的所有value值 返回list

body  #响应正文，字节对象

request #返回请求此响应的Request对象

meta #元数据,可以获取Request.meta中的数据。可以理解meta就是一个中继数据

flags #包含此响应标志的列表
```

对象方法

```
copy（） #返回一个新的Response，它是此Response的副本

replace（[ url，status，headers，body，request，flags，cls ] ）  #返回替换了对应参数的新对象

urljoin（url ） #通过将Response url与可能的相对URL 组合来构造绝对URL

follow(url, callback=None, method='GET', headers=None, body=None, cookies=None, meta=None, encoding='utf-8', priority=0, dont_filter=False, errback=None, cb_kwargs=None)  #可以接收url或相对url的Request请求方法。常用于下一页请求。
```

#### TextResponse对象

TextResponse主要继承于基类Response，并且新加了一些方法的实现，以及新的对象属性

**class scrapy.http.TextResponse（url [，encoding [，... ] ] ）**

属性

```
text  #响应文本，与response.body.decode(response.encoding)类似，但是text更方便

encoding  #HTTP 响应正文的编码，它的值可能是从HTTP响应头部或正文中解析出来的

selector  #Selector 对象用于在Response 中提取数据
```

在基类新增的方法

```
xpath(query)  #使用XPath选择器在Response中提取数据；它是 response.selector.xpath 方法的快捷方式

css(query)  #使用 CSS选择器在Response中提取数据；它是 response.selector.css方法的快捷方式。
```

#### HtmlResponse与XmlResponse

HtmlResponse和XmlResponse在源码实现上就是继承了TextResponse，目前与TextResponse没有区别
