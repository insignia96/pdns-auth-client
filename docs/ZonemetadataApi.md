# pdns_auth_client.ZonemetadataApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata**](ZonemetadataApi.md#create_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
[**delete_metadata**](ZonemetadataApi.md#delete_metadata) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
[**get_metadata**](ZonemetadataApi.md#get_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a Metadata object.
[**list_metadata**](ZonemetadataApi.md#list_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the Metadata associated with the zone.
[**modify_metadata**](ZonemetadataApi.md#modify_metadata) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Replace the content of a single kind of domain metadata.


# **create_metadata**
> create_metadata(server_id, zone_id, metadata)

Creates a set of metadata entries

Creates a set of metadata entries of given kind for the zone. Existing metadata entries for the zone with the same kind are not overwritten.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.metadata import Metadata
from pdns_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_auth_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_auth_client.ZonemetadataApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | 
    metadata = pdns_auth_client.Metadata() # Metadata | Metadata object with list of values to create

    try:
        # Creates a set of metadata entries
        api_instance.create_metadata(server_id, zone_id, metadata)
    except Exception as e:
        print("Exception when calling ZonemetadataApi->create_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata** | [**Metadata**](Metadata.md)| Metadata object with list of values to create | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata**
> delete_metadata(server_id, zone_id, metadata_kind)

Delete all items of a single kind of domain metadata.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_auth_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_auth_client.ZonemetadataApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve
    metadata_kind = 'metadata_kind_example' # str | The kind of metadata

    try:
        # Delete all items of a single kind of domain metadata.
        api_instance.delete_metadata(server_id, zone_id, metadata_kind)
    except Exception as e:
        print("Exception when calling ZonemetadataApi->delete_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| The kind of metadata | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> Metadata get_metadata(server_id, zone_id, metadata_kind)

Get the content of a single kind of domain metadata as a Metadata object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.metadata import Metadata
from pdns_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_auth_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_auth_client.ZonemetadataApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve
    metadata_kind = 'metadata_kind_example' # str | The kind of metadata

    try:
        # Get the content of a single kind of domain metadata as a Metadata object.
        api_response = api_instance.get_metadata(server_id, zone_id, metadata_kind)
        print("The response of ZonemetadataApi->get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonemetadataApi->get_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| The kind of metadata | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata object with list of values |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata**
> List[Metadata] list_metadata(server_id, zone_id)

Get all the Metadata associated with the zone.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.metadata import Metadata
from pdns_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_auth_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_auth_client.ZonemetadataApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Get all the Metadata associated with the zone.
        api_response = api_instance.list_metadata(server_id, zone_id)
        print("The response of ZonemetadataApi->list_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonemetadataApi->list_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**List[Metadata]**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Metadata objects |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_metadata**
> Metadata modify_metadata(server_id, zone_id, metadata_kind, metadata)

Replace the content of a single kind of domain metadata.

Creates a set of metadata entries of given kind for the zone. Existing metadata entries for the zone with the same kind are removed.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.metadata import Metadata
from pdns_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_auth_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_auth_client.ZonemetadataApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | 
    metadata_kind = 'metadata_kind_example' # str | The kind of metadata
    metadata = pdns_auth_client.Metadata() # Metadata | metadata to add/create

    try:
        # Replace the content of a single kind of domain metadata.
        api_response = api_instance.modify_metadata(server_id, zone_id, metadata_kind, metadata)
        print("The response of ZonemetadataApi->modify_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonemetadataApi->modify_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata_kind** | **str**| The kind of metadata | 
 **metadata** | [**Metadata**](Metadata.md)| metadata to add/create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata object with list of values |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

