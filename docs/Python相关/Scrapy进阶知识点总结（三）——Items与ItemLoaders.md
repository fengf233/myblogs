

### 一.Items

抓取的主要目标是从非结构化源（通常是网页）中提取结构化数据。Scrapy蜘蛛可以像Python一样返回提取的数据。虽然方便和熟悉，但Python缺乏结构：很容易在字段名称中输入拼写错误或返回不一致的数据，尤其是在具有许多蜘蛛的较大项目中。

为了定义通用输出数据格式，Scrapy提供了Item类。 Item对象是用于收集数据的简单容器。它们提供类似字典的 API，并具有用于声明其可用字段的方便语法。

#### **1.定义Items**

```
./items.py

import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
```

类似于django的model，scrapy定义items也是继承scrapy.Item类，然后设置需要的字段，但是Item没有像django那样有许多不同类型的Field

注意:Field用于声明项目的对象不会保留为类属性，所以不能用item.attr去访问，但可以通过Item.fields属性访问它们

```
>>> item.fields
{'last_updated': {'serializer': <class 'str'>}, 'name': {}, 'price': {}, 'stock': {}, 'tags': {}}
```

#### 2.Field()类

Field对象指明了每个对象的元数据（metadata）。可以为每个字段指明任何类型的元数据。需要注意的是，用来声明item的Field对象并没有被赋值class的属性。不过可以通过Item.fields属性进行访问

查看Field()源码

```
class Field(dict):
    """Container of field metadata"""
```

所以实际上Field等同于dict，可以像last_updated那样在定义Items的时候，给字段一个元数据（这个元数据的作用主要是通过中间件时，给予特定的功能或处理，例如上面last_updated的序列化函数指定为str，可任意指定元数据，不过每种元数据对于不同的组件意义不一样）。并且只能Item.fields['serializer']这样访问，不能Item['last_updated']['serializer']，并且Item['last_updated']的赋值不影响元数据serializer值

总结就是：

1.Field对象指明了每个字段的元数据（任何元数据），Field对象接受的值没有任何限制

2.设置Field对象的主要目就是在一个地方定义好所有的元数据

3.声明item的Field对象，并没有被赋值成class属性。（可通过item.fields进行访问）

4.Field类仅是内置字典类（dict）的一个别名，并没有提供额外的方法和属性。被用来基于类属性的方法来支持item生命语法。

#### 3.使用Items

创建对象

```
>>> product = Product(name='Desktop PC', price=1000)
>>> print(product)
Product(name='Desktop PC', price=1000)
```

从项目创建dicts

```
>>> dict(product) # create a dict from all populated values
{'price': 1000, 'name': 'Desktop PC'}
```

从dicts创建项目

```
>>> Product({'name': 'Laptop PC', 'price': 1500})
Product(price=1500, name='Laptop PC')

>>> Product({'name': 'Laptop PC', 'lala': 1500}) # warning: unknown field in dict
Traceback (most recent call last):
    ...
KeyError: 'Product does not support field: lala'
```

获取字段值

```
#想字典一样取值
>>> product['name']
Desktop PC
>>> product.get('name')
Desktop PC
>>> product['price']
1000
#没有设置的字段无法取值
>>> product['last_updated']
Traceback (most recent call last):
    ...
KeyError: 'last_updated'
#没有获取到值可以设置个默认返回值
>>> product.get('last_updated', 'not set')
not set
#不能获取没有定义的字段
>>> product['lala'] # getting unknown field
Traceback (most recent call last):
    ...
KeyError: 'lala'

#判断key是否在item中
>>> 'name' in product  # is name field populated?
True

>>> 'last_updated' in product  # is last_updated populated?
False

>>> 'last_updated' in product.fields  # is last_updated a declared field?
True

>>> 'lala' in product.fields  # is lala a declared field?
False
```

设置字段值

```
>>> product['last_updated'] = 'today'
>>> product['last_updated']
today

>>> product['lala'] = 'test' # setting unknown field
Traceback (most recent call last):
    ...
KeyError: 'Product does not support field: lala'
```

字典API

```
>>> product.keys()
['price', 'name']

>>> product.items()
[('price', 1000), ('name', 'Desktop PC')]
```

子类拓展

```
#可以通过声明原始Item的子类来扩展Items
class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()

#可以使用先前的字段元数据扩展字段元数据，并附加更多值或更改现有值
class SpecificProduct(Product):
    name = scrapy.Field(Product.fields['name'], serializer=my_serializer)
```

### 二.Item Loaders

定义了Item，我们在爬虫的时候，可以使用字典的方式来填充我们抓取的数据（通过css xpath等方法）。同时scrap有也提供了一种方法，结合.css .xpath方法与item字典API来给Item输入数据，这就是item Loaders

从另一方面来说， Items 提供保存抓取数据的 容器 ， 而 Item Loaders提供的是 填充 容器的机制。

```
from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()
```

这是官网上的示例，实际上ItemLoader就是item字典api与response.css() /.xpath()方法的集合，不过item Loaders更加简便与统一。

#### 输入/输出处理器

每个Item Loader对每个Field都有一个输入处理器和一个输出处理器。输入处理器在数据被接受到时执行，当数据收集完后调用ItemLoader.load_item()时再执行输出处理器，返回最终结果。

