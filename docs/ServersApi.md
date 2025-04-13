# pdns_auth_client.ServersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cache_flush_by_name**](ServersApi.md#cache_flush_by_name) | **PUT** /servers/{server_id}/cache/flush | Flush a cache-entry by name
[**list_server**](ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
[**list_servers**](ServersApi.md#list_servers) | **GET** /servers | List all servers


# **cache_flush_by_name**
> CacheFlushResult cache_flush_by_name(server_id, domain)

Flush a cache-entry by name

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.cache_flush_result import CacheFlushResult
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
    api_instance = pdns_auth_client.ServersApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    domain = 'domain_example' # str | The domain name to flush from the cache

    try:
        # Flush a cache-entry by name
        api_response = api_instance.cache_flush_by_name(server_id, domain)
        print("The response of ServersApi->cache_flush_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->cache_flush_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **domain** | **str**| The domain name to flush from the cache | 

### Return type

[**CacheFlushResult**](CacheFlushResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flush successful |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_server**
> Server list_server(server_id)

List a server

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.server import Server
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
    api_instance = pdns_auth_client.ServersApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve

    try:
        # List a server
        api_response = api_instance.list_server(server_id)
        print("The response of ServersApi->list_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->list_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**Server**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An server |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_servers**
> List[Server] list_servers()

List all servers

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.server import Server
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
    api_instance = pdns_auth_client.ServersApi(api_client)

    try:
        # List all servers
        api_response = api_instance.list_servers()
        print("The response of ServersApi->list_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->list_servers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Server]**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of servers |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

