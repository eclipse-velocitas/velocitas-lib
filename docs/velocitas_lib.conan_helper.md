<!-- markdownlint-disable -->

<a href="../velocitas_lib/conan_helper.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.conan_helper`





---

<a href="../velocitas_lib/conan_helper.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_required_sdk_version`

```python
get_required_sdk_version() → Optional[str]
```

Return the required version of the core SDK. 



**Returns:**
 
 - <b>`Optional[str]`</b>:  The required version or None in case SDK is not a dependency. 


---

<a href="../velocitas_lib/conan_helper.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `export_conan_project`

```python
export_conan_project(conan_project_path: str) → None
```

Export a conan project to the local conan cache. 



**Args:**
 
 - <b>`conan_project_path`</b> (str):  The path to directory containing the project. 


---

<a href="../velocitas_lib/conan_helper.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