```
l = ItemLoader(Product(), some_selector)
l.add_xpath('name', xpath1) # (1)
l.add_xpath('name', xpath2) # (2)
l.add_css('name', css) # (3)
l.add_value('name', 'test') # (4)
return l.load_item() # (5)
```

流程如下

1.xpath1中的数据被提取出来，然后传输到name字段的输入处理器中，在输入处理器处理完后生成结果放在Item Loader里面(这时候没有赋值给item)

2.xpath2数据被提取出来，然后传输给(1)中同样的输入处理器，因为它们都是name字段的处理器，然后处理结果被附加到(1)的结果后面

3.跟2一样

4.跟3一样，不过这次是直接的字面字符串值，先转换成一个单元素的可迭代对象再传给输入处理器

5.上面4步的数据被传输给name的输出处理器，将最终的结果赋值给name字段

注意：add_xpath()，add_css()或 add_value()方法不是输入处理器，而是提取数据传入到输入处理器的方法。如果没有定义输入处理器就是传入原值

#### 定义输入输出处理器

**1.自定义类**:示例如下，通过对ItemLoader继承来重写Loader，其中name_in与name_out表示name字段的输入与输出处理器，default_input_processor和default_input_processor.则是指定默认的处理器(而在ItemLoader源码中实际就是使用Identity()处理器)

```
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose(unicode.title)
    name_out = Join()

    price_in = MapCompose(unicode.strip)

    # ...
```

处理器也可以使用自定义的函数，如果要将普通函数用作处理器，请确保将其self作为第一个参数接收 

```
def lowercase_processor(self, values):
    for v in values:
        yield v.lower()

class MyItemLoader(ItemLoader):
    name_in = lowercase_processor
```

2.在Field定义中声明输入/输出处理器

```
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value

class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )
```

3.处理器的优先级

(1)在Item Loader中定义的field_in和field_out

(2)Filed元数据(input_processor和output_processor关键字)

(3)Item Loader中的默认的

4.内置的处理器

- **Identity() **最简单的处理器，它什么都不做。它返回原始值不变。它不接收任何构造函数参数，也不接受Loader上下文。
- **TakeFirst()** 从接收的值返回第一个非null /非空值，因此它通常用作单值字段的输出处理器。它不接收任何构造函数参数，也不接受Loader上下文。
- **Join(**separator = u' ' )**** 将结果连起来，默认使用空格' ',等同于u' '.join
- **Compose(*** functions**，**** default_loader_context **)** 将函数链接起来形成管道流，产生最后的输出
- **MapCompose(*** functions**，**** default_loader_context **)** 跟上面的Compose类似，区别在于内部结果在函数中的传递方式.它的输入值是可迭代的，首先将第一个函数依次作用于所有值，产生新的可迭代输入，作为第二个函数的输入，最后生成的结果连起来返回最终值，一般用在输入处理器中
- **SelectJmes(**json_path **)** 使用json路径来查询值并返回结果

#### Item Loader上下文

Item Loader Context是任意键/值的dict，它在Item Loader中的所有输入和输出处理器之间共享。它可以在声明，实例化或使用Item Loader时传递。它们用于修改输入/输出处理器的行为。

以上官网说的不是很清楚，查看源码其实可以知道，context是Item Loader类的一个属性(字典形式)，其记录传入Item Loader类任何数据，包括selector ，response ，item。可以通过loader.context访问，源码如下

```
class ItemLoader(object):

     ...

    def __init__(self, item=None, selector=None, response=None, parent=None, **context):
        if selector is None and response is not None:
            selector = self.default_selector_class(response)
        self.selector = selector
        #将selector与response传入context字典
        context.update(selector=selector, response=response)
        if item is None:
            item = self.default_item_class()
        self.context = context
        self.parent = parent
        #context添加item
        self._local_item = context['item'] = item
        self._local_values = defaultdict(list)

    ....
```

比如继续使用上面Product Item类来实验

```
>>> from scrapy.loader import ItemLoader
>>> l = ItemLoader(item=Product(),tmp='tmp')
>>> l
<scrapy.loader.ItemLoader object at 0x000000000388DD68>
>>> l.context
{'tmp': 'tmp', 'selector': None, 'response': None, 'item': {}}
>>> l.add_value('name','admin')
>>> l.add_value('price','1000')
>>> l.context
{'tmp': 'tmp', 'selector': None, 'response': None, 'item': {}}
>>> l.load_item()
{'name': ['admin'], 'price': ['1000']}
>>> l.context
{'tmp': 'tmp', 'selector': None, 'response': None, 'item': {'name': ['admin'], 'price': ['1000']}}
```

context的用途，比如一个接收文本值并从中提取长度的函数

```
def parse_length(text, loader_context):
    unit = loader_context.get('unit', 'm')
    # ... length parsing code goes here ...
    return parsed_length
```

通过接收一个loader_context参数，这个函数告诉Item Loader它能够接收Item Loader context。于是当函数被调用的时候Item Loader传递当前活动的context给它。并且处理器函数（这里是parse_length）可以使用它们。

然后可以在定义处理器时使用

```
class ProductLoader(ItemLoader):
    length_out = MapCompose(parse_length)
```

这个相当于在给length字段赋值时，通过处理器返回的是赋值的长度。注意的是只有在定义函数时接收loader_context这个特定的参数才会接收context

参考官方文档[https://docs.scrapy.org/en/latest/topics/loaders.html](https://docs.scrapy.org/en/latest/topics/loaders.html)
