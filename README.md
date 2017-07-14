## Beyond Python Basics

#### Packages vs Modules

In a nutshell, a package is a folder, module is a file.

##### Modules

A module is typically a single source file, when imported it's an object of the class module.

```
import my_module
type(my_module) # returns <class `module`>
```

##### Package

Special type of module, that can contain other modules. It's used to organize the modules. A package is a module that contains a `__path__` attribute.

#### Sys.path

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

#### Packages

Basic package structure, `path_entry` must by in `sys.path`, then a package is essentially a folder with a `__init__.py` inside.
```
path_entry/
 |---my_package/
      |---__init__.py
```
when you import `my_package` the `__init__.py` is executed.
