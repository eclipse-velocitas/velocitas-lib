<!-- markdownlint-disable -->

<a href="../velocitas_lib/conan_helper.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.conan_helper`





---

<a href="../velocitas_lib/conan_helper.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_required_sdk_version`

```python
get_required_sdk_version() → Optional[str]
```

Return the required version of the core SDK. 



**Returns:**
 
 - <b>`Optional[str]`</b>:  The required version or None in case SDK is not a dependency. 


---

<a href="../velocitas_lib/conan_helper.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `move_generated_sources`

```python
move_generated_sources(
    generated_source_dir: str,
    output_dir: str,
    include_dir_rel: str,
    src_dir_rel: str
) → Tuple[List[str], List[str]]
```

Move generated source code from the generation dir into headers: <output_dir>/<include_dir_rel> sources: <output_dir>/<src_dir_rel> 



**Args:**
 
 - <b>`generated_source_dir`</b> (str):  The directory containing the generated sources. 
 - <b>`output_dir`</b> (str):  The root directory to move the generated files to. 
 - <b>`include_dir_rel`</b> (str):  Path relative to output_dir where to move the headers to. 
 - <b>`src_dir_rel`</b> (str):  Path relative to the output_dir where to move the sources to. 



**Returns:**
 
 - <b>`Tuple[List[str], List[str]]`</b>:  A tuple containing  [0] = a list of the paths to all headers  [1] = a list of the paths to all sources 


---

<a href="../velocitas_lib/conan_helper.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `export_conan_project`

```python
export_conan_project(conan_project_path: str) → None
```

Export a conan project to the local conan cache. 



**Args:**
 
 - <b>`conan_project_path`</b> (str):  The path to directory containing the project. 


---

<a href="../velocitas_lib/conan_helper.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_dependency_to_conanfile`

```python
add_dependency_to_conanfile(
    dependency_name: str,
    dependency_version: str
) → None
```

Add the dependency name to the project's list of dependencies. 



**Args:**
 
 - <b>`dependency_name`</b> (str):  The dependency to add e.g. grpc 
 - <b>`dependency_version`</b> (str):  The version of the dependency to add e.g. 1.50.1 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
