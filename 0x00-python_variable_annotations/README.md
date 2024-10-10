# Python Variable Annotations

## Description
This project focuses on Python variable annotations and type hints. It covers various aspects of type annotations in Python 3, including:
- Type annotations for variables
- Type annotations for functions
- Duck typing
- Validating code with mypy

## Project Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a newline character
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code should use the `pycodestyle` style (version 2.5)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be real sentences explaining the purpose of the module, class, or method

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

```python
def add(a: float, b: float) -> float:
```

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

### 2. Basic annotations - floor
Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

### 4. Define variables
Define and annotate variables with the specified values:
- `a`: int = 1
- `pi`: float = 3.14
- `i_understand_annotations`: bool = True
- `school`: str = "Holberton"

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple.

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

### 9. Let's duck type an iterable object
Annotate a function's parameters and return values with the appropriate types using duck typing.

### Advanced Tasks

### 10. Duck typing - first element of a sequence
Augment the code with the correct duck-typed annotations.

### 11. More involved type annotations
Add type annotations to the function using TypeVar.

### 12. Type Checking
Use mypy to validate code and apply necessary changes.

## Files
- `0-add.py`
- `1-concat.py`
- `2-floor.py`
- `3-to_str.py`
- `4-define_variables.py`
- `5-sum_list.py`
- `6-sum_mixed_list.py`
- `7-to_kv.py`
- `8-make_multiplier.py`
- `9-element_length.py`
- `100-safe_first_element.py`
- `101-safely_get_value.py`
- `102-type_checking.py`

## Usage
Each file can be tested using its corresponding main file:

```bash
./0-main.py
./1-main.py
# etc...
```

For type checking:
```bash
mypy 102-type_checking.py
```

## Author
Mohammed Elgaily

## License
This project is part of the ALX Backend Python curriculum.

