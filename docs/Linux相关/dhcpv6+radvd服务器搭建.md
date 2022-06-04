

**1.isc-dhcp-server install**

```
sudo apt update

sudo apt-get install isc-dhcp-server
```

**2.设置dhcp**

创建/etc/dhcp/dhcpd6.conf文件，按以下内容自定义添加：

```
default-lease-time 600;
max-lease-time 7200; 
log-facility local7; 
subnet6 2001:db8:0:1::/64 {
        # Range for clients
        range6 2001:db8:0:1::129 2001:db8:0:1::254;

        # Range for clients requesting a temporary address
        range6 2001:db8:0:1::/64 temporary;

        # Additional options
        option dhcp6.name-servers fec0:0:0:1::1;
        option dhcp6.domain-search "domain.example";

        # Prefix range for delegation to sub-routers pd
        prefix6 2001:db8:0:100:: 2001:db8:0:f00:: /56;


}
```

创建

```
touch /var/lib/dhcp/dhcpd6.leases

chown dhcpd:dhcpd /var/lib/dhcp/dhcpd6.leases
```

**3.启动server：**

```
sudo dhcp -6 -f -cf /etc/dhcp/dhcpd6.conf eth0
```

**4.安装radvd**

```
sudo apt-install radvd
```

**5.配置radvd**

```
创建/etc/radvd.conf 并 chmod 777 /etc/radvd.conf
```

配置如下:

```
#log-level 8
#log-mode full
#stateless
interface eth0 {
   AdvSendAdvert on;
   MinRtrAdvInterval 30;
   MaxRtrAdvInterval 600;
   AdvManagedFlag on;                   #M bit=1
   AdvOtherConfigFlag on;               #O bit=1
   AdvLinkMTU 1500;
   AdvSourceLLAddress on;
   AdvDefaultPreference high;
   prefix 2001:db8:0:1::/64
   {
   AdvOnLink on;
   AdvAutonomous off;                   #A bit=0
   AdvRouterAddr on;
   AdvPreferredLifetime 3600;
   AdvValidLifetime 7200;
   }; 
route 2001:db8:0:1::/64 {
    };

};
```

启动radvd

```
radvd d C /etc/radvd.conf
```
