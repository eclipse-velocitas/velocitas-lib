<!-- markdownlint-disable -->

<a href="../velocitas_lib/templates.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.templates`





---

<a href="../velocitas_lib/templates.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `copy_templates`

```python
copy_templates(
    template_dir: str,
    target_dir: str,
    template_file_mapping: List[CopySpec],
    variables: Dict[str, str]
) → None
```

Copy templates from the template dir to the target dir. 



**Args:**
 
 - <b>`template_dir`</b> (str):  Path to the directory containing the template files. 
 - <b>`target_dir`</b> (str):  Path to the target directory. 
 - <b>`template_file_mapping`</b> (Dict[str, str]):  A mapping of source path to target path. 
 - <b>`variables`</b> (Dict[str, str]):  Name to value mapping which will be replaced when parsing the template files. 


---

<a href="../velocitas_lib/templates.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CopySpec`
Copy specification of a single file or directory. 

<a href="../velocitas_lib/templates.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(source_path: str, target_path: Optional[str] = None)
```








---

<a href="../velocitas_lib/templates.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_target`

```python
get_target() → str
```

Get the target path of the copy spec. 



**Returns:**
 
 - <b>`str`</b>:  If a target_path is given explicitly, it will be returned.  Otherwise the source_path will be returned. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
