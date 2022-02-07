## Issues with intellisense in Visual Studio Code
When i use this simple module Visual Studio don't provide intellisense, but the code runs

### Repro steps
Clone this repo and put the module in f. example folder ```C:\Python27\Lib\site-packages```

Create a new script.py file in another location an import the module.

```python
from myModule import MyClass
from myModule.mySubModule import MySubClass

myClass = MyClass('baseParameterValue', 'parameterValue')
mySubClass = MySubClass('baseParameterValue', 'parameterValue')

myClass.baseFunction()
mySubClass.baseFunction()
```

![](/Resources/Missing%20intellisense.png)

### Expected behavior
Intellisense and collored code

![](/Resources/Intellisense.png)
