

### unittest简介

Unittest是python内置的一个单元测试框架，主要用于自动化测试用例的开发与执行

简单的使用如下

```
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def tearDown(self):
        print("test end") 

if __name__ == '__main__':
    unittest.main()
```

- 1.导入unittest库
- 2.创建类继承TestCase类
- 3.以test开头的方法，就是实际执行的独立用例，必须要以test开头，因为是unittest中约定的
- 4.setUp()方法用于测试用例执行前的初始化工作，tearDown()方法用于用例执行完后的清理操作，这里用例指以test开头的方法，也就是每个test开头的方法执行前后都会调用这两个方法
- 5.assertEqual等是TestCase类断言的方法，实际就是简单的比较并抛出异常
- 6.main()方法提供了一个测试脚本的命令行接口，可以在脚本内直接运行

运行测试

```
1.使用命令行python -m unittest xxx脚本名

2.有unittest.main()就直接执行脚本

结果

----------------------------------------------------------------------
test start
test end
.test start
test end
.
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

### 主要结构

整体结构：unittest库提供了Test Case, Test Suite, Test Runner, Test Fixture

- Test Case:通过继承TestCase类，创建一个测试用例集，但这个测试用例集里面可能包含多个测试用例（或者测试步骤）即test开头的方法
- Test Suite:把多个测试用例集合在一起来执行。可以通过addTest加载TestCase到Test Suite中，从而返回一个TestSuite实例。
- Test Runner:Test Runner是一个用于执行和输出测试结果的组件，可以使用图形界面，文本界面，或者返回一个特殊的值的方式来表示测试执行的结果。
- Test Fixture:提供一些脚手架类的方法，常用于测试环境的设置与清理。

### 构建用例

构建用例的方法主要就是继承TestCase类，创建自己的测试类，然后用约定的test开头命名方法，这些方法就是测试用例

```
class TestStringMethods(unittest.TestCase):

    #用例以test开头
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
```

写用例的时候常使用断言，主要断言有以下:
|断言方法|检查条件
|assertEqual(a, b)|a == b
|assertNotEqual(a, b)|a != b
|assertTrue(x)|bool(x) is True
|assertFalse(x)|bool(x) is False
|assertIs(a, b)|a is b
|assertIsNot(a, b)|a is not b
|assertIsNone(x)|x is None
|assertIsNotNone(x)|x is not None
|assertIn(a, b)|a in b
|assertNotIn(a, b)|a not in b
|assertlsInstance(a, b)|isinstance(a, b)
|assertNotIsInstance(a, b)|not isinstance(a, b)

还有判断数据类型的断言：
|断言方法|用于比较的类型
|assertMultiLineEqual(a, b)|字符串(string)
|assertSequenceEqual(a, b)|序列(sequence)
|assertListEqual(a, b)|列表(list)
|assertTupleEqual(a, b)|元组(tuple)
|assertSetEqual(a, b)|集合(set 或 frozenset)
|assertDictEqual(a, b)|字典(dict)

官网还给了剩下其他的断言，比如异常,日志等，可以查看[https://docs.python.org/zh-cn/3/library/unittest.html](https://docs.python.org/zh-cn/3/library/unittest.html)

### 完善用例

**1.用例环境清理**

每个用例执行的时候需要独特的测试环境，可以在单独test方法中编写，但是每个用例执行前后的环境清理或统一的预处理，需要特殊的Test Fixture方法解决

主要使用这两种方法

- setUp()：程序会在运行每个测试用例（以 test_ 开头的方法）之前自动执行 setUp() 方法，该方法抛出的异常都视为error，而不是测试不通过。
- tearDown()：每个测试用例（以 test_ 开头的方法）运行完成之后自动执行 tearDown() 方法，该方法抛出的异常都视为error，而不是测试不通过，且无论用例是否出错都会调用。

```
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def tearDown(self):
        print("test end") 
```

**2.用例类的环境清理**

上面说的是每个测试用例（以 test_ 开头的方法）的环境清理，那么每个测试类（继承TestCase 的类）运行的时候怎么清理环境呢？

主要使用下面两个类方法

- setUpClass():一个类方法在单个类测试之前运行。setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器
- tearDownClass():一个类方法在单个类测试之后运行。setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器

```
class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("test start")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @classmethod
    def tearDownClass(self):
        print("test end") 
```

**3.模块级的环境清理**

运行多个测试的时候，可能会将一部分功能的测试类集中在一个文件中，对这一个文件级的环境清理主要使用下面两种方法

<li>
setUpModule()：模块开始时运行
</li>
<li>
tearDownModule()：模块结束时运行
</li>

```
./test.py

def setUpModule():  
    print('test module start')

def tearDownModule():  
    print("test module end")    

class Test1(unittest.TestCase):

    ...

class Test2(unittest.TestCase):

    ...
