

####  

#### 一.ORM(对象关系映射)

ORM就是用实例对象的方法来操作关系型数据库，即:

- 数据库的表 --> 类（class）
- 表中的数据--> 对象（object）
- 字段（field）--> 对象的属性（attribute）

同理，Django中也是使用ORM将Django代码中的模型定义映射到底层数据库使用的数据结构:

- 每个模型都是一个 Python 的类，继承 django.db.models.Model,且映射一张数据库表``
- 模型类的实例对象就是一条条数据
- 模型类的每个属性都相当于一个数据库的字段
- 模型方法就是一些sql语句的封装



#### 二.基本操作流程

1.在app.models中创建模型

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

2.迁移数据模型至底层数据库

```
python manage.py makemigrations
python manage.py migrate
```

#### 三.字段
