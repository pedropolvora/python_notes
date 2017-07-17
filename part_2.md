## Functions


Functions can take two types of parameters, **positional** which depends on the position of the parameter, and **keyword** which depend on the name of the parameter itself.

```python
def my_function(first_arg, second_arg, named_arg='default_value):
    print('executing the function')
    return first_arg, named_arg


# Note that the choice between positional and keyword argument
# is made at the call, not at the definition

my_function(first_arg, named_arg = 'new_value')
```

