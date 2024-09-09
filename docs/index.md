<!-- markdownlint-disable -->

# API Overview

## Modules

- [`velocitas_lib`](./velocitas_lib.md#module-velocitas_lib)
- [`velocitas_lib.conan_utils`](./velocitas_lib.conan_utils.md#module-velocitas_libconan_utils)
- [`velocitas_lib.docker`](./velocitas_lib.docker.md#module-velocitas_libdocker)
- [`velocitas_lib.functional_interface`](./velocitas_lib.functional_interface.md#module-velocitas_libfunctional_interface)
- [`velocitas_lib.middleware`](./velocitas_lib.middleware.md#module-velocitas_libmiddleware)
- [`velocitas_lib.services`](./velocitas_lib.services.md#module-velocitas_libservices)
- [`velocitas_lib.templates`](./velocitas_lib.templates.md#module-velocitas_libtemplates)
- [`velocitas_lib.text_utils`](./velocitas_lib.text_utils.md#module-velocitas_libtext_utils)
- [`velocitas_lib.variables`](./velocitas_lib.variables.md#module-velocitas_libvariables)

## Classes

- [`middleware.MiddlewareType`](./velocitas_lib.middleware.md#class-middlewaretype): Enumeration containing all possible middleware types.
- [`services.Service`](./velocitas_lib.services.md#class-service): Service(id, config)
- [`services.ServiceSpecConfig`](./velocitas_lib.services.md#class-servicespecconfig): ServiceSpecConfig(image, is_enabled, env_vars, args, ports, port_forwards, mounts, startup_log_patterns)
- [`templates.CopySpec`](./velocitas_lib.templates.md#class-copyspec): Copy specification of a single file or directory.
- [`variables.ProjectVariables`](./velocitas_lib.variables.md#class-projectvariables)

## Functions

- [`velocitas_lib.create_log_file`](./velocitas_lib.md#function-create_log_file): Create a log file for the given service and runtime.
- [`velocitas_lib.discover_files_in_filetree`](./velocitas_lib.md#function-discover_files_in_filetree): Recursively search for files with a specific file type under the tree root.
- [`velocitas_lib.download_file`](./velocitas_lib.md#function-download_file)
- [`velocitas_lib.extract_zip`](./velocitas_lib.md#function-extract_zip): Extract a zip file.
- [`velocitas_lib.get_app_manifest`](./velocitas_lib.md#function-get_app_manifest)
- [`velocitas_lib.get_cache_data`](./velocitas_lib.md#function-get_cache_data): Return the data of the cache as Python object.
- [`velocitas_lib.get_log_file_name`](./velocitas_lib.md#function-get_log_file_name): Build the log file name for the given service and runtime.
- [`velocitas_lib.get_package_path`](./velocitas_lib.md#function-get_package_path): Return the absolute path to the package directory the invoked Python
- [`velocitas_lib.get_programming_language`](./velocitas_lib.md#function-get_programming_language): Return the programming language of the project.
- [`velocitas_lib.get_project_cache_dir`](./velocitas_lib.md#function-get_project_cache_dir): Return the project's cache directory.
- [`velocitas_lib.get_script_path`](./velocitas_lib.md#function-get_script_path): Return the absolute path to the directory the invoked Python script
- [`velocitas_lib.get_valid_arch`](./velocitas_lib.md#function-get_valid_arch): Return a known architecture for the given `arch`.
- [`velocitas_lib.get_workspace_dir`](./velocitas_lib.md#function-get_workspace_dir): Return the workspace directory.
- [`velocitas_lib.have_internet_connection`](./velocitas_lib.md#function-have_internet_connection)
- [`velocitas_lib.is_uri`](./velocitas_lib.md#function-is_uri): Check if the provided path is a URI.
- [`velocitas_lib.obtain_local_file_path`](./velocitas_lib.md#function-obtain_local_file_path): Return the absolute path to the file, specified by a absolute/relative local path or with an URI.
- [`velocitas_lib.require_env`](./velocitas_lib.md#function-require_env): Require and return an environment variable.
- [`conan_utils.add_dependency_to_conanfile`](./velocitas_lib.conan_utils.md#function-add_dependency_to_conanfile): Add the dependency name to the project's list of dependencies.
- [`conan_utils.export_conan_project`](./velocitas_lib.conan_utils.md#function-export_conan_project): Export a conan project to the local conan cache.
- [`conan_utils.get_required_sdk_version`](./velocitas_lib.conan_utils.md#function-get_required_sdk_version): Return the required version of the core SDK.
- [`docker.build_vehicleapp_image`](./velocitas_lib.docker.md#function-build_vehicleapp_image): Build VehicleApp docker image and display the progress using a spinner.
- [`docker.container_exists`](./velocitas_lib.docker.md#function-container_exists): Check if a container with a given name exists.
- [`docker.is_docker_image_build_locally`](./velocitas_lib.docker.md#function-is_docker_image_build_locally): Check if vehicle app docker image is locally available
- [`docker.push_docker_image_to_registry`](./velocitas_lib.docker.md#function-push_docker_image_to_registry): Push docker image to local image registry
- [`functional_interface.get_interfaces_for_type`](./velocitas_lib.functional_interface.md#function-get_interfaces_for_type): Return all interfaces for the given type.
- [`middleware.get_middleware_type`](./velocitas_lib.middleware.md#function-get_middleware_type): Return the current middleware type.
- [`services.get_service_port`](./velocitas_lib.services.md#function-get_service_port): Return the service port as string for the specified service.
- [`services.get_services`](./velocitas_lib.services.md#function-get_services): Return all specified services as Python object.
- [`services.get_specific_service`](./velocitas_lib.services.md#function-get_specific_service): Return the specified service as Python object.
- [`services.parse_service_config`](./velocitas_lib.services.md#function-parse_service_config): Parse service spec configuration and return it as an named tuple.
- [`services.resolve_functions`](./velocitas_lib.services.md#function-resolve_functions)
- [`templates.copy_templates`](./velocitas_lib.templates.md#function-copy_templates): Copy templates from the template dir to the target dir.
- [`text_utils.capture_area_in_file`](./velocitas_lib.text_utils.md#function-capture_area_in_file): Capture an area of a textfile between a matching start line (exclusive) and the first line matching end_line (exclusive).
- [`text_utils.create_truncated_string`](./velocitas_lib.text_utils.md#function-create_truncated_string): Create a truncated version of input if it is longer than length.
- [`text_utils.read_file`](./velocitas_lib.text_utils.md#function-read_file): Reads the file with the given file_path and returns it's content as a str.
- [`text_utils.replace_item_in_list`](./velocitas_lib.text_utils.md#function-replace_item_in_list): Replace the whole line which matches the given text with a replacement.
- [`text_utils.replace_text_area`](./velocitas_lib.text_utils.md#function-replace_text_area): Replace all occurrences of all text areas matching the parameters with a replacement.
- [`text_utils.replace_text_in_file`](./velocitas_lib.text_utils.md#function-replace_text_in_file): Replace all occurrences of text in a file with a replacement.
- [`text_utils.to_camel_case`](./velocitas_lib.text_utils.md#function-to_camel_case): Return a camel case version of a snake case string.
- [`text_utils.write_file`](./velocitas_lib.text_utils.md#function-write_file): Writes the specified content to the specified file_path and returns it's content as a str.
- [`variables.json_obj_to_flat_map`](./velocitas_lib.variables.md#function-json_obj_to_flat_map): Flatten a JSON Object into a one dimensional dict by joining the keys


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
