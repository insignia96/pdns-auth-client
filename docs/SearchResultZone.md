# SearchResultZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**object_type** | **str** | set to \&quot;zone\&quot; | [optional] 
**zone_id** | **str** |  | [optional] 

## Example

```python
from pdns_auth_client.models.search_result_zone import SearchResultZone

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultZone from a JSON string
search_result_zone_instance = SearchResultZone.from_json(json)
# print the JSON string representation of the object
print(SearchResultZone.to_json())

# convert the object into a dict
search_result_zone_dict = search_result_zone_instance.to_dict()
# create an instance of SearchResultZone from a dict
search_result_zone_from_dict = SearchResultZone.from_dict(search_result_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


