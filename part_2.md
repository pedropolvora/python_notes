## Functions


Functions can take two types of parameters, **positional** which depends on the position of the parameter, and **keyword** which depend on the name of the parameter itself.

```python
def my_function(first_arg, second_arg, named_arg='default_value'):
    print('executing the function')
    return first_arg, named_arg


# Note that the choice between positional and keyword argument
# is made at the call, not at the definition

my_function(first_arg, named_arg = 'new_value')
```


### Callable instances


To find if an object is callable we can use the `callable()` method.


We can use the python special method `__call__()` to create callable instances.


Occasional we would like to have function that perserves state between calls, this is usually a bad pratice, but we can needed for eample for caching purposes. To achieve this we use the `__call__()` and a class. A full example can be found [here](./part2_scripts) 


As a note, we should say that **classes are callable objects**, when called they create a new instance.


### Lambda functions

```python
square = lambda x: x*2
print(square) # <function <square> ...
print(square(3))
```

The differences between a normal function vs a lambda:

* `def ` is a **statement** that defines a function and binds it to a name
* `lambda x: ..` is an **expression** which evaluates to a function
* regular functions must have names, lambdas are anonymous
* lambdas have a single expression, and use no return
* lambdas are very hard if not impossible to test

### Extended Argument Syntax


Consider this example,
```python
def hypervolumen(*lengths):
    print(type(lengths))    # will return tuple
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v
```
In addition to the `*args` we can have arbitrary keyword arguments `**kwargs`.

```python
def tag(name, **attributes):
    print(type(attributes))     # will return dict
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=value))
    result += '>'
    return result 
```

Some rules:
    * we must always have `*args` before `**kwargs` 
    * any arguments before `*args` are required positional arguments
    * any arguments after `*args` are required keyword arguments
    * `**kwargs` must be in the end of the declaration 

```python
def extended_args(p1, p2, *args, k1, k2, **kwargs):
    .......
```

### Extended Call Argument

Allows to easily populate positional and keyword arguments.

```python
def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha': 52}
color(**k)
```
this will output 
```
r= 21
g= 68
b= 120
{'alpha': 52}
```
