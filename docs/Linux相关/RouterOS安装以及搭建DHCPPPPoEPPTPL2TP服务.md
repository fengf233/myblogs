

**1.安装routeros**

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150556635-612734563.png" alt="" />

vdi格式 ：VirtualBox默认创建的硬盘文件格式

vmdk格式：VMware创建的虚拟硬盘文件格式

ova格式：开放虚拟化格式

这里我们使用virtual box来创建

下载ova镜像，选择ova文件，直接导入到vbox

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150636541-2002248717.png" alt="" />

导入完成后，在设置中更改网络。最好选择桥接两张不同的网卡，一个做WAN，一个做LAN

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150650523-1062672147.png" alt="" />

**2.配置routeros**

安装完成后进入命令行界面 默认账户admin 密码空

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150800708-1176902261.png" alt="" />

使用 interface set ether1 name=lan 来设置接口对应的名称，方便之后管理

可以使用interface print detail查看详细的接口信息

命令可以使用tab键补全

安上图设置好LAN WAN接口，需要确定LAN WAN对应实际的网卡是不是正确，请按照interface print detail里mac来查看

RouterOS命令行与cisco这些路由设备比较像，用/可以返回上一级命令

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150817096-101028448.png" alt="" />

然后使用ip address add address=192.168.10.1/24 interface=lan （IP只是例子）来设置lan接口的ip地址，

最好与PC同一个网段，用来访问RouterOS的管理界面,WAN的地址可以先不设置，或设置为外部的网络地址

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150852953-1729992574.png" alt="" />

以上基础的配置完成了，接下来进入管理界面配置

使用浏览器访问192.168.10.1或者使用官网的winbox访问192.168.10.1，这里直接使用网页访问

访问直接进入以下界面

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150917391-1912704144.png" alt="" />

用户名密码与命令行一样

在quick set里面可以设置RouterOS的网络，就像普通的路由器那样去设置就行

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515150936588-930455178.png" alt="" />

至此，routeros基本设置就完成了，下面介绍搭建使用ROS搭建DHCP PPPoe L2TP PPTP

**3.搭建DHCP**

在ip-pool中增加一个地址池

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151117773-1263928816.png" alt="" />

进入IP->DHCP Server，add new，添加一个DHCP server，interface选择lan，Address Pool选择刚刚建的DHCP Pool其他默认，APPLY OK

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151133543-420137512.png" alt="" />

进入IP->DHCP Server->Network，根据需求配置

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151148663-1226680903.png" alt="" />

到此步骤，DHCP服务就配置好了，在DHCP界面d或e控制dhcp开关

**4.搭建pppoe**

增加一个地址池，最好与LAN接口ip不同网段

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151301788-1573354684.png" alt="" />

添加PPPoE属性  进入PPP->Profiles，add new，配置如下，其余默认

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151313563-2115444145.png" alt="" />

进入PPPoE server配置服务器，配置如下，具体参数可自行设定

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151327543-703996847.png" alt="" />

进入secret配置PPPoE账户,密码pppoe

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151341021-1423593551.png" alt="" />

至此PPPoE服务器搭建完毕,router会虚拟出一个pppoe接口

**5.搭建PPTP L2TP server**

配置PPTP和L2TP与PPPoE配置方法相同，先各自建立一个地址池和账号

再添加配置Profiles

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151442275-362604707.png" alt="" />

配置server 在PPP  interface PPTP server

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151455388-2111878798.png" alt="" />

L2TP的配置如下:

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151517415-812068525.png" alt="" />

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151525563-987140781.png" alt="" />

搭建完如图

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151539733-620890029.png" alt="" />

**6.通过配置firewall来使PPPoe PPTP L2TP客户端来连接WAN端的外网**

**<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151626796-199347820.png" alt="" />**

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151633839-1946911929.png" alt="" />

配置后

<img src="2019-05-15-RouterOS安装以及搭建DHCPPPPoEPPTPL2TP服务.assets/1685507-20190515151646790-418507154.png" alt="" />
