1. #### 安装syslog-ng

> apt-get install syslog-ng 安装syslog-ng

1. #### 配置syslog-ng

> vim /etc/syslog-ng/syslog-ng.conf
> 配置可以参考如下：



```
@version: 3.5
@include "scl.conf"
@include "`scl-root`/system/tty10.conf"
    options {
        time-reap(30);
        mark-freq(10);
        keep-hostname(yes);
        };
    source s_network {
        network(transport(tcp) port(515));
        };
    destination d_local {
    file("/var/log/syslog-ng/messages_${HOST}"); };
    destination d_logs {
        file(
            "/var/log/syslog-ng/logs.txt"
            owner("root")
            group("root")
            perm(0777)
            ); };
    log { source(s_network); destination(d_logs); };
```

这个配置文件是监听所有网络TCP 515端口的输出，如果想修改端口与协议可以直接在network(transport(tcp) port(515));修改。由于log记录会输出到/var/log/syslog-ng/logs.txt,所以需要创建目录和文件：

> mkdir /var/log/syslog-ng
> touch /var/log/syslog-ng/logs.txt

1. #### 启动syslog-ng

> /etc/init.d/syslog-ng restart

1. #### 追踪日志

> tail -f /var/log/syslog-ng/logs.txt