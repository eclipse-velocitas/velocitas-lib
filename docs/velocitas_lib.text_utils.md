<!-- markdownlint-disable -->

<a href="../velocitas_lib/text_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.text_utils`





---

<a href="../velocitas_lib/text_utils.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../velocitas_lib/text_utils.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
