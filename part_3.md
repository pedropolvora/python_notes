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

## Closures


A closure is how does a local function presevers the encolsing scope once it's called and the enclosing scope no longer exists.
In the example bellow, it's how the `inner` function preservers the reference of `x`.
It's like the local function closes over the arguments in need preventing them from being garbage collected.

```python
def outer():
    x = 10

    def inner(y):
        return x + y

    return inner

i = outer()
```
You can access the closure by `i.__closure__`. ( using the example above).


### Function Factory

A function that returns new specialized function depending on the enclosing context.

```python
>>> def sum_to(x):
...     def inner(y):
...             return x + y
...     return inner
...
>>> sum2 = sum_to(2)
>>> sum2(3)
5
```
