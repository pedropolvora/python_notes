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

