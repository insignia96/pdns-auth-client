# MapStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name | [optional] 
**type** | **str** | Set to \&quot;MapStatisticItem\&quot; | [optional] 
**value** | [**List[SimpleStatisticItem]**](SimpleStatisticItem.md) | Named values | [optional] 

## Example

```python
from pdns_auth_client.models.map_statistic_item import MapStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapStatisticItem from a JSON string
map_statistic_item_instance = MapStatisticItem.from_json(json)
# print the JSON string representation of the object
print(MapStatisticItem.to_json())

# convert the object into a dict
map_statistic_item_dict = map_statistic_item_instance.to_dict()
# create an instance of MapStatisticItem from a dict
map_statistic_item_from_dict = MapStatisticItem.from_dict(map_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


