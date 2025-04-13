# pdns_auth_client.StatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.


# **get_stats**
> List[GetStats200ResponseInner] get_stats(server_id, statistic=statistic, includerings=includerings)

Query statistics.

Query PowerDNS internal statistics.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_auth_client
from pdns_auth_client.models.get_stats200_response_inner import GetStats200ResponseInner
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
    api_instance = pdns_auth_client.StatsApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    statistic = 'statistic_example' # str | When set to the name of a specific statistic, only this value is returned. If no statistic with that name exists, the response has a 422 status and an error message.  (optional)
    includerings = True # bool | “true” (default) or “false”, whether to include the Ring items, which can contain thousands of log messages or queried domains. Setting this to ”false” may make the response a lot smaller. (optional) (default to True)

    try:
        # Query statistics.
        api_response = api_instance.get_stats(server_id, statistic=statistic, includerings=includerings)
        print("The response of StatsApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **statistic** | **str**| When set to the name of a specific statistic, only this value is returned. If no statistic with that name exists, the response has a 422 status and an error message.  | [optional] 
 **includerings** | **bool**| “true” (default) or “false”, whether to include the Ring items, which can contain thousands of log messages or queried domains. Setting this to ”false” may make the response a lot smaller. | [optional] [default to True]

### Return type

[**List[GetStats200ResponseInner]**](GetStats200ResponseInner.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Statistic Items |  -  |
**400** | The supplied request was not valid |  -  |
**404** | Requested item was not found |  -  |
**422** | Returned when a non-existing statistic name has been requested. Contains an error message |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

