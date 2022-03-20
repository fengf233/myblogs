

### 概述

与request不同的是，request是单独请求一个http，而selenium则是以浏览器方式加载整个页面流，所以那些异步的请求也不用像request一样去分析接口，一切都像浏览器一样，所见即所得。

优点是：

1.所见即所得，不用考虑cookie，ajax，重定向等等，方便数据的查取

2.平时在我们在浏览器上做的操作（鼠标，浏览器操作等），基本都可以用这个实现，并且步骤动态可视

3.多平台支持，不仅语言多平台支持，支持浏览器driver也很多

缺点是：

1.慢，由于加载了整个页面的数据流，资源开销大，所以对于只想获取关键数据来说肯定没有请求接口来的快

2.不稳定，脚本维护成本高等，比如你用xpath去找元素，但是前端改其他问题影响到了你这个元素的路径，那么这个脚本就gg

主要作用：

1.用于前端自动化测试，总的来说算集成测试，更关注用户端的测试

2.模拟登录等，爬虫的模拟登录常用到，同时使用这种时要开开发者模式，因为已经有很多网站能识别了

3.个人办公用途，减少重复劳动力。举个栗子：百度云离线下载多个链接

### 安装

库安装

```
pip install selenium
```

WebDriver安装

WebDriver是W3C的一个标准，由Selenium主持，主要目的就是通过这套WebDriverAPI控制你电脑上的浏览器，相当于一个selenium与浏览器之间的驱动，需要注意的是，不同浏览器，需要安装不同的WebDriver，常见的如下
|Firefox浏览器|[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
|Chrome浏览器|[https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
|IE浏览器|[http://selenium-release.storage.googleapis.com/index.html](http://selenium-release.storage.googleapis.com/index.html)
|Edge浏览器|[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
|Opera浏览器|[https://github.com/operasoftware/operachromiumdriver/releases](https://github.com/operasoftware/operachromiumdriver/releases)
|PhantomJS浏览器|[https://phantomjs.org/](https://phantomjs.org/)

其中PhantomJS是一个无窗口的WebDriver，现在已经停更了

根据你电脑所装浏览器版本来安装WebDriver（至少需要大版本相同，不然会有一些问题），安装WebDriver很简单，将可执行文件放到脚本目录或者python安装目录即可

### WebDriver

#### 创建WebDriver对象

创建WebDriver对象，相当于启动了浏览器

```
#导入webdriver模块
from selenium import webdriver

#创建对象，根据你选择的浏览器创建

driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Ie()
driver = webdriver.Edge()
driver = webdriver.Opera()
driver = webdriver.PhantomJS()
```

#### WebDriver对象操作

对WebDriver对象的操作可以抽象成你怎么去控制浏览器，主要方法有：

1.访问URL

```
driver.get("http://www.python.org")
```

2.窗口大小调整

```
#设置宽800px 高600px
driver.set_window_size(800,600)

#设置最大，最小
driver.maximize_window()
driver.minimize_window()
```

3.刷新页面

```
driver.refresh()
```

4.前进后退

```
driver.forward()
driver.back()
```

5.关闭浏览器或窗口

```
#关闭浏览器
driver.quit()
#关闭窗口
driver.close()
```

6.返回当前的一些属性

```
#当前url
driver.current_url
#返回窗口句柄
driver.current_window_handle  #当前
driver.window_handles #所有
#返回title
driver.title
```

7.查找元素，返回Element对象，之后会详细讲

```
find_element_by_name()
find_element_by_id()
find_element_by_xpath()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_tag_name()
find_element_by_class_name()
find_element_by_css_selector()
```

8.切换窗口

```
driver.switch_to_window(handle)
```

9.切换frame

```
#切换框架,直接输入iframe的name或id属性，或者传入定位的元素
driver.switch_to_frame(frame_reference)
```

10.截图保持为文件

```
#img_path_name为文件路径，只支持.png格式，文件名注意带上后缀，如/Screenshots/foo.png
driver.get_screenshot_as_file(img_path_name)
```

11.执行js

```
#简单执行
driver.execute_script(script, *args)
    -script：要执行的JavaScript。
    -*args：JavaScript的所有适用参数。

#异步执行
driver.execute_async_script(script, *args)
```

12.操作cookie

```
#获取cookies
driver.get_cookies()

#添加cookie
driver.add_cookie(cookie_dict) 

#删除cookie
driver.delete_all_cookies()  #所有
driver.delete_cookie(name) #一个，指明key
```

### 元素Element

#### 查找元素Element

在我们使用driver.get(url)方法后，driver会加载整个页面，如果我们要操作比如点击页面中的某个元素，则首先需要定位到这个元素，再进行操作

注意的是这部分需要HTML CSS XPATH基础，不熟悉的可以查看W3C教程，这里不做多诉

示例

```
<html>
 <body>
  <h1>Welcome</h1>
  <p class="content">Site content goes here.</p>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
  </form>
  <a href="continue.html">Continue</a>
</body>
<html>
```

1.通过id属性定位

```
driver.find_element_by_id(loginForm)

#定位<form id="loginForm">
```

2.通过name属性定位

```
driver.find_element_by_name(username)

#定位<input name="username" type="text" />
```

3.通过class名定位

```
driver.find_elements_by_class_name(content)

#定位<p class="content">Site content goes here.</p>
```

4.通过TagName标签名定位

```
driver.find_element_by_tag_name(input)

#定位<input name="username" type="text" />，如果匹配了多个，只选第一个
```

5.通过link text定位，就是通过a标签的text内容定位

```
driver.find_elements_by_link_text(Continue) #全匹配 
driver.find_element_by_partial_link_text(Cont) #部分text匹配

#定位<a href="continue.html">Continue</a>
```

6.通过xpath定位

```
driver.find_element_by_xpath("//from[input/@name='username']")

#定位<input name="username" type="text" />
```

7.通过css选择器定位

```
driver.find_element_by_css_selector('p.content')

#定位<p class="content">Site content goes here.</p>
```

8.定位多个元素

将1~7中的**find_element_by_xxx**改成**find_elements_by_xxx**则可以返回所有匹配的元素为list

```
driver.find_elements_by_tag_name(input)

定位[<input name="username" type="text" />
   <input name="password" type="password" />]
```

9.串联查找

Element对象也是有find_element_by_xxx这些方法的，所以可以在第一次定位的元素下查找子节点等

```
driver.find_element_by_id(loginForm).find_element_by_name(username)
```

10.简洁方法

find_element(by='id', value=None)与find_elements(by='id', value=None)实际是实现find_element_by_xxx这个的底层实现，只是简洁些，当然我们也可以用

```
#导入By模块，实际里面就是id，class，name这些常量
from selenium.webdriver.common.by import By

driver.find_element(By.NAME,username)
```

#### 元素Element事件

Element对象有一系列的方法，来让我们操作定位的元素

1.Element.click() 点击元素

```
driver.find_elements_by_link_text(Continue).click()
```

2.输入文本

```
#有些输入框中原有的文本不会被自动清除掉，需要使用clear()方法清除
driver.find_element_by_name(username).clear()

#输入内容
driver.find_element_by_name(username).send_keys("username")
```

3.获取参数

```
#获取对应特性值
Element.get_attribute(name)

#获取对应属性值
Element.get_property(name)

#property是DOM中的属性，是JavaScript里的对象；attribute是HTML标签上的特性，它的值只能够是字符串。一般用attr就行

#获取当前元素的内容
Element.text

#获取当前元素标签名
Element.tag_name

#获取当前元素尺寸
Element.size

#获取当前元素坐标
Element.location
```

4.判断方法

```
#判断当前元素是否可见
Element.is_displayed()

#判断当前元素是否被启用
Element.is_enabled()

#判断当前元素是否被选中
Element.is_selected()
```

### 等待

现在的网页，基本都是使用ajax异步的加载各种资源的，所以可能我们需要定位的元素不会第一时间就加载出来，这时候是无法定位的，也就会抛出异常。而解决这个问题的方法，就是等待。

#### 1.硬性等待

使用time.sleep(sec)实现，需要自己估计网页加载的时间，硬性地等待，无论网页加载快慢，都会强制等待这么多时间

```
import time

time.sleep(10)
```

#### 2.显式等待

就是设定一个条件，同时设置一个时间，在这个时间范围内，如果网页出现符合的条件，就不等待继续执行，如果没有则循环直到超时报错

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delay_loading")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"myDynamicElement"))
    )
finally:
    driver.quit()
```

这段代码主要讲的是：

1. 实例化WebDriverWait类，传入driver与最大等待时长，默认poll_frequency(扫描频率)为500毫秒
1. until()是WebDriverWait类的一个方法，参数是一个等待条件（expected_conditions），如果满足等待条件，则WebDriverWait类停止等待，并且返回expected_conditions的值，否则当等待时间到将抛出TimeoutException异常
1. 除了until()还有个until_not()，看语义就明白
1. 等待条件（expected_conditions）如果成功则返回element对象，或有些是返回布尔值，或者其它不为null的值

等待条件（expected_conditions）内置的方法主要有：

```
title_is : #验证 driver 的 title 是否与传入的 title 一致，返回布尔值
title_contains : #验证 driver 的 title 中是否包含传入的 title，返回布尔值
presence_of_element_located :# 验证页面中是否存在传入的元素，传入元素的格式是 locator 元组，如 (By.ID, "id1")，返回element对象
visibility_of_element_located : #验证页面中传入的元素（ locator 元组格式 ）是否可见，这里的可见不仅仅是 display 属性非 None ，还意味着宽高均大于0，返回element对象或false
visibility_of : #验证页面中传入的元素（ WebElement 格式 ）是否可见。返回element对象或false
presence_of_all_elements_located : #验证页面中是否存在传入的所有元素，传入元素的格式是 locator 元组构成的 list，如 [(By.ID, "id1"), (By.NAME, "name1")，返回element或false
text_to_be_present_in_element : #验证在指定页面元素的text中是否包含传入的文本，返回布尔值
text_to_be_present_in_element_value : #验证在指定页面元素的value中是否包含传入的文本，返回布尔值
frame_to_be_available_and_switch_to_it : #验证frame是否可切入，传入 locator 元组 或 WebElement，返回布尔值
invisibility_of_element_located : #验证页面中传入的元素（ locator 元组格式 ）是否可见，返回布尔值
element_to_be_clickable : #验证页面中传入的元素（ WebElement 格式 ）是否点击，返回element
staleness_of : #判断传入元素（WebElement 格式）是否仍在DOM中，返回布尔值
element_to_be_selected : #判断传入元素（WebElement 格式）是否被选中，返回布尔值
element_located_to_be_selected :# 判断传入元素（locator 元组格式）是否被选中，返回布尔值
element_selection_state_to_be :# 验证传入的可选择元素（WebElement 格式）是否处于某传入状态，返回布尔值
element_located_selection_state_to_be : #验证传入的可选择元素（WebElement 格式）是否处于某传入状态，返回布尔值
alert_is_present : #验证是否有 alert 出现。返回alert对象
```

#### 3.隐式等待

一种全局的设置，设置一个最大时长，如果定位的元素没有出现就会循环的查询直到超时或者元素出现，相比于硬性等待，这个更加弹性，元素出现了就不会等待了

```
rom selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id('myDynamicElement')
```

### 行为链

ActionChains可以完成简单的交互行为，例如鼠标移动，鼠标点击事件，键盘输入，以及内容菜单交互。这对于模拟那些复杂的类似于鼠标悬停和拖拽行为很有用

使用方法：

实例化一个ActionChains对象并在对象上调用行为方法时，这些行为会存储在ActionChains对象的一个队列里。只有调用perform()时，这些动作就以他们队列的顺序来触发

导入类

```
from selenium.webdriver import ActionChains
```

链式模型操作：

```
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

队列顺序操作：

```
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
action.perform()
```

主要的行为方法有

```
click(on_element=None)
#点击一个元素。参数：on_element:要点击的元素，如果是None，点击鼠标当前的位置

click_and_hold(on_element=None)
#鼠标左键点击一个元素并且保持。参数：on_element:同click()类似

double_click(on_element=None)
#双击一个元素

drag_and_drop(source, target)
#鼠标左键点击source元素，然后移动到target元素释放鼠标按键

drag_and_drop_by_offset(source, xoffset,yoffset)
#拖拽目标元素到指定的偏移点释放。参数: source:点击的参数 xoffset:X偏移量 * yoffset:Y偏移量

key_down(value,element=None)
#只按下键盘，不释放。我们应该只对那些功能键使用(Contril,Alt,Shift)。参数： value：要发送的键，值在Keys类里有定义 element:发送的目标元素，如果是None，value会发到当前聚焦的元素上

key_up(value,element=None)
#释放键。参考key_down的解释

move_by_offset(xoffset,yoffset)
#将当前鼠标的位置进行移动

move_to_element(to_element)
#把鼠标移到一个元素的中间

move_to_element_with_offset(to_element,xoffset,yoffset)
#鼠标移动到元素的指定位置，偏移量以元素的左上角为基准。参数： to_element:目标元素 xoffset:要移动的X偏移量 * yoffset:要移动的Y偏移量

perform()
#执行所有存储的动作

release(on_element=None)
#释放一个元素上的鼠标按键

send_keys(*keys_to_send)
#向当前的焦点元素发送键

send_keys_to_element(element,*keys_to_send)
#向指定的元素发送键
```

参考的key值在[这里](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys)

### 弹窗操作

目前主流弹窗就三种，alert，window，div封装的

#### alert弹窗

alert弹窗主要是js中alert()、confirm()、prompt()方法实现的，虽然这三种在js中不同，但对selenium都可以统一实例化Alert对象处理，首先查看Alert对象的主要方法

```
#接受和忽略弹框：

Alert(driver).accept()
Alert(driver).dismiss()

#prompt里输入字符:

Alert(driver).send_keys("text")

#读取prompt的提示字符：

Alert(driver).text

#向一个认证的对话框发送用户名和密码，会自动点击确认

Alert(driver).authenticate('user','passwd')
```

对于弹窗生成Alert对象主要有两种方法

1.使用driver的API切换至弹窗操作

```
alert = driver.switch_to_alert() #底层实际就是Alert(driver)，返回Alert对象
```

2.直接使用Alert类实例化

```
from selenium.webdriver.common.alert import Alert

alert = Alert(driver)
```

#### window类型

window类型实际就是那种点击界面元素后，浏览器新开的一个窗口，我们可以用driver的API直接切换到这个窗口进行一般的定位元素那些操作

```
#选择对应的window_handle切换
driver.switch_to_window(window_handle)

#window_handle获取
driver.current_window_handle
driver.window_handles
```

#### div封装的

div封装的弹窗就是使用浏览器F12查看HTML源代码时，弹窗的代码由div标签封装在页面中，所以这种弹窗可以直接find_element_by_xxx直接定位

可能还有网页中使用frame标签的，这就需要先切换到新的frame，上面driver的方法有介绍

如果对JavaScript熟悉的，这些弹窗都可以用js处理

参考：

[https://python-selenium-zh.readthedocs.io/zh_CN/latest](https://python-selenium-zh.readthedocs.io/zh_CN/latest)

[https://selenium-python.readthedocs.io/api.html](https://selenium-python.readthedocs.io/api.html)
