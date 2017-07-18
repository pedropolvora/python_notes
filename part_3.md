## Local Functions

In python we can define functions in another functions

```python
def main():
    def local_func():
        return 'hi'

    local_func()
    return 'world'
```

Local functions are not members of their parents in any way, they are just name bindings.. so `main.local_func()` does not work.

They are useful for on-off uses, similar to lambdas but a bit more general.

## LEGB rule

How names are looked-up:
* Local scope
* Enclosing scope (local + parameters of the enclosing function)
* Global scope (module level name bindings)
* Built-in scope


```python3
>>> g = 'global'
>>> def outer(p='param'):
...     l = 'local'
...     def inner():
...             print(g, p, l)
...     inner()
...
>>> outer()
global param local
>>>
```

