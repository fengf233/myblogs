

简介

Flask是一个使用Python编写的轻量级Web应用框架，基于Werkzeug提供的WSGI(Web Server Gateway Interface，web服务网关接口)工具箱和Jinja2 模板引擎。

Flask本身相当于一个内核（对于WSGI的包装）， 所以Flask也被称为microframework，因为它使用简单的核心，用extension增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术。

安装

```
pip install flask
```
