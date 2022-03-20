### apt-get install 或 apt-get upgrade /dist-upgrade 离线升级方式

1.在一个可以联网的环境中，更新源

```shell
sudo sed -i s#//.*archive.ubuntu.com#//mirrors.aliyun.com# /etc/apt/sources.list  #换源
sudo apt-get update
```



2.再下载需要的deb包

使用```--print-uris```可以不安装，只打印deb url地址，然后通过下面处理到一个文本中

```apt-get -y install --print-uris package-name | cut -d\' -f2 | grep http:// > apturls```

```apt-get upgrade```一样

```sudo apt-get dist-upgrade -y --print-uris |cut -d\' -f2 | grep http:// > apturls```

然后使用wget下载

```sudo wget -i apturls```

或者

使用 

```
sudo apt-get dist-upgrade --download-only
sudo apt-get install --download-only  software
```

--download-only 会下载到```/var/cache/apt/archives```



3.最后将下载的deb包拷贝到未联网设备上安装

```sudo dpkg -i *.deb```