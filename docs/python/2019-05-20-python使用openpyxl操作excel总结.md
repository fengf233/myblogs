

### **安装openpyxl**

```
pip install openpyxl
```

### **简单示例**

```
from openpyxl import Workbook

#创建一个工作薄对象,也就是创建一个excel文档
wb = Workbook()

#指定当前显示（活动）的sheet对象
ws = wb.active

# 给A1单元格赋值
ws['A1'] = 42

# 一行添加多列数据
ws.append([1, 2, 3])

# 保存excel
wb.save("sample.xlsx")
```

 

使用openpyxl的一般流程为：创建/读取excel文件-->选择sheet对象-->对表单/cell进行操作-->保存excel

 

### **1.创建/读取excel文件**

创建excel

```
from openpyxl import Workbook
wb = Workbook()
```

读取excel

```
from openpyxl import load_workbook
wb = load_workbook('1.xlsx')
```

保存excel

```
wb.save('filename.xlsx')
```

### **2.sheet表单操作**

获取sheet

```
#以list方式返回excel文件所有sheet名称（->list[str,str..]）wb.sheetnames
wb.get_sheet_names()
```

选择sheet对象

```
#根据sheet名称选取
ws = wb['sheet1']
ws = wb.get_sheet_by_name('sheet1')
#选择当前显示，活动的sheet
ws = wb.active
ws = wb.get_active_sheet()
```

创建新的sheet

```
#默认插入到最后
ws = wb.create_sheet("newsheet") 
#插入到最开始的位置(从0开始计算)
ws = wb.create_sheet("newsheet", 0)
```

复制一个sheet对象

```
source = wb.active
target = wb.copy_worksheet(source)
```

sheet常见属性

```
#sheet名称
sheet.title
#最大行和最大列
sheet.max_row
sheet.max_column
#行列生成器
sheet.rows #为行生成器, 里面是每一行的cell对象，由一个tuple包裹。
sheet.columns #为列生成器, 里面是每一列的cell对象，由一个tuple包裹。
可以使用list(sheet.rows)[0].value 类似方法来获取数据，或
for row in sheet.rows:
    for cell in row:
        print(cell.value)
来遍历值,或值生成器 sheet.values 仅遍历值
```

删除sheet

```
wb.remove(sheetobject) 
del wb['sheet'] #sheetname
```

sheet的其它操作

```
#插入行，在第7行之前插入
ws.insert_rows(7)
#插入列，在第7列之前插入
ws.insert_cols(7)
#删除行列
ws.delete_rows(7)
ws.delete_cols(7)
#可以删除多个
ws.delete_cols(6, 3)
```

 

### **3.单元格对象**

选择cell单元格对象

```
#根据名称访问
a1 = ws['A1'] #A列1行的单元对象
a2 = ws['a2'] #也可以小写
#cell方法访问
b2 = ws.cell(row=2, column=2)
b3 = ws.cell(3,2)
#从cell列表中返回
b3 = list(ws.rows)[2][1]
b3 = list(ws.columns)[1][2]
```

选择多个单元格

```
#切片访问
a2_b3 = ws['a2':'b3']
以行组成tuple返回tuple
((<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>))
#单独字母与数字返回列与行的所有数据
b = ws['b'] #返回b列的所有cell对象
row1 = ws['1'] #返回第1行的所有cell
#当然也能范围选择
a_e = ws['a:e'] #a-e列的cell对象
```

单元格属性

```
#返回列
cell.column
#返回行
cell.row
#返回值
cell.value
注意:如果单元格是使用的公式，则值是公式而不是计算后的值
#返回单元格格式属性
cell.number_format
默认为General格式
#单元格样式
cell.font
```

更改单元格值

```
#直接赋值
ws['a2'] = 222 
ws['a2'] = 'aaa'
ws['b2'] = '=SUM(A1:A17)' #使用公式

#value属性赋值
cell.value = 222
或
ws.cell(1,2,value = 222)
```

移动单元格

```
ws.move_range("D4:F10", rows=-1, cols=2)
表示单元格D4:F10向上移动一行，右移两列。单元格将覆盖任何现有单元格。(最新版本的才会这个方法，使用pip list查看版本是否为最新)
ws.move_range("G4:H10", rows=1, cols=1, translate=True)
移动中包含公式的自动转换
```

合并与拆分单元格

```
#合并单元格,以最左上角写入数据或读取数据
ws.merge_cells('A2:D2')
#拆分单元格
ws.unmerge_cells('A2:D2')
```

### **4.格式样式设置**

导入类

```
from openpyxl.styles import Font, colors, Alignment
```

Font类常见参数

```
font = Font(name='Calibri',  　　　　　　#字体名字
                 size=11,            　#字体大小
                 bold=False,        　　#是否加粗
                 italic=False,        #斜体
                 underline='none',　　#下划线
                 color='FF000000')　　#颜色,可以用colors中的颜色
```

设置字体

```
t_font = Font(name='Calibri', size=24, italic=True, color=colors.RED, bold=True)
#给font属性赋值font对象即可
sheet['A1'].font = t_font
```

对齐方式

```
# 设置B1中的数据垂直居中和水平居中，除了center，还可以使用`right、left`等等参数
sheet['B1'].alignment = Alignment(horizontal='center', vertical='center')
```

设置单元格长宽

```
# 第2行行高
sheet.row_dimensions[2].height = 40
# C列列宽
sheet.column_dimensions['C'].width = 30
```

官方文档参考:[https://openpyxl.readthedocs.io/en/latest/](https://openpyxl.readthedocs.io/en/latest/)
