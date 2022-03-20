

按理讲，类属性改变，类的实例对象这个属性也应该被改变，但是在python中实际却不是这样

```
class test():
    name = 111

a = test()
b = test()

a.name = 222
test.name = 333
print(a.name,b.name,test.name)

输出:
222 333 333
```

这里a.name的值没有被test.name = 333改变

查看属性在内存中的位置

```
print(id(a.name))
print(id(b.name))
print(id(test.name))

输出:
140705896729248
2154539206672
2154539206672
```

再查看对象的属性

```
print(a.__dict__)
print(b.__dict__)
print(test.__dict__)

{'name': 222}
{}
{...'name': 333.....}
```

所以当操作a对象给name属性赋值时，创建了a的name属性，可以理解为这个name已经不是类的属性而是a对象的属性了（好绕）

所以类属性与实例属性查询的优先级为： 实例属性>类属性     实例属性没有是会去查类属性
