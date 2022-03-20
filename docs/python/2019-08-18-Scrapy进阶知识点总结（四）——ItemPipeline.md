

### Item Pipeline

Item Pipeline调用发生在Spider产生Item之后。当Spider解析完Response之后，Item就会传递到Item Pipeline，被定义的Item Pipeline组件会顺次调用，完成一连串的处理过程，比如数据清洗、存储等。

Item Pipeline的主要用途是:

<li>
清理HTML数据。
</li>
<li>
验证爬取数据，检查爬取字段。
</li>
<li>
查重并丢弃重复内容。
</li>
<li>
将爬取结果保存到数据库。
</li>

### Pipeline类

可以自定义管道类，但每个管道类必须实现以下方法:

**process_item(self, item, spider)**

参数:

<li>
**`item`**，是Item对象，即被处理的Item。
</li>
<li>
**`spider`**，是Spider对象，即生成该Item的Spider。
</li>

除了process_item()必须实现，管道类还有其它的方法实现:

1.**open_spider(spider)**

在Spider开启时被调用，主要做一些初始化操作，如连接数据库等。参数是即被开启的Spider对象

2.**close_spider(spider)**

在Spider关闭时被调用，主要做一些如关闭数据库连接等收尾性质的工作。参数spider就是被关闭的Spider对象

3.**from_crawler(cls,crawler)**

类方法，用@classmethod标识，是一种依赖注入的方式。它的参数是crawler，通过crawler对象，我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息，然后创建一个Pipeline实例。参数cls就是Class，最后返回一个Class实例。

**激活Item Pipeline组件**

要激活Item Pipeline组件，必须将其类添加到 ITEM_PIPELINES设置中，如下例所示

```
ITEM_PIPELINES = {
    'myproject.pipelines.Pipelineclass1': 300,
    'myproject.pipelines.Pipelineclass2': 800,
}
```

设置中为类分配的整数值决定了它们运行的​​顺序：项目从较低值到较高值类别。习惯上在0-1000范围内定义这些数字。

### 示例

#### 1.写入文件

```
import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
```

#### 2.存入mysql

```
import pymysql
class MySQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host='localhost',  # 数据库IP地址
            port=3306,  # 数据库端口
            db='dbname',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            )
        # 使用cursor()方法获取操作游标 
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        #编写insert sql语句，这里是数据库中已经有表了
        sql =  "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME) VALUES ('%s', '%s')" %(item['F_name'],item['L_name'])
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交sql语句
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        # 返回item
        return item 
        
    def close_spider(self, spider):
        self.db.close()
```

#### 3.存入mongodb

```
import pymongo
class MongodbPipeline(object):

    def __init__(self):
        # 建立MongoDB数据库连接
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        # 连接所需数据库
        self.db = self.client['scrapy']
        # 连接集合（表）
        self.coll = self.db['collection_name']

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert_one(postItem)  # 向数据库插入一条记录
        return item 
        
    def close_spider(self, spider):
        self.client.close()
```

#### 4.from_crawler()实例

```
class MongoPipeline(object):
    collection_name = 'xxx'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            #从crawler setting中获取配置
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        postItem = dict(item) 
        self.db[self.collection_name].insert(postItem) 
        return item
```
