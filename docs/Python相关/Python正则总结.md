

### 正则基本语法

#### 元字符

<th align="center">元字符</th>|描述|示例|匹配
|------
<td align="center">.</td>|句号匹配任意单个字符除了换行符。|a.c|abc adc
<td align="center">[ ]</td>|字符种类。匹配方括号内的任意字符。|[Tt]he|The the
<td align="center">[^ ]</td>|否定的字符种类。匹配除了方括号里的任意字符|[^Tt]he|xhe
<td align="center">*</td>|匹配*号之前的字符大于等于0次。|abc*|ab abccc
<td align="center">+</td>|匹配+号之前的字符大于等于1次。|abc+|abc abcc
<td align="center">?</td>|匹配？号之前的字符0或1次.|abc?|ab abc
<td align="center">{n,m}</td>|匹配之前的字符重复n到m次，`{n}` 重复n次，`{n,}` 重复n次或更多次|ab{1,2}c|abc abbc
<td align="center">(xyz)</td>|分组，匹配与 xyz 完全相等的字符串.|(abc){2}|abcabc
<td align="center">|</td>|或运算符，匹配符号前或后的字符.|(ab|bc){2}|abab bcbc
<td align="center">\</td>|转义字符,用于匹配一些保留的字符 `[ ] ( ) { } . * + ? ^ $ \ |`|\\abc|\abc
<td align="center">^</td>|从开始行开始匹配.|^abc|abc
<td align="center">$</td>|从末端开始匹配.|abc$|abc

#### 简写字符集

<th align="center">简写</th>|描述|示例|匹配
|------
<td align="center">\w</td>|匹配所有字母数字，等同于 `[a-zA-Z0-9_]`|a\wc|abc aBc
<td align="center">\W</td>|匹配所有非字母数字，即符号，等同于： `[^\w]`|a\Wc|a.c
<td align="center">\d</td>|匹配数字： `[0-9]`|a\dc|a2c
<td align="center">\D</td>|匹配非数字： `[^\d]`|a\Dc|abc
<td align="center">\s</td>|匹配所有空格字符，等同于： `[\t\n\f\r\p{Z}]`|a\sc|a c
<td align="center">\S</td>|匹配所有非空格字符： `[^\s]`|a\Sc|abc
<td align="center">\f</td>|匹配一个换页符|a\fc| 
<td align="center">\n</td>|匹配一个换行符|a\nc| 
<td align="center">\r</td>|匹配一个回车符|a\rc| 
<td align="center">\t</td>|匹配一个制表符|a\tc| 
<td align="center">\v</td>|匹配一个垂直制表符|a\vc| 
<td align="center">\p</td>|匹配 CR/LF（等同于 `\r\n`），用来匹配 DOS 行终止符|a\pc| 

#### 零宽断言

<th align="center">符号</th>|描述|示例|匹配
|------
<td align="center">?=</td>|正先行断言-存在，即之后的字符串要匹配判断才能匹配|a(?=ing)|a后面有ing结尾的才匹配a(不包括ing)
<td align="center">?!</td>|负先行断言-排除，即之后的字符串要不匹配判断才能匹配|a(?!ing)|a后面不是ing结尾的才匹配a(不包括后面)
<td align="center">?<=</td>|正后发断言-存在，即之前的字符串要匹配判断才能匹配|(?<=re)a|a前面有re的才匹配a(不包括re)
<td align="center">?<!</td>|负后发断言-排除，即之前的字符串要不匹配判断才能匹配|(?<!re)a|a前面没有re的才匹配a(不包括re)

#### 贪婪与惰性匹配

贪婪：匹配尽可能长的字符串

惰性：匹配尽可能短的字符串

惰性模式的启用只需在重复元字符之后加?既可。

<th align="center">符号</th>|描述|示例|匹配
|------
<td align="center">*? </td>|重复任意次，但尽可能少重复|abc*?|ab
<td align="center">+?</td>|重复1次或更多次，但尽可能少重复|abc+?|abc
<td align="center">??</td>|重复0次或1次，但尽可能少重复|abc??|ab
<td align="center">{n,m}?</td>|重复n到m次，但尽可能少重复|abc{1,2}?|abc
<td align="center">{n,}?</td>|重复n次以上，但尽可能少重复|abc{1,}?|abc

#### 处理选项

<th align="center">符号</th>|描述|示例|匹配
|------
<td align="center">(?i) </td>|忽略大小写|(?i)abc|abC
<td align="center">(?x)</td>|忽略空格字符|(?x)ab c|abc
<td align="center">(?s)</td>|.匹配任意字符，包括换行符|(?s)abc|ab\nc
<td align="center">(?m)</td>|多行模式,更改^和$的含义，使它们分别在任意一行的行首和行尾匹配，而不仅仅在整个字符串的开头和结尾匹配。|(?m)abc|abc

