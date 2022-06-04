

**原型对象**

1.每个对象一定会有一个原型对象

2.原型对象实际是构造实例对象的构造器中的一个属性，只不过这个属性是个对象

3.这个原型对象中的属性与方法，都会被对象实例所共享（类似python中的类方法，类属性）

4.但，原型对象的属性不是对象实例的属性，只要修改原型对象上的属性和方法，变动就会立刻体现在所有对象实例上。

5.JavaScript对每个创建的对象都会设置一个属性__proto__ ，指向它的原型对象xxx.prototype。

比如按照传统方法创建一个构造器

```
function Person(firstname,lastname,age,eyecolor)
{
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyecolor=eyecolor;
    this.changeName=changeName;
    function changeName(name)
    {
        this.lastname=name;
    }
}
```

实例化

```
var person1=new Person("John","Doe",50,"blue");
var person2=new Person("Sally","Rally",48,"green");
```

如上面person1和person2的changeName实际是绑定在实例上的

```
person1.changeName === person2.changeName 

...false

person1.changeName === Person.changeName 

...false
//因为this绑定实例，所以方法都是各自实例独立的方法。所以说this跟python中self类似
```

如果想要一种所有实例共享的方法或属性，那只有给Person.prototype中添加修改方法或属性，则person1和person2都会得到更新，且person1.__proto__ 等同于Person.prototype

```
Person.prototype.changeName2= function (name)
    {
        this.lastname=name;
    }

person1.changeName2 === person2.changeName2;

...true

person1.__proto__ === person2.__proto__;

...true
person1.__proto__ === Person.prototype;

...true
person1.__proto__

...{changeName2: , constructor: }
```

上面person1.__proto__(即Person.prototype)除了changeName2属性外，还有一个constructor属性，这个是指向创建当前对象的构造函数

```
person1.__proto__.constructor
...
 Person(firstname,lastname,age,eyecolor)
{
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyecolor=eyecolor;
    this.changeName=changeName;
    function changeNa
```

**原型链**

1.由于xxx.prototype也是个某个构造器的实例对象，所以它也有__proto__指向一个原型对象yyy.prototype,所以会成链

2.原型链的顶端或源头，是Object.prototype（有点像基因链呀，继承也是通过这条链实现的）

3.读取实例对象的某个属性或方法时，JavaScript引擎按照 对象-->原型对象a-->a的原型对象b----,最后到Object.prototype如果还是找不到，就返回undefined

4.如果实例对象属性和原型对象属性名一样，同python，优先实例自身的属性

按照上面例子构造一个继承Person的构造器

```
class Teacher extends Person{
    constructor(firstname,lastname,age,eyecolor,subject) {
        super(firstname,lastname,age,eyecolor);
        this.subject = subject;
        }
    teach(){
        console.log(this.subject);
    }
}
```

实例化

```
var teacher1=new Teacher("Tim","D",25,"blue","math");
```

在实例中查看原型链的情况

```
>>>teacher1.__proto__

...Person {constructor: , teach: }

>>>teacher1.__proto__.constructor

...class Teacher extends Person{
    ...
}

>>>teacher1.__proto__.__proto__

...{changeName2: , constructor: }

>>>teacher1.__proto__.__proto__.constructor

...function Person(firstname,lastname,age,eyecolor)
{
    ....
}

>>>teacher1.__proto__.__proto__.__proto__

...{constructor: , __defineGetter__: , __defineSetter__: , hasOwnProperty: , __lookupGetter__: , }

>>>teacher1.__proto__.__proto__.__proto__.constructor

...Object() { [native code] }

>>>teacher1.__proto__.__proto__.__proto__.__proto__

...null
```

可以发现teacher1的原型链是 Teacher.prototype ---> Person.prototype ---> Object.prototype ---> null
