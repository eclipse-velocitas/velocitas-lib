<!-- markdownlint-disable -->

<a href="../velocitas_lib/services.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `velocitas_lib.services`





---

<a href="../velocitas_lib/services.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `resolve_functions`

```python
resolve_functions(input_str: str) → str
```






---

<a href="../velocitas_lib/services.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `parse_service_config`

```python
parse_service_config(
    service_id: str,
    service_spec_config: List[Dict[str, Any]]
) → ServiceSpecConfig
```

Parse service spec configuration and return it as an named tuple. 



**Args:**
 
 - <b>`service_id`</b>:  The ID of the service to be parsed. 
 - <b>`service_spec_config`</b>:  The specificon of the services from config file. 


---

<a href="../velocitas_lib/services.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_services`

```python
get_services(verbose: bool = True) → List[Service]
```

Return all specified services as Python object. 


---

<a href="../velocitas_lib/services.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_specific_service`

```python
get_specific_service(service_id: str) → Service
```

Return the specified service as Python object. 



**Args:**
 
 - <b>`service_id`</b>:  The ID of the service to be parsed. 


---

<a href="../velocitas_lib/services.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_service_port`

```python
get_service_port(service_id: str) → str
```

Return the service port as string for the specified service. 



**Args:**
 
 - <b>`service_id`</b>:  The ID of the service to be parsed. 


---

<a href="../velocitas_lib/services.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ServiceSpecConfig`
ServiceSpecConfig(image, is_enabled, env_vars, args, ports, port_forwards, mounts, startup_log_patterns) 





---

<a href="../velocitas_lib/services.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Service`
Service(id, config) 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
