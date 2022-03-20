

### 1. Selectors选择器

在抓取网页时，您需要执行的最常见任务是从HTML源提取数据。有几个库可用于实现此目的，例如：

- BeautifulSoup是Python程序员中非常流行的Web抓取库，它基于HTML代码的结构构造Python对象，并且相当好地处理坏标记，但它有一个缺点：它很慢。
- lxml是一个XML解析库（也可以解析HTML），它使用基于ElementTree的pythonic API 。（lxml不是Python标准库的一部分。）

XPath是一种用于在XML文档中选择节点的语言，也可以与HTML一起使用。CSS是一种将样式应用于HTML文档的语言。它定义选择器以将这些样式与特定HTML元素相关联。

### 2. 选择器使用

1.通过response响应对象属性.selector构建选择器实例

```
response.selector.xpath('//span/text()').get()
```

使用XPath和CSS查询响应非常常见，响应包括另外两个快捷方式：response.xpath()和response.css()：

```
>>> response.xpath('//span/text()').get()
'good'
>>> response.css('span::text').get()
'good'
```

2.直接使用Selectors构建

从HTML文本构造

```
>>> from scrapy.selector import Selector
>>> body = '<html><body>good</body></html>'
>>> Selector(text=body).xpath('//span/text()').get()
'good'
```

从响应构造

```
>>> from scrapy.selector import Selector
>>> from scrapy.http import HtmlResponse
>>> response = HtmlResponse(url='http://example.com', body=body)
>>> Selector(response=response).xpath('//span/text()').get()
'good'
```

### 3. CSS选择器

基础选择器
<td valign="top" width="148">**选择器**</td><td valign="top" width="684">**含义**</td>
<td valign="top" width="148">*</td><td valign="top" width="684">通用元素选择器，匹配页面任何元素（这也就决定了我们很少使用）</td>
<td valign="top" width="148">#id</td><td valign="top" width="684">id选择器，匹配特定id的元素</td>
<td valign="top" width="148">.class</td><td valign="top" width="684">类选择器，匹配class**包含(不是等于)**特定类的元素</td>
<td valign="top" width="148">element</td><td valign="top" width="684">标签选择器 根据标签选择元素</td>
<td valign="top" width="148">[attr]</td><td valign="top" width="684">属性选择器 根据元素属性去选择</td>

组合选择器
<td valign="top" width="180">**选择器**</td><td valign="top" width="100">**<strong>示例**</strong></td><td valign="top" width="250">**<strong>示例说明**</strong></td><td valign="top" width="787">**含义**</td>
<td valign="top" width="180">elementE,elementF</td><td valign="top" width="100">div,p</td><td valign="top" width="250">选择所有元素和<p>元素</td><td valign="top" width="787">多元素选择器，用,分隔，同时匹配元素E或元素F</td>
<td valign="top" width="180">elementE elementF</td><td valign="top" width="100">div p</td><td valign="top" width="250">选择元素内的所有<p>元素</td><td valign="top" width="787">后代选择器，用空格分隔，匹配E元素所有的**后代（不只是子元素、子元素向下递归）**元素F</td>
<td valign="top" width="180">elementE>elementF</td><td valign="top" width="100">div>p</td><td valign="top" width="250">选择所有父级是  元素的 <p> 元素</td><td valign="top" width="787">子元素选择器，用>分隔，匹配E元素的所有直接子元素</td>
<td valign="top" width="180">elementE+elementF</td><td valign="top" width="100">div+p</td><td valign="top" width="250">选择所有紧接着元素之后的<p>元素</td><td valign="top" width="787">直接相邻选择器，匹配E元素**之后**的**相邻**的**同级**元素F</td>
<td valign="top" width="180">elementE~elementF</td><td valign="top" width="100">p~ul</td><td valign="top" width="250">选择p元素之后的每一个ul元素</td><td valign="top" width="787">普通相邻选择器，匹配E元素**之后**的**同级**元素F（无论直接相邻与否）</td>
<td valign="top" width="180">.class1.class2</td><td valign="top" width="100">.user.login</td><td valign="top" width="250">匹配如元素</td><td valign="top" width="787">匹配类名中既包含class1又包含class2的元素</td>

