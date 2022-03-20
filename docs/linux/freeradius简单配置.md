
**1.安装freeradius**

```
sudo apt-get update
sudo apt-get install freeradius
```

2.**配置client.conf**

```
vim /etc/freeradius/client.conf
添加以下配置：
client 192.168.1.0/24 {
        secret          = 123123
        shortname      = test
}
即radius认证客户端的密码
```

3.**配置user**

```
vim /etc/freeradius/user
在大约90行修改：
"user" Cleartext-Password := "admin"
              Reply-Message = "Hello, %{User-Name}"
即用户名与密码
```

4.**生成证书使用EAP-TLS**

到目前配置，freeradius默认支持PAP, CHAP, MS-CHAPv1, MS-CHAPv2, PEAP, EAP-TTLS, EAP-GTC, EAP-MD5.认证方式

如果需要使用EAP-TLS需要先生成ca server client证书，这里用freeradius自带的工具生成

```
sudo apt-get install openssl
cd /usr/share/doc/freeradius/examples/certs
make
```

这里编译后只有CA Server证书

```
make client.pem
```

详细可阅读路径下README

```
rm /etc/freeradius/certs ca.pem dh server.key server.pem删除临时证书
cp ca.pem dh server.key server.pem /etc/freeradius/certs/复制刚刚生成的到配置里
chmod 777 ca.pem dh server.key server.pem
修改/etc/freeradius/eap.conf
第30行修改default_eap_type = tls
第295行注释make_cert_command = "${certdir}/bootstrap"
```

将/usr/share/doc/freeradius/examples/certs下client.p12拷贝至手机安装既可以使用EAP-TLS认证

**5.其它**

开启freeradius调试模式：freeradius XXX

安装证书的密码为whatever
