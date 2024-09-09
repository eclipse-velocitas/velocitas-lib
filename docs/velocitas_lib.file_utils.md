<!-- markdownlint-disable -->

<a href="../velocitas_lib/file_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.file_utils`





---

<a href="../velocitas_lib/file_utils.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `replace_text_in_file`

```python
replace_text_in_file(file_path: str, text: str, replacement: str) → None
```

Replace all occurrences of text in a file with a replacement. 



**Args:**
 
 - <b>`file_path`</b> (str):  The path to the file. 
 - <b>`text`</b> (str):  The text to find. 
 - <b>`replacement`</b> (str):  The replacement for text. 


---

<a href="../velocitas_lib/file_utils.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `capture_area_in_file`

```python
capture_area_in_file(
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

<a href="../velocitas_lib/file_utils.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_file`

```python
read_file(file_path: str) → Optional[str]
```

Reads the file with the given file_path and returns it's content as a str. 



**Args:**
 
 - <b>`file_path`</b> (str):  the file_path of the file to read. 



**Returns:**
 
 - <b>`str`</b>:  the content of the specified file. 


---

<a href="../velocitas_lib/file_utils.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_file`

```python
write_file(file_path: str, content: str) → bool
```

Writes the content to the file_path and returns the success of the write operation. 



**Args:**
 
 - <b>`file_path`</b> (str):  the file_path of the file to write. 
 - <b>`content`</b> (str):  the content to be written to the file. 



**Returns:**
 
 - <b>`bool`</b>:  True if writing was successful, False otherwise. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
