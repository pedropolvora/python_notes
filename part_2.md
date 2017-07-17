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

We can use the python special method `__call__()` to create callable instances.


Occasional we would like to have function that perserves state between calls, this is usually a bad pratice, but we can needed for eample for caching purposes. To achieve this we use the `__call__()` and a class. A full example can be found [here](./part2_scripts) 