```

### 运行用例

**1.通过代码调用测试用例**

```
if __name__ == '__main__':
    unittest.main()
```

**2.命令行执行**

```
#运行测试文件
python -m unittest test_module

#测试单个测试类
python -m unittest test_module.test_class

#测试多个测试类
python -m unittest test_module.test_class test_module2.test_class2

#通配符匹配测试文件执行
python -m unittest -p test*.py 

#显示详细信息
python -m unittest -v test_module

#帮助
python -m unittest -h
```

**3.通过组织Test Suit后使用Test Runner运行Suite来运行测试**

组织Suite的方法很多，下面怎么组织Suite在管理用例中会介绍

```
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods("test_upper"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

### 管理用例

通过组织TestSuite可以管理多个测试用例的执行，然后使用Test Runner运行Suite来运行测试，主要用的对象有：

- TestSuit：组织测试用例的实例，支持测试用例的添加和删除，最终将传递给 testRunner进行测试执行；
- TextTestRunner：进行测试用例执行的实例，其中Text的意思是以文本形式显示测试结果。测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息；

**1.通过addTest()的方式**，上文中有

```
if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods("test_upper"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

**2.通过TestLoader()方式组织TestSuite**

```
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

class TestStringMethods2(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods2) 
    suite = unittest.TestSuite([suite1, suite2]) 
    unittest.TextTestRunner().run(suite)
```

**3.统一管理测试用例执行**，比如测试用例达到成百上千个，可以将这些用例按照所测试的功能进行拆分，分散到不同的测试文件中，最后再创建用于执行所有测试用例的runtest.py文件

比如有下面很多测试文件

```
├─test
│      test1.py
│      test2.py
│      test3.py
│      test4.py
│      tmp1.py
│      tmp2.py
        ...
```

如果我们只想执行test开头的测试文件，除了上文中的命令行命令外，我们还可以使用defaultTestLoader类提供的discover()方法来加载所有的测试用例

discover(start_dir,pattern='test*.py',top_level_dir=None)

找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才能被加载。如果启动的不是顶层目录，那么顶层目录必须单独指定。

- start_dir：要测试的模块名或测试用例目录路径
- pattern='test*.py'：表示用例文件名的匹配原则。此处匹配文件名以test开头的.py类型的文件，幸好*表示任意多个字符
- top_level_dir=None：测试模块的顶层目录，如果没有顶层目录，默认为None

注意：discover()方法中的start_dir只能加载当前目录下的.py文件，如果加载子目录下的.py文件，需在每个子目录下放一个_init_.py文件。

```
-runtest.py

import unittest

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
```

当然，如果用例少，也可以使用addTest()的方式一个个添加到TestSuite中

**4.跳过用例和预期失败**

unittest提供了实现某些需求的装饰器，在执行测试用例时每个装饰前面加@符号。

- unittest.skip(reason):无条件的跳过装饰的测试，说明跳过测试的原因
- unittest.skipIf(condition,reason)：跳过装饰的测试，如果条件为真。
- unittest.skipUnless(condition,reason):跳过装饰的测试，除非条件为真。
- unittest.expectedFailure():测试标记为失败，不管执行结果是否失败，统一标记为失败，但不会抛出错误信息。

```
class TestStringMethods(unittest.TestCase):

    @unittest.skip("not wht")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
```

**5.执行顺序**

unittest框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z,a-z。所以上文测试方法test_isupper()会比test_upper()先执行

同理测试类以及测试文件也是按照这个顺序执行，但如果你使用addTest()的方式添加了测试，会按照添加的顺序执行

### 测试结果

**1.console输出结果**

结果中有几个特殊字符表示不同的意思

- . ：代表测试通过。有几个点就表示有几个测试通过
- F：代表测试失败，F 代表 failure。
- E：代表测试出错，E 代表 error。
- s：代表跳过该测试，s 代表 skip。

**2.HTMLTestRunner输出测试报告**

HTMLTestRunner是一个第三方库用于替代TestRunner，用于生成可视化的报表，是python2时期的产物，现在python3需要修改其内容才能用，不过网上有改好的，可以直接用

使用就是将下载好的HTMLTestRunner.py复制到...\python35\Lib目录下，然后下面这样使用

```
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #HTMLTestRunner可以读取docstring类型的注释
        '''
        test1
        '''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':

    testsuite = unittest.TestSuite()
    testsuite.addTest(TestStringMethods("test_upper"))
    testsuite.addTest(TestStringMethods("test_isupper"))
    fp = open('./result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
    runner.run(testsuite)
    fp.close()
```

3.如果想打印log到测试报告可以看我另一篇文章[https://www.cnblogs.com/fengf233/p/10871055.html](https://www.cnblogs.com/fengf233/p/10871055.html)

参考:

[https://docs.python.org/zh-cn/3/library/unittest.html](https://docs.python.org/zh-cn/3/library/unittest.html)
