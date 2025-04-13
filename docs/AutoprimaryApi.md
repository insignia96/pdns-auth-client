# pdns_auth_client.AutoprimaryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_autoprimary**](AutoprimaryApi.md#create_autoprimary) | **POST** /servers/{server_id}/autoprimaries | Add an autoprimary
[**delete_autoprimary**](AutoprimaryApi.md#delete_autoprimary) | **DELETE** /servers/{server_id}/autoprimaries/{ip}/{nameserver} | Delete the autoprimary entry
[**get_autoprimaries**](AutoprimaryApi.md#get_autoprimaries) | **GET** /servers/{server_id}/autoprimaries | Get a list of autoprimaries


# **create_autoprimary**
> create_autoprimary(server_id, autoprimary)

Add an autoprimary

This methods add a new autoprimary server.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.autoprimary import Autoprimary
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
    api_instance = pdns_auth_client.AutoprimaryApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on
    autoprimary = pdns_auth_client.Autoprimary() # Autoprimary | autoprimary entry to add

    try:
        # Add an autoprimary
        api_instance.create_autoprimary(server_id, autoprimary)
    except Exception as e:
        print("Exception when calling AutoprimaryApi->create_autoprimary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to manage the list of autoprimaries on | 
 **autoprimary** | [**Autoprimary**](Autoprimary.md)| autoprimary entry to add | 

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
**201** | Created |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_autoprimary**
> delete_autoprimary(server_id, ip, nameserver)

Delete the autoprimary entry

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
    api_instance = pdns_auth_client.AutoprimaryApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to delete the autoprimary from
    ip = 'ip_example' # str | IP address of autoprimary
    nameserver = 'nameserver_example' # str | DNS name of the autoprimary

    try:
        # Delete the autoprimary entry
        api_instance.delete_autoprimary(server_id, ip, nameserver)
    except Exception as e:
        print("Exception when calling AutoprimaryApi->delete_autoprimary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to delete the autoprimary from | 
 **ip** | **str**| IP address of autoprimary | 
 **nameserver** | **str**| DNS name of the autoprimary | 

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
**204** | OK, key was deleted |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autoprimaries**
> Autoprimary get_autoprimaries(server_id)

Get a list of autoprimaries

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.autoprimary import Autoprimary
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
    api_instance = pdns_auth_client.AutoprimaryApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to manage the list of autoprimaries on

    try:
        # Get a list of autoprimaries
        api_response = api_instance.get_autoprimaries(server_id)
        print("The response of AutoprimaryApi->get_autoprimaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoprimaryApi->get_autoprimaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to manage the list of autoprimaries on | 

### Return type

[**Autoprimary**](Autoprimary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

