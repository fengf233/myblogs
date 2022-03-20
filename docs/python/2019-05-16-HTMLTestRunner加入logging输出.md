

**使用HTMLTestRunner生成html的测试报告的时候，报告中只有console输出，logging的输出无法保存，**

**如果要在报告中加入每一个测试用例执行的logging信息，则需要改HTMLTestRunner的源码**

HTMLTestRunner原作者文件下载地址：[http://tungwaiyip.info/software/HTMLTestRunner.html](http://tungwaiyip.info/software/HTMLTestRunner.html)

这里使用findyou的美化版来做实验，github地址[https://github.com/findyou/HTMLTestRunnerCN/tree/dev](https://github.com/findyou/HTMLTestRunnerCN/tree/dev)

在HTMLTestReportCN.py 474行加入一个logger，可以自己传入一个logger，这里固定一个

```
class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        #增加一个测试通过率 --Findyou
        self.passrate=float(0)
        self.logger = logging.getLogger('mylog') 
```

在488行startTest函数中初始化logging.Handler，记录到内存中

```
def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        #----add logging output----fengf233
        self.log_cap = io.StringIO()
        self.ch = logging.StreamHandler(self.log_cap)
        self.ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(levelname)s][%(asctime)s] [%(filename)s]->[%(funcName)s] line:%(lineno)d ---> %(message)s')
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.ch)
```

在496行 complete_output函数的返回值中加入logging存在内存中的输出，用换行符隔开

```
def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        #add log out put ---fengf233
        return self.outputBuffer.getvalue()+'\n'+self.log_cap.getvalue()
```

每个用例执行完后，最好清除handler，在504行stopTest函数中加入

```
def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        a = self.complete_output()
        #清除log的handle---fengf233
        self.logger.removeHandler(self.ch)
        return a
```

使用这个方法也不用去改html的代码，集成在每个用例的a中返回，效果如下

<img src="https://img2018.cnblogs.com/blog/1685507/201905/1685507-20190515173513355-1383377672.png" alt="" width="669" height="304" />

每个用例都是单独logging记录，不会重复

HTMLTestReportCN.py 中输出是居中，觉得不好看，可以在414行中更改标签，增加style="text-align:left"属性

```

    <pre>
    %(script)s
    </pre>
    
```

**别忘了在最前面import logging**

最后只需要在你需要logging输出的文件位置加上logging就可以了，但是需要注意，这里我是使用mylog名称的logger，你创建的logger需要同名

所以这里HTMLTestRunner还有增加传入logger的提升空间，这里不做增加了

```
logger = logging.getLogger(logger=mylog)
```
