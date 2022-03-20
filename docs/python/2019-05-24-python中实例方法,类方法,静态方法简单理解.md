

按照字面名称来理解的话：

实例方法就是实例化对象的方法，绑定在实例对象上

类方法就是类自己的方法，不需要实例化对象，类自己就是对象，直接绑定在类上

静态方法就是普通的函数，函数作为对象，不过是封装在类的内部，通过类.方法引用

从参数上看：

实例方法默认参数是self

类方法默认参数是cls

静态方法可以没有

举个例子：

```
class Test():
    
    def a(self):
        print(self.a)

    @classmethod
    def b(cls):
        print(cls.b)

    @staticmethod
    def c():
        print(Test.c)
```

实例化一个对象

```
tmp = Test()
tmp.a()
tmp.b()
tmp.c()

输出:
<bound method Test.a of <__main__.Test object at 0x02145110>>
<bound method Test.b of <class '__main__.Test'>>
<function Test.c at 0x021424F8>
```

直接通过类去调用（以类本身为对象）

```
Test.a()
Test.b()
Test.c()

输出:
TypeError: a() missing 1 required positional argument: 'self'
<bound method Test.b of <class '__main__.Test'>>
<function Test.c at 0x021D24F8>
```

类自己实例化

```
print(Test())
print(Test)
Test().a()
Test().b()
Test().c()

输出
<__main__.Test object at 0x006E50B0>
<class '__main__.Test'>
<bound method Test.a of <__main__.Test object at 0x006E5790>>
<bound method Test.b of <class '__main__.Test'>>
<function Test.c at 0x006E24F8>

这里Test()与Test().a()在内存中对象不同，是因为一个是类对象，一个是实例方法对象
```

简单来说，@classmethod就是不用实例化，直接用类内部的方法；@staticmethod则是为封装类好看，为了满足强迫症，把方法装进类里面，实际大家都可以用