### Python re模块

#### 常见参数
|参数|描述
|pattern|匹配的正则表达式
|string|要匹配的字符串。
|flags|标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

#### 可选标志位

正则表达式可以包含一些可选标志修饰符（flags参数）来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志
|修饰符|描述
|re.I|使匹配对大小写不敏感
|re.L|做本地化识别（locale-aware）匹配
|re.M|多行匹配，影响 ^ 和 $
|re.S|使 . 匹配包括换行在内的所有字符
|re.U|根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
|re.X|该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

#### 常用方法

**1.compile方法**

re.compile(pattern, flags=0)

将正则表达式的样式编译为一个正则表达式对象（正则对象），可以用于匹配，通过这个对象的方法 match(), search()匹配，比如

```
prog = re.compile(pattern)
result = prog.match(string)
```

等价

```
result = re.match(pattern, string)
```

**2.re.match方法**

re.match(pattern, string, flags=0)

re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none，如果匹配就返回匹配对象

```
re.match(r"a.c","babc")
返回None

re.match(r"a.c","abcb")
返回匹配对象<re.Match object; span=(0, 3), match='abc'>
```

**3.re.search方法**

re.search(pattern, string, flags=0)

扫描整个字符串找到匹配样式的第一个位置，并返回一个相应的匹配对象。如果没有匹配，就返回一个 None 

```
re.search(r"a.c","babc")
返回匹配对象<re.Match object; span=(1, 4), match='abc'>
```

**4.re.findall方法**

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表（字符串列表，不是匹配对象），如果没有找到匹配的，则返回空列表

```
re.findall(r"a.c","babcbABC",re.I)
返回['abc', 'ABC']
```

相类似还有一个re.finditer方法，这个返回一个可迭代对象

**5.re.split方法**

re.split(pattern, string, maxsplit=0, flags=0)

maxsplit参数表示分割次数，默认0不限制

**6.re.sub方法**

re.sub(pattern, repl, string, count=0, flags=0)

返回通过使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串。 如果样式没有找到，则不加改变地返回 string。 repl 可以是字符串或函数；如为字符串，则其中任何反斜杠转义序列都会被处理。

- pattern : 正则中的模式字符串。
- repl : 替换的字符串，也可为一个函数。
- string : 要被查找替换的原始字符串。
- count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
- flags : 编译时用的匹配模式标志。

#### 正则对象

re.compile() 返回 Pattern正则对象，它的方法与上面re的常见方法差不多，只不过要多些参数

- pattern: 编译时用的表达式字符串。
- flags: 编译时用的匹配模式。数字形式。
- groups: 表达式中分组的数量。
- groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内

常用方法有：

**1.Pattern.search(string[, pos[, endpos]])**

这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None（re.search()无法指定这两个参数）

**2.Pattern.match(string[, pos[, endpos]])**

这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；如果匹配过程中pattern无法匹配，或者匹配未结束就已到达endpos，则返回None。pos和endpos的默认值分别为0和len(string)

**3.Pattern.split(string, maxsplit=0**

等价于 re.split() 函数，使用了编译后的样式

**4.Pattern.findall(string[, pos[, endpos]])**

类似函数 findall() ， 使用了编译后样式，但也可以接收可选参数 pos 和 endpos ，限制搜索范围，就像 search()。

**5.Pattern.sub(repl, string, count=0)**

等价于 re.sub() 函数，使用了编译后的样式。

#### 匹配对象

匹配对象是使用 match() 和 search() 方法是查找到了匹配的返回对象

基本属性：

- **string**: 匹配时使用的文本。
- **re**: 匹配时使用的Pattern对象。
- **pos**: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
- **endpos**: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
- **lastindex**: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
- **lastgroup**: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

基本方法：

**1.Match.group([group1, ...])**

获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。

```
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')
```

使用(?P<name>)语法取分组别名

```
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')
'Malcolm'
>>> m.group('last_name')
'Reynolds'
```

**2.Match.groups(default=None)**

返回一个元组，包含所有匹配的子组，在样式中出现的从1到任意多的组合。 default 参数用于不参与匹配的情况，默认为 None。

```
>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> m.groups()
('24', '1632')
```

**3.start([group])**

返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。

**4.end([group])**

返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。

**5.span([group])**

返回(start(group), end(group))

参考

[https://docs.python.org/zh-cn/3/library/re.html#search-vs-match](https://docs.python.org/zh-cn/3/library/re.html#search-vs-match)

[https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html](https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)
