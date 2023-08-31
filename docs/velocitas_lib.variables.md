<!-- markdownlint-disable -->

<a href="../velocitas_lib/variables.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.variables`





---

<a href="../velocitas_lib/variables.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `json_obj_to_flat_map`

```python
json_obj_to_flat_map(
    obj,
    prefix: str = '',
    separator: str = '.'
) → Dict[str, str]
```

Flatten a JSON Object into a one dimensional dict by joining the keys with the specified separator. 


---

<a href="../velocitas_lib/variables.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ProjectVariables`




<a href="../velocitas_lib/variables.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(env: Dict[str, str])
```








---

<a href="../velocitas_lib/variables.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `replace_occurrences`

```python
replace_occurrences(input_str: str) → str
```

Replace all occurrences of the defined variables in the input string 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
