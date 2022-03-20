

使用xadmin时，在网上找到文档中，xadmin中list_export_fields字段时限制导出的字段

但是在实际使用中却是不生效

参考这篇文章就可以使之生效[https://blog.csdn.net/Laozizuiku/article/details/105260408](https://blog.csdn.net/Laozizuiku/article/details/105260408)

具体修改就是修改xadmin/plugins/export.py中的ExportPlugin的get_result_list方法

```
def get_result_list(self, __):
    if self.request.GET.get('all', 'off') == 'on':
       self.admin_view.list_per_page = sys.maxsize
    self.admin_view.list_display=getattr(self.admin_view,'list_export_fields', self.admin_view.list_display)
    return __()
```

然后就可以在adminx.py中使用list_export_fields了

但如果像排除某个字段不导出呢，比如自定义字段，同样可以这样修改

```
    def get_result_list(self, __):
        if self.request.GET.get('all', 'off') == 'on':
            self.admin_view.list_per_page = sys.maxsize
        #添加exclude_export_fields字段
        exclude_export_fields = getattr(self.admin_view,'exclude_export_fields', '')
        list_display_tmp = self.admin_view.list_display[:]
        if exclude_export_fields:
            for exclude in exclude_export_fields:
                if exclude in list_display_tmp:
                    list_display_tmp.remove(exclude)
                else:
                    pass
        self.admin_view.list_display = list_display_tmp[:]
        return __()
```

在adminx.py中使用exclude_export_fields就可以了
