

嵩天老师一直强调的通用代码框架，这个框架可以用在很多爬虫中用来获取HTML文本，并且它通过response.raise_for_status()方法判断返回的状态码是不是200，如果不是，就会引发HTTPError异常，然后通过try except的异常处理获取到异常，而apparent_encoding则可以使得返回的编码准确。这样一个简单的通用代码框架可以有效的处理访问处理时遇到的网络问题。

```
def get_page(url):
    try:
        res = requests.get(url,timeout=10)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        print('错误')
        return ''
```

参考：[https://zhuanlan.zhihu.com/p/36478306](https://zhuanlan.zhihu.com/p/36478306)
