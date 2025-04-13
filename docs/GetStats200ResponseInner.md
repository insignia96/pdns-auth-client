# GetStats200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name | [optional] 
**type** | **str** | Set to \&quot;RingStatisticItem\&quot; | [optional] 
**value** | [**List[SimpleStatisticItem]**](SimpleStatisticItem.md) | Named values | [optional] 
**size** | **int** | Ring size | [optional] 

## Example

```python
from pdns_auth_client.models.get_stats200_response_inner import GetStats200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStats200ResponseInner from a JSON string
get_stats200_response_inner_instance = GetStats200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetStats200ResponseInner.to_json())

# convert the object into a dict
get_stats200_response_inner_dict = get_stats200_response_inner_instance.to_dict()
# create an instance of GetStats200ResponseInner from a dict
get_stats200_response_inner_from_dict = GetStats200ResponseInner.from_dict(get_stats200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


