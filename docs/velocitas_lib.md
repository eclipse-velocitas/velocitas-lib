<!-- markdownlint-disable -->

<a href="../velocitas_lib/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib`





---

<a href="../velocitas_lib/__init__.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_camel_case`

```python
to_camel_case(snake_str: str) → str
```

Return a camel case version of a snake case string. 



**Args:**
 
 - <b>`snake_str`</b> (str):  A snake case string. 



**Returns:**
 
 - <b>`str`</b>:  A camel case version of a snake case string. 


---

<a href="../velocitas_lib/__init__.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_truncated_string`

```python
create_truncated_string(input: str, length: int) → str
```

Create a truncated version of input if it is longer than length. Will keep the rightmost characters and cut of the front if it is longer than allowed. 



**Args:**
 
 - <b>`input`</b> (str):  The input string. 
 - <b>`length`</b> (int):  The allowed overall length. 



**Returns:**
 
 - <b>`str`</b>:  A truncated string which has len() of length. 


---

<a href="../velocitas_lib/__init__.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `replace_in_file`

```python
replace_in_file(file_path: str, text: str, replacement: str) → None
```

Replace all occurrences of text in a file with a replacement. 



**Args:**
 
 - <b>`file_path`</b> (str):  The path to the file. 
 - <b>`text`</b> (str):  The text to find. 
 - <b>`replacement`</b> (str):  The replacement for text. 


---

<a href="../velocitas_lib/__init__.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `capture_textfile_area`

```python
capture_textfile_area(
    file: TextIOWrapper,
    start_line: str,
    end_line: str,
    map_fn: Optional[Callable[[str], str]] = None
) → List[str]
```

Capture an area of a textfile between a matching start line (exclusive) and the first line matching end_line (exclusive). 



**Args:**
 
 - <b>`file`</b> (TextIOWrapper):  The text file to read from. 
 - <b>`start_line`</b> (str):  The line which triggers the capture (will not be part of the output) 
 - <b>`end_line`</b> (str):  The line which terminates the capture (will not be bart of the output) 
 - <b>`map_fn`</b> (Optional[Callable[[str], str]], optional):  An optional mapping function to transform captured lines. Defaults to None. 



**Returns:**
 
 - <b>`List[str]`</b>:  A list of captured lines. 


---

<a href="../velocitas_lib/__init__.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_workspace_dir`

```python
get_workspace_dir() → str
```

Return the workspace directory. 


---

<a href="../velocitas_lib/__init__.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_app_manifest`

```python
get_app_manifest() → Dict[str, Any]
```






---

<a href="../velocitas_lib/__init__.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_script_path`

```python
get_script_path() → str
```

Return the absolute path to the directory the invoked Python script is located in. 


---

<a href="../velocitas_lib/__init__.py#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_package_path`

```python
get_package_path() → str
```

Return the absolute path to the package directory the invoked Python script belongs to. 


---

<a href="../velocitas_lib/__init__.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_project_cache_dir`

```python
get_project_cache_dir() → str
```

Return the project's cache directory. 



**Returns:**
 
 - <b>`str`</b>:  The path to the project's cache directory. 


---

<a href="../velocitas_lib/__init__.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_cache_data`

```python
get_cache_data() → Dict[str, Any]
```

Return the data of the cache as Python object. 


---

<a href="../velocitas_lib/__init__.py#L186"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_programming_language`

```python
get_programming_language() → str
```

Return the programming language of the project. 


---

<a href="../velocitas_lib/__init__.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/__init__.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `download_file`

```python
download_file(uri: str, local_file_path: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
