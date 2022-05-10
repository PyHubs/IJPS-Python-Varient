# IJPS-Python-Varient V1

Offical Release Version 1 and comes with bug fixes!
 
 
> IJP CODE
```python
#/ijp python
fun name():
  write('this is the main function')
  
  fun subname():
    write("this is a sub function, which can be called in name")
    
  subname()
  
name()
```

> Python CODE
```
def name():
  print('this is a main function')
  
def subname():
  print('this is a sub function, which can be called in name')
```

Before, whitespace used to break everything however, now its fixed!

# IJP SYNTAX DIFFERENCES TO PYTHON
`write("hello world")` --> `print("hello world")`

`!fun name():` --> `def name():`

`#!imp` --> `import`

`#!fr` --> `from`

`#/ijp python` --> `#/ijp python compiled`

`!hell` --> `class`

So most important custom IJP features, start with "!NAME", this means ! is a very special character.

DONT WRITE `!fun:`

DONT WRITE `!hell:`

As they will break the language.

# Upcoming features
```
#/ijp python
#/ijp color text

# Colored text!
write.red("Hello world")
write(red + "Hello world" + nor)
```
