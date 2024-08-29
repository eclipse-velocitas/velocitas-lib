<!-- markdownlint-disable -->

<a href="../velocitas_lib/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib`





---

<a href="../velocitas_lib/__init__.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_valid_arch`

```python
get_valid_arch(arch: str) → str
```

Return a known architecture for the given `arch`. 



**Args:**
 
 - <b>`arch`</b> (str):  The architecture of the profile. 



**Returns:**
 
 - <b>`str`</b>:  valid architecture. 


---

<a href="../velocitas_lib/__init__.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `require_env`

```python
require_env(name: str) → str
```

Require and return an environment variable. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the variable. 



**Raises:**
 
 - <b>`ValueError`</b>:  In case the environment variable is not set. 



**Returns:**
 
 - <b>`str`</b>:  The value of the variable. 


---

<a href="../velocitas_lib/__init__.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_workspace_dir`

```python
get_workspace_dir() → str
```

Return the workspace directory. 


---

<a href="../velocitas_lib/__init__.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_app_manifest`

```python
get_app_manifest() → Dict[str, Any]
```






---

<a href="../velocitas_lib/__init__.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_script_path`

```python
get_script_path() → str
```

Return the absolute path to the directory the invoked Python script is located in. 


---

<a href="../velocitas_lib/__init__.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_package_path`

```python
get_package_path() → str
```

Return the absolute path to the package directory the invoked Python script belongs to. 


---

<a href="../velocitas_lib/__init__.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_project_cache_dir`

```python
get_project_cache_dir() → str
```

Return the project's cache directory. 



**Returns:**
 
 - <b>`str`</b>:  The path to the project's cache directory. 


---

<a href="../velocitas_lib/__init__.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_cache_data`

```python
get_cache_data() → Dict[str, Any]
```

Return the data of the cache as Python object. 


---

<a href="../velocitas_lib/__init__.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_log_file_name`

```python
get_log_file_name(service_id: str, runtime_id: str) → str
```

Build the log file name for the given service and runtime. 



**Args:**
 
 - <b>`service_id`</b> (str):  The ID of the service to log. 
 - <b>`runtime_id`</b> (str):  The ID of the runtime to log. 



**Returns:**
 
 - <b>`str`</b>:  The log file name. 


---

<a href="../velocitas_lib/__init__.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_programming_language`

```python
get_programming_language() → str
```

Return the programming language of the project. 


---

<a href="../velocitas_lib/__init__.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_log_file`

```python
create_log_file(service_id: str, runtime_id: str) → TextIOWrapper
```

Create a log file for the given service and runtime. 



**Args:**
 
 - <b>`service_id`</b> (str):  The ID of the service to log. 
 - <b>`runtime_id`</b> (str):  The ID of the runtime to log. 



**Returns:**
 
 - <b>`TextIOWrapper`</b>:  The log file. 


---

<a href="../velocitas_lib/__init__.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `download_file`

```python
download_file(uri: str, local_file_path: str) → None
```






---

<a href="../velocitas_lib/__init__.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_uri`

```python
is_uri(path: str) → bool
```

Check if the provided path is a URI. 



**Args:**
 
 - <b>`path`</b> (str):  The path to check. 



**Returns:**
 
 - <b>`bool`</b>:  True if the path is a URI. False otherwise. 


---

<a href="../velocitas_lib/__init__.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `have_internet_connection`

```python
have_internet_connection() → bool
```






---

<a href="../velocitas_lib/__init__.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `obtain_local_file_path`

```python
obtain_local_file_path(
    path_or_uri: str,
    download_path: Optional[str] = None
) → str
```

Return the absolute path to the file, specified by a absolute/relative local path or with an URI. 



**Args:**
 
 - <b>`path_or_uri`</b> (str):  Absolute/relative local path or URI. 
 - <b>`download_path`</b> (str):  The path to download the file. 



**Returns:**
 
 - <b>`str`</b>:  The absolute path to the file. 


---

<a href="../velocitas_lib/__init__.py#L203"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_zip`

```python
extract_zip(file_path: str, extract_to: str) → str
```

Extract a zip file. 



**Args:**
 
 - <b>`file_path`</b> (str):  The file path to the zip. 
 - <b>`extract_to`</b> (str):  The file path to extract to. 



**Raises:**
 RuntimeError if the file_path is not a zip. 



**Returns:**
 
 - <b>`str`</b>:  The file path to the extracted top level folder. 


---

<a href="../velocitas_lib/__init__.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `discover_files_in_filetree`

```python
discover_files_in_filetree(tree_root: str, file_type: str) → List[str]
```

Recursively search for files with a specific file type under the tree root. 



**Args:**
 
 - <b>`tree_root`</b> (str):  The path to the tree root to search from. 
 - <b>`file_type`</b> (str):  The file type that is searched for. 



**Returns:**
 
 - <b>`List[str]`</b>:  A list of file paths, relative to the search tree root. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
