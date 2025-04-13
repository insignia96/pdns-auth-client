# SimpleStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name | [optional] 
**value** | **str** | Item value | [optional] 

## Example

```python
from pdns_auth_client.models.simple_statistic_item import SimpleStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleStatisticItem from a JSON string
simple_statistic_item_instance = SimpleStatisticItem.from_json(json)
# print the JSON string representation of the object
print(SimpleStatisticItem.to_json())

# convert the object into a dict
simple_statistic_item_dict = simple_statistic_item_instance.to_dict()
# create an instance of SimpleStatisticItem from a dict
simple_statistic_item_from_dict = SimpleStatisticItem.from_dict(simple_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


