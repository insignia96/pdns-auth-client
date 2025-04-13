# SearchResultComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**object_type** | **str** | set to \&quot;comment\&quot; | [optional] 
**zone** | **str** |  | [optional] 
**zone_id** | **str** |  | [optional] 

## Example

```python
from pdns_auth_client.models.search_result_comment import SearchResultComment

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultComment from a JSON string
search_result_comment_instance = SearchResultComment.from_json(json)
# print the JSON string representation of the object
print(SearchResultComment.to_json())

# convert the object into a dict
search_result_comment_dict = search_result_comment_instance.to_dict()
# create an instance of SearchResultComment from a dict
search_result_comment_from_dict = SearchResultComment.from_dict(search_result_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


