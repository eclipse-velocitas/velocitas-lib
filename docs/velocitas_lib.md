<!-- markdownlint-disable -->

<a href="../velocitas_lib/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib`





---

<a href="../velocitas_lib/__init__.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_workspace_dir`

```python
get_workspace_dir() → str
```

Return the workspace directory. 


---

<a href="../velocitas_lib/__init__.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_app_manifest`

```python
get_app_manifest() → dict
```






---

<a href="../velocitas_lib/__init__.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_script_path`

```python
get_script_path() → str
```

Return the absolute path to the directory the invoked Python script is located in. 


---

<a href="../velocitas_lib/__init__.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_package_path`

```python
get_package_path() → str
```

Return the absolute path to the package directory the invoked Python script belongs to. 


---

<a href="../velocitas_lib/__init__.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_project_cache_dir`

```python
get_project_cache_dir() → str
```

Return the project's cache directory. 



**Returns:**
 
 - <b>`str`</b>:  The path to the project's cache directory. 


---

<a href="../velocitas_lib/__init__.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_cache_data`

```python
get_cache_data() → Dict[str, Any]
```

Return the data of the cache as Python object. 


---

<a href="../velocitas_lib/__init__.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_programming_language`

```python
get_programming_language() → str
```

Return the programming language of the project. 


---

<a href="../velocitas_lib/__init__.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `download_file`

```python
download_file(uri: str, local_file_path: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
