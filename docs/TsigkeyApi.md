# pdns_auth_client.TsigkeyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tsig_key**](TsigkeyApi.md#create_tsig_key) | **POST** /servers/{server_id}/tsigkeys | Add a TSIG key
[**delete_tsig_key**](TsigkeyApi.md#delete_tsig_key) | **DELETE** /servers/{server_id}/tsigkeys/{tsigkey_id} | Delete the TSIGKey with tsigkey_id
[**get_tsig_key**](TsigkeyApi.md#get_tsig_key) | **GET** /servers/{server_id}/tsigkeys/{tsigkey_id} | Get a specific TSIGKeys on the server, including the actual key
[**list_tsig_keys**](TsigkeyApi.md#list_tsig_keys) | **GET** /servers/{server_id}/tsigkeys | Get all TSIGKeys on the server, except the actual key
[**put_tsig_key**](TsigkeyApi.md#put_tsig_key) | **PUT** /servers/{server_id}/tsigkeys/{tsigkey_id} | 


# **create_tsig_key**
> TSIGKey create_tsig_key(server_id, tsig_key)

Add a TSIG key

This methods add a new TSIGKey. The actual key can be generated by the server or be provided by the client

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.tsig_key import TSIGKey
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
    api_instance = pdns_auth_client.TsigkeyApi(api_client)
    server_id = 'server_id_example' # str | The id of the server
    tsig_key = pdns_auth_client.TSIGKey() # TSIGKey | The TSIGKey to add

    try:
        # Add a TSIG key
        api_response = api_instance.create_tsig_key(server_id, tsig_key)
        print("The response of TsigkeyApi->create_tsig_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TsigkeyApi->create_tsig_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server | 
 **tsig_key** | [**TSIGKey**](TSIGKey.md)| The TSIGKey to add | 

### Return type

[**TSIGKey**](TSIGKey.md)

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
**409** | An item with this name already exists |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tsig_key**
> delete_tsig_key(server_id, tsigkey_id)

Delete the TSIGKey with tsigkey_id

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
    api_instance = pdns_auth_client.TsigkeyApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve the key from
    tsigkey_id = 'tsigkey_id_example' # str | The id of the TSIGkey. Should match the \"id\" field in the TSIGKey object

    try:
        # Delete the TSIGKey with tsigkey_id
        api_instance.delete_tsig_key(server_id, tsigkey_id)
    except Exception as e:
        print("Exception when calling TsigkeyApi->delete_tsig_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve the key from | 
 **tsigkey_id** | **str**| The id of the TSIGkey. Should match the \&quot;id\&quot; field in the TSIGKey object | 

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

# **get_tsig_key**
> TSIGKey get_tsig_key(server_id, tsigkey_id)

Get a specific TSIGKeys on the server, including the actual key

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.tsig_key import TSIGKey
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
    api_instance = pdns_auth_client.TsigkeyApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve the key from
    tsigkey_id = 'tsigkey_id_example' # str | The id of the TSIGkey. Should match the \"id\" field in the TSIGKey object

    try:
        # Get a specific TSIGKeys on the server, including the actual key
        api_response = api_instance.get_tsig_key(server_id, tsigkey_id)
        print("The response of TsigkeyApi->get_tsig_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TsigkeyApi->get_tsig_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve the key from | 
 **tsigkey_id** | **str**| The id of the TSIGkey. Should match the \&quot;id\&quot; field in the TSIGKey object | 

### Return type

[**TSIGKey**](TSIGKey.md)

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

# **list_tsig_keys**
> List[TSIGKey] list_tsig_keys(server_id)

Get all TSIGKeys on the server, except the actual key

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.tsig_key import TSIGKey
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
    api_instance = pdns_auth_client.TsigkeyApi(api_client)
    server_id = 'server_id_example' # str | The id of the server

    try:
        # Get all TSIGKeys on the server, except the actual key
        api_response = api_instance.list_tsig_keys(server_id)
        print("The response of TsigkeyApi->list_tsig_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TsigkeyApi->list_tsig_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server | 

### Return type

[**List[TSIGKey]**](TSIGKey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TSIGKey objects |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tsig_key**
> TSIGKey put_tsig_key(server_id, tsigkey_id, tsig_key)



The TSIGKey at tsigkey_id can be changed in multiple ways:  * Changing the Name, this will remove the key with tsigkey_id after adding.  * Changing the Algorithm  * Changing the Key  Only the relevant fields have to be provided in the request body. 

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.tsig_key import TSIGKey
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
    api_instance = pdns_auth_client.TsigkeyApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve the key from
    tsigkey_id = 'tsigkey_id_example' # str | The id of the TSIGkey. Should match the \"id\" field in the TSIGKey object
    tsig_key = pdns_auth_client.TSIGKey() # TSIGKey | A (possibly stripped down) TSIGKey object with the new values

    try:
        api_response = api_instance.put_tsig_key(server_id, tsigkey_id, tsig_key)
        print("The response of TsigkeyApi->put_tsig_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TsigkeyApi->put_tsig_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve the key from | 
 **tsigkey_id** | **str**| The id of the TSIGkey. Should match the \&quot;id\&quot; field in the TSIGKey object | 
 **tsig_key** | [**TSIGKey**](TSIGKey.md)| A (possibly stripped down) TSIGKey object with the new values | 

### Return type

[**TSIGKey**](TSIGKey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. TSIGKey is changed. |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**409** | An item with this name already exists |  -  |
**422** | The input to the operation was not valid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

