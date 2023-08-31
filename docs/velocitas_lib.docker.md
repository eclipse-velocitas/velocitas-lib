<!-- markdownlint-disable -->

<a href="../velocitas_lib/docker.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.docker`





---

<a href="../velocitas_lib/docker.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `build_vehicleapp_image`

```python
build_vehicleapp_image(log_output: TextIOWrapper | int = -3) → None
```

Build VehicleApp docker image and display the progress using a spinner. 



**Args:**
 
 - <b>`log_output`</b> (TextIOWrapper | int):  Logfile to write or DEVNULL by default. 


---

<a href="../velocitas_lib/docker.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_docker_image_build_locally`

```python
is_docker_image_build_locally(app_name: str) → bool
```

Check if vehicle app docker image is locally available 



**Args:**
 
 - <b>`app_name`</b> (str):  App name to check for 


---

<a href="../velocitas_lib/docker.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `push_docker_image_to_registry`

```python
push_docker_image_to_registry(
    app_name: str,
    log_output: TextIOWrapper | int = -3
) → None
```

Push docker image to local image registry 



**Args:**
 
 - <b>`app_name`</b> (str):  App name to push to registry 
 - <b>`log_output`</b> (TextIOWrapper | int):  Logfile to write or DEVNULL by default. 


---

<a href="../velocitas_lib/docker.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `container_exists`

```python
container_exists(name: str, log_output: TextIOWrapper | int = -3) → bool
```

Check if a container with a given name exists. 



**Args:**
 
 - <b>`log_output`</b> (TextIOWrapper | int):  Logfile to write or DEVNULL by default. 



**Returns:**
 
 - <b>`bool`</b>:  True if the container exists, False if not. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
