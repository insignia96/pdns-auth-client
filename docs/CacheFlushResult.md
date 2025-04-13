# CacheFlushResult

The result of a cache-flush

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** | Amount of entries flushed | [optional] 
**result** | **str** | A message about the result like \&quot;Flushed cache\&quot; | [optional] 

## Example

```python
from pdns_auth_client.models.cache_flush_result import CacheFlushResult

# TODO update the JSON string below
json = "{}"
# create an instance of CacheFlushResult from a JSON string
cache_flush_result_instance = CacheFlushResult.from_json(json)
# print the JSON string representation of the object
print(CacheFlushResult.to_json())

# convert the object into a dict
cache_flush_result_dict = cache_flush_result_instance.to_dict()
# create an instance of CacheFlushResult from a dict
cache_flush_result_from_dict = CacheFlushResult.from_dict(cache_flush_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


