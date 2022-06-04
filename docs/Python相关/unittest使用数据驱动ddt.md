

### 简介

ddt（data driven test）数据驱动测试：由外部数据集合来驱动测试用例,适用于测试方法不变，但需要大量变化的数据进行测试的情况，目的就是为了数据和测试步骤的分离

由于unittest没有数据驱动的模块，所以主要使用ddt这个库，安装如下

```
pip install ddt
```

ddt包含类的装饰器ddt和常用的三个方法装饰器data（直接输入测试数据），file_data（可以从json或者yaml中获取测试数据），unpack(分解数据)

### 使用

1.单独几个数据的时候

```
import unittest
import ddt

@ddt.ddt                          #在测试类定义之前使用：@ddt.ddt
class Mytest(unittest.TestCase):
    
    @ddt.data(1,2,3,4)       #在测试用例定义之前使用：@ddt.data（测试数据）测试数据之间用逗号隔开
    def test_1(self,a):
        print(a)

if __name__ == "__main__":
    unittest.main()
```

结果

```
1
.2
.3
.4
.
----------------------------------------------------------------------
Ran 4 tests in 0.013s

OK
```

2.数据组是列表的时候，拆分成单个元素

```
import unittest
import ddt

value = [(1,2),(3,4),(5,6)]

@ddt.ddt                          #在测试类定义之前使用：@ddt.ddt
class Mytest(unittest.TestCase):
    
    @ddt.data(*value)       #在测试用例定义之前使用：@ddt.data（测试数据），*就是python中参数分解，将列表分为一个个元素依次传入
    def test_1(self,a):
        print(a)

if __name__ == "__main__":
    unittest.main()
```

结果

```
(1, 2)
.(3, 4)
.(5, 6)
.
----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK
```

如果要将上面列表里面的元组分解成单个元素，使用unpack

```
import unittest
import ddt

value = [(1,2),(3,4),(5,6)]

@ddt.ddt                          #在测试类定义之前使用：@ddt.ddt
class Mytest(unittest.TestCase):
    
    @ddt.data(*value)       #在测试用例定义之前使用：@ddt.data（测试数据），*就是python中参数分解，将列表分为一个个元素依次传入
    @ddt.unpack     #单独取value中[1],分解成1，2传入
    def test_1(self,a,b):
        print(a,b)

if __name__ == "__main__":
    unittest.main()
```

结果

```
1 2
.3 4
.5 6
.
----------------------------------------------------------------------
Ran 3 tests in 0.010s

OK
```

3.数据组是字典的时候

```
import unittest
import ddt

value = {"a":1,"b":2}

@ddt.ddt
class Mytest(unittest.TestCase):

    @ddt.data(value)
    @ddt.unpack
    def test_1(self,a,b):
        print(a,b)

if __name__ == "__main__":
    unittest.main()
```

结果

```
1 2
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

4.使用json或yaml文件

json文件

```
{
    "test1":1,
    "test2":"abc",
    "test3":[1,2,3]
}
```

代码

```
import unittest
import ddt


@ddt.ddt
class Mytest(unittest.TestCase):

    @ddt.file_data("tmp.json")
    def test_1(self,a):
        print(a)

if __name__ == "__main__":
    unittest.main()
```

结果

```
1
.abc
.[1, 2, 3]
.
----------------------------------------------------------------------
Ran 3 tests in 0.014s

OK
```