CSS选择器是前端的基础,以上只给了比较重要的内容，具体CSS选择器内容可以去w3school参考

**Scrapy中CSS选择器的拓展**

根据W3C标准，CSS选择器不支持选择文本节点或属性值。但是在Web抓取环境中选择这些是非常重要的，Scrapy（parsel）实现了一些非标准的伪元素

- 要选择文本节点，使用 `::text`
- 选择属性值，用`::attr(name) name`是指你想要的价值属性的名称

```
#没有用::text，对selectors对象使用get方法后，返回的是匹配的html元素

>>> response.css('title').get()
<title>Example website</title>

#使用::text就是返回标签内的文本

>>> response.css('title::text').get()
'Example website'

#<a href='image1.html'>Name: My image 1 <img src='image1_thumb.jpg' /></a> 使用a::attr(href)可以提取属性

>>>response.css('a::attr(href)').get()
'image1.html'
```

### 4. XPath

XPath，全称 XML Path Language，即 XML 路径语言，它是一门在XML文档中查找信息的语言。XPath 最初设计是用来搜寻XML文档的，但是它同样适用于 HTML 文档的搜索。

1.XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。 下面列出了最有用的路径表达式

举例如下

选取根元素 bookstore。

注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！

2.谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中。

3.选取未知节点

实例如下:

同样scrapy也给XPath拓展了方法，使用.//text()可以选择文本

摘自[https://www.w3school.com.cn/xpath/xpath_syntax.asp](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

### 5. .xpath()和.css()方法

**css(query)**

应用给定的CSS选择器并返回一个SelectorList实例。（SelectorList实例可以理解为Selector组成的list）

query 是一个包含要应用的CSS选择器的字符串。

在后台，CSS查询使用cssselect库和run .xpath()方法转换为XPath查询 。

```
>>> response.css("link")
[<Selector xpath='descendant-or-self::link' data='<link rel="alternate" type="text/html" h'>,
 <Selector xpath='descendant-or-self::link' data='<link rel="next" type="application/atom+'>,
 ...
```

**xpath(query, namespaces=None, **kwargs)**

查找与xpath匹配的节点query，并将结果作为SelectorList实例返回， 并将所有元素展平。List元素也实现了Selector接口。

query 是一个包含要应用的XPATH查询的字符串。

```
>>> response.xpath("//link")
[<Selector xpath='//link' data='<link rel="alternate" type="text/html" h'>,
 <Selector xpath='//link' data='<link rel="next" type="application/atom+'>,
 ...
```

**串联查询**

由于css()与xpath()方法返回SelectorList实例，并且SelectorList实例也有与Selector对象相同的方法(SelectorList实例的方法可以理解为list中所有Selector遍历执行)，所以可以在返回结果上继续查询

```
response.css(".quote").css("small")

#这个就是先查找出所有class=quote的元素，然后在这些元素中查找small标签元素
```

### 6. .get()与.getall()

**get()**

以unicode字符串返回第一个真实的数据，没有css xpath拓展方法（::text ::attr //text()），就返回匹配的html元素数据

**getall()**

以unicode字符串list返回所有数据，其它同get()一样

**默认返回值**

如果没有匹配到元素则返回None，但是可以提供默认返回值作为参数，以代替None

```
>>> response.xpath('//div[@id="not-exists"]/text()').get(default='not-found')
'not-found'
```

**.get() .getall()与extract() extract_first()**

### 7. Selector其他属性方法

**.attrib**

返回底层元素的属性字典

```
>>> response.css('img').attrib['src']
'image1_thumb.jpg'
```

**re(regex，replace_entities = True )**

```
>>> response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
['My image 1',
 'My image 2',
 'My image 3',
 'My image 4',
 'My image 5']
```
