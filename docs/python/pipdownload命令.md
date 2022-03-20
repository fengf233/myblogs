pip`download`命令可让您下载软件包而不安装它们：

```
pip download -r requirements.txt
```

（在以前的pip版本中，这是拼写的`pip install --download -r requirements.txt`。）

然后，您可以使用它们`pip install --no-index --find-links /path/to/download/dir/ -r requirements.txt`来安装那些下载的sdist，而无需访问网络。

