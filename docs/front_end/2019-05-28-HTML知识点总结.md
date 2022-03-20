

**一.基本知识**

HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage

HTML 标记标签通常被称为** HTML 标签 (HTML tag)    <标签>内容</标签>**

**HTML 元素**包含了开始标签与结束标签，**元素的内容**是开始标签与结束标签之间的内容，**元素属性**是 HTML 元素提供的附加信息。

基本**HTML 网页结构**如下，body标签内的才是我们在浏览器上所视内容

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>页面标题</title>
    </head>
    <body>
        <h1>标题</h1>
        <p>段落</p>
    </body>
</html>    
```

**<!DOCTYPE html>** 声明为 HTML5 文档

**<html>** 元素是 HTML 页面的根元素

**<head>** 元素包含了文档的元（meta）数据，如 <meta charset="utf-8"> 定义网页编码格式为 **utf-8**。

**<title>** 元素描述了文档的标题，浏览器标签名

**<body>** 元素包含了可见的页面内容

**<h1>** 元素定义一个大标题

**<p>** 元素定义一个段落

**<!-- 内容 -->**注释内容

**二.元素属性**

HTML元素属性一般在开始标签中，以键值对表示

```
<a href="http://www.baidu.com">表示链接</a>
```

常见属性

<img src="https://img2018.cnblogs.com/blog/1685507/201905/1685507-20190528102008305-791408060.png" alt="" width="570" height="181" />

其它标准属性参考[这里](https://www.runoob.com/tags/ref-standardattributes.html)

**三.头部**

可以添加在头部区域的元素标签为: <title>, <style>, <meta>, <link>, <script>, <noscript>, and <base>.

```
<title>文档标题</title>
```

```
<link rel="stylesheet" type="text/css" href="theme.css" />
```

**四.主体**

最为常见的有:

1.<h1> 定义最大的标题。 <h6> 定义最小的标题。标题（Heading）是通过 <h1> - <h6> 标签进行定义的.

```
<h1>这是一个标题。</h1>
<h2>这是一个标题。</h2>
<h3>这是一个标题。</h3>
```

2.<hr> 标签在 HTML 页面中创建水平线

```
<p>这是一个段落。</p>
<hr>
<p>这是一个段落。</p>
```

3.<p> 标签定义段落。

如果在不产生一个新段落的情况下进行换行（新行），请使用 <br> 标签

```
<p>这个<br>段落<br>演示了分行的效果</p>
```

4.<a> 标签定义超链接，用于从一张页面链接到另一张页面。<a> 元素最重要的属性是 href 属性，它指示链接的目标。

```
<a href="URL">链接</a>
```

5.<img> 元素向网页中嵌入一幅图像,<img> 标签有两个必需的属性：src 属性 和 alt 属性。src 指 "source"。源属性的值是图像的 URL 地址。alt 属性用来为图像定义一串预备的可替换的文本。

```
<img src="url"  alt="图片" />
```

6.HTML表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

7.无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。

无序列表使用 <ul> 标签

```
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
```

8.有序列表也是一列项目，列表项目使用数字进行标记。 有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。

列表项使用数字来标记。

```
<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>
```

9. 可定义文档中的分区或节（division/section）。

如果用 id 或 class 来标记 ，那么该标签的作用会变得更加有效。

```

  <h3>This is a header</h3>
  <p>This is a paragraph.</p>

```

10.<form> 标签用于为用户输入创建 HTML 表单。

表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。

表单还可以包含 menus、textarea、fieldset、legend 和 label 元素。

表单用于向服务器传输数据。详细[这里](https://www.runoob.com/html/html-forms.html)

```
<form action="form_action.asp" method="get">
  <p>First name: <input type="text" name="fname" /></p>
  <p>Last name: <input type="text" name="lname" /></p>
  <input type="submit" value="Submit" />
</form>
```

摘于[https://www.runoob.com/html/html-tutorial.html](https://www.runoob.com/html/html-tutorial.html)
