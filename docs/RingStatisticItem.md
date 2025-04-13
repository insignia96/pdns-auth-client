# RingStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name | [optional] 
**size** | **int** | Ring size | [optional] 
**type** | **str** | Set to \&quot;RingStatisticItem\&quot; | [optional] 
**value** | [**List[SimpleStatisticItem]**](SimpleStatisticItem.md) | Named values | [optional] 

## Example

```python
from pdns_auth_client.models.ring_statistic_item import RingStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of RingStatisticItem from a JSON string
ring_statistic_item_instance = RingStatisticItem.from_json(json)
# print the JSON string representation of the object
print(RingStatisticItem.to_json())

# convert the object into a dict
ring_statistic_item_dict = ring_statistic_item_instance.to_dict()
# create an instance of RingStatisticItem from a dict
ring_statistic_item_from_dict = RingStatisticItem.from_dict(ring_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


