## Beyond Python Basics

### Packages vs Modules

In a nutshell, a package is a folder, module is a file.

#### Modules

A module is typically a single source file, when imported it's an object of the class module.

```
import my_module
type(my_module) # returns <class `module`>
```

#### Package

Special type of module, that can contain other modules. It's used to organize the modules. A package is a module that contains a `__path__` attribute.

### Sys.path

`sys.path` is where python will look for modules, it's a **list**.
we can add folders to `sys.path` by doing 
```
import sys
sys.path.append('/usr/path')
```

The `PYTHONPATH` environment variable contains values that are added to the `sys.path` list.

```
export PYTHONPATH=/usr/path
```

### Packages

Basic package structure, `path_entry` must by in `sys.path`, then a package is essentially a folder with a `__init__.py` inside.
```
path_entry/
 |---my_package/
      |---__init__.py
```
when you import `my_package` the `__init__.py` is executed.


### Imports

#### Relative Imports

Imports which use a relative path to modules **in the same package**.



```
|---my_package/
    |---__init__.py
    |---a.py
    |---nested/
        |---__init__.py
            |---b.py
            |---c.py
```

To import,

```
# in c.py
from ..a import A
from .b import B
```

**Although useful they should be avoided**

#### `__all__`

Lets you control all the attributes that are imported when a module is imported, it's an optional attribute.
The `__all__` attribute should be a list of strings, they contain all the names available in the module.

If `__all__` is not imported then all the public names are imported


### Namespace packages

Namespace packages are essentially a package spread accross different directories. 

They don't  have `__init__.py`, nothing is executed when the it's imported, so that questions of initialization order are avoided.

##### How import works

Consider `import foo`

1. Scanning of sys.path
1. If `__init__.py`, a normal package is imported
1. If the file `foo.py` is found, then it's loaded
1. Otherwise, all matching dires are considered parts of the package.


### Executable Directories

You can pass a path to python `python dir_path`, but to have it actually execute the directory you must create a `__main__.py` file.
