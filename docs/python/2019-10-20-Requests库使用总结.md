

### 概述

Requests是python中一个很Pythonic的HTTP库，用于构建HTTP请求与解析响应

Requests开发哲学

- Beautiful is better than ugly.(美丽优于丑陋)
- Explicit is better than implicit.(直白优于含蓄)
- Simple is better than complex.(简单优于复杂)
- Complex is better than complicated.(复杂优于繁琐)
- Readability counts.(可读性很重要)

### 安装

直接安装

```
pip install requests
```

### 简单上手

**导入模块**

```
import requests
```

**发送请求**

```
#get
r = requests.get('http://httpbin.org/get')

#post
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```

通过requests.get或post方法实际发出一个http请求，返回一个response对象，[http://httpbin.org](http://httpbin.org/)是一个可以测试http请求的网站

**处理响应**

```
r.text  #返回响应内容主体，Requests 会自动解码来自服务器的内容

r.content  #返回二进制的响应内容主体

r.json() #处理json的响应内容，返回解码后的dict
```

### 构造请求

Requests中requests.get或post这些方法实际都是通过**requests.request(method, url, **kwargs)**实现的，主要返回response对象，下面主要介绍这个方法的参数

```
method -- Request对象的请求方法.
url -- 请求的URL.
params -- (可选) 请求的URL查询字符串中要发送的字典或字节.
data -- (可选) 字典或者元组列表[(key, value)] (form-encoded), 字节, 或者文件对象包含在请求主体中发生，主要是post put使用.
json -- (可选) 包含请求主体中的json数据.
headers -- (可选) HTTP首部(请求/通用/实体首部)，字典形式.
cookies -- (可选) Dict 或者 CookieJar对象包含在首部cookie字段发送.
files -- (可选) 名称：类文件对象（或{名称：file-tuple}）的字典，用于分段编码上传。 file-tuple可以是2元组（ filename，fileobj），3元组（ filename，fileobj， content_type）或4元组（ filename，fileobj， content_type，custom_headers）， 其中， content-type是一个字符串，用于定义给定文件的内容类型，而custom_headers是一个类似dict的对象，其中包含要为该文件添加的其他标题。
auth -- (可选)  用于Basic/Digest/Custom HTTP 认证，元组类型.
timeout (float or tuple) -- (可选)超时时间，在放弃请求之前，等待服务器发送数据的秒数，以浮点数或（连接超时，读取超时）元组为单位.
allow_redirects (bool) -- (可选)布尔值。 启用/禁用GET / OPTIONS / POST / PUT / PATCH / DELETE / HEAD重定向。 默认为True。
proxies -- (可选)字典，代理设置
verify -- (可选)布尔值（在这种情况下，它控制我们是否验证服务器的TLS证书）或字符串（在这种情况下，它必须是要使用的CA捆绑包的路径）。 默认为True。
stream -- (可选) 如果为False，则将立即下载响应内容。
cert -- (可选) 如果为String，则为ssl客户端证书文件（.pem）的路径。 如果是元组，则（证书，密钥）配对。
```

#### GET请求 

**requests.get(url, params=None, **kwargs)**等价于**requests.request('get', url, <strong>params=None,****kwargs)，****kwargs**</strong>即上面支持的可选参数

```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

#即向http://httpbin.org/get?key2=value2&key1=value1请求
```

#### POST请求

**requests.post(url, data=None, json=None, **kwargs)**等价于**requests.request('post', <strong>url, data=None, json=None, **kwargs**)**，<strong>**kwargs**</strong>即上面支持的可选参数</strong>

- application/x-www-form-urlencoded ：最常见post提交数据的方式，以form表单形式提交数据。
- application/json ：以json串提交数据。
- multipart/form-data ：一般使用来上传文件。

```
#application/x-www-form-urlencoded，一般form提交

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)

#application/json，如果使用 json 参数直接传递dict，就会被自动编码等同于json.dumps(payload)。如果使用data参数传递json.dumps(payload)，与json参数不同在于前者有Content-Type，后者无

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", json=payload)

#multipart/form-data 传文件

url = 'http://httpbin.org/post'

files = {'file': open('report.xls', 'rb')}

r = requests.post(url, files=files)
```

#### 定制请求头

如果想为请求添加 HTTP 头部，只要简单地传递一个 dict 给 headers 参数就可以了

```
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get('http://httpbin.org/get', headers=headers)
```

注意的是如果headers中包含Cookie会覆盖使用cookies参数时传入的dict

#### 传入Cookie

直接将字典类型的cookies传入到cookies参数即可

```
cookies = dict(cookies_are='working')

r = requests.get('http://httpbin.org/get',cookies=cookies)
```

### 处理响应

requests方法返回一个response对象

#### 响应内容主体

```
r = requests.get('http://httpbin.org/get')

r.text  #返回响应内容主体，Requests 会自动解码来自服务器的内容

r.content  #返回二进制的响应内容主体

r.json() #处理json的响应内容，返回解码后的dict
```

注意：有的中文网站使用r.text时，返回的内容为乱码，实际是自动解码错误了，解决办法主要有

```
#先返回二进制内容，再根据实际的编码解码

r.content.decode("utf-8")

#不知道具体编码形式时，可以使用下面方法自动解码

r.encoding = r.apparent_encoding

r.text
```

#### 获取响应头部

1.响应头部信息

```
r.headers
```

2.获取此响应的原始请求的头部

```
r.request.headers
```

#### 响应状态

1.返回状态码

```
r.status_code
```

2.响应是400或500类就抛出HTTPError异常

```
r.raise_for_status()
```

3返回状态原因

```
r.reason
```

#### 响应内容编码

```
r.encoding     #从HTTP报文header中猜测的响应内容的编码方式

r.apparent_encoding  #从内容中分析响应内容的编码方式(备选编码方式，一般从html<meta>标签中属性charset获取)
```

需要注意的是

- r.encoding:如果header中不存在charset,则认为编码是ISO-8859-1
- r.text根据r.encoding显示网页内容
- r.apparent_encoding:根据网页内容分析处的编码方式可以看做是r.encoding的备选

#### 其它方法与属性

response对象其它的方法与属性参考，具体可以查看官网地址[http://cn.python-requests.org/zh_CN/latest/api.html#requests.Response](http://cn.python-requests.org/zh_CN/latest/api.html#requests.Response)

- apparent_encoding：由html chardet属性表示的编码
- close()：关闭连接，一般不用
- content：二进制内容主体
- cookies：返回CookieJar对象
- elapsed：从发送请求到响应到达之间经过的时间
- encoding：决定.text的编码，从头部获取
- headers：响应的头部信息，以字典形式
- history：是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。主要用在重定向中
- is_permanent_redirect：如果此响应是重定向的永久版本之一，则为True。
- is_redirect：如果此响应是自动处理后格式正确的HTTP重定向，则为true
- links：返回响应的已解析头链接（如果有）。
- ok：如果status_code小于400，则返回True。
- request：这个响应的原始request对象
- url：响应的最终URL

### 会话对象

有时候可能需要多个请求才能完成任务的情况，比如模拟登录后的请求操作，如果单独用requests去请求的话，就需要将最初的请求响应的cookie或header保存下来并且在后面的请求中都加入，这样比较麻烦。

所以requests提供了个Session对象，用来让你能够跨请求保持某些参数，它也会在同一个 Session 实例发出的所有请求之间保持 cookie，并且向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。

1.跨请求保持一些 cookie

```
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```

2.属性的合并

```
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
```

注意的是，只有对象属性才能合并，方法层的参数覆盖则会覆盖

```
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'
```

3.前后文管理器

```
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
```

这样就能确保with区块退出后会话能被关闭，即使发生了异常也一样

参考:[http://cn.python-requests.org/zh_CN/latest/](http://cn.python-requests.org/zh_CN/latest/)
