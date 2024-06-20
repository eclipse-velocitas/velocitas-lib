<!-- markdownlint-disable -->

<a href="../velocitas_lib/text_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.text_utils`





---

<a href="../velocitas_lib/text_utils.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `replace_item_in_list`

```python
replace_item_in_list(
    text: List[str],
    matching_text: str,
    replacement: str = '',
    remove_empty: bool = False
) → List[str]
```

Replace the whole line which matches the given text with a replacement. 



**Args:**
 
 - <b>`text`</b> (List[str]):  All text lines to replace lines within. 
 - <b>`text`</b> (str):  The text to find the line with. 
 - <b>`replacement`</b> (str):  The replacement for line. 
 - <b>`remove_empty`</b> (bool):  If true and the replacement for a line is empty, the line will be removed. 


---

<a href="../velocitas_lib/text_utils.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `replace_text_area`

```python
replace_text_area(
    text: List[str],
    start_occurence: str,
    end_occurence: str,
    replacement: str = ''
) → List[str]
```

Replace all occurrences of all text areas matching the parameters with a replacement. If the replacement for a line is empty, then the line will be removed. 



**Args:**
 
 - <b>`text`</b> (List[str]):  All text lines to replace text within. 
 - <b>`start_occurence`</b> (str):  The starting line which matches the occurence for replacement text area. 
 - <b>`start_occurence`</b> (str):  The ending line which matches the occurence for replacement text area. 
 - <b>`replacement`</b> (str):  The replacement for text area. 


---

<a href="../velocitas_lib/text_utils.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
