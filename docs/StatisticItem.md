# StatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name | [optional] 
**type** | **str** | set to \&quot;StatisticItem\&quot; | [optional] 
**value** | **str** | Item value | [optional] 

## Example

```python
from pdns_auth_client.models.statistic_item import StatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticItem from a JSON string
statistic_item_instance = StatisticItem.from_json(json)
# print the JSON string representation of the object
print(StatisticItem.to_json())

# convert the object into a dict
statistic_item_dict = statistic_item_instance.to_dict()
# create an instance of StatisticItem from a dict
statistic_item_from_dict = StatisticItem.from_dict(statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


