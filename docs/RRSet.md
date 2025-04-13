# RRSet

This represents a Resource Record Set (all records with the same name and type).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changetype** | **str** | MUST be added when updating the RRSet. Must be REPLACE or DELETE. With DELETE, all existing RRs matching name and type will be deleted, including all comments. With REPLACE: when records is present, all existing RRs matching name and type will be deleted, and then new records given in records will be created. If no records are left, any existing comments will be deleted as well. When comments is present, all existing comments for the RRs matching name and type will be deleted, and then new comments given in comments will be created. | [optional] 
**comments** | [**List[Comment]**](Comment.md) | List of Comment. Must be empty when changetype is set to DELETE. An empty list results in deletion of all comments. modified_at is optional and defaults to the current server time. | [optional] 
**name** | **str** | Name for record set (e.g. “www.powerdns.com.”) | 
**records** | [**List[Record]**](Record.md) | All records in this RRSet. When updating Records, this is the list of new records (replacing the old ones). Must be empty when changetype is set to DELETE. An empty list results in deletion of all records (and comments). | 
**ttl** | **int** | DNS TTL of the records, in seconds. MUST NOT be included when changetype is set to “DELETE”. | [optional] 
**type** | **str** | Type of this record (e.g. “A”, “PTR”, “MX”) | 

## Example

```python
from pdns_auth_client.models.rr_set import RRSet

# TODO update the JSON string below
json = "{}"
# create an instance of RRSet from a JSON string
rr_set_instance = RRSet.from_json(json)
# print the JSON string representation of the object
print(RRSet.to_json())

# convert the object into a dict
rr_set_dict = rr_set_instance.to_dict()
# create an instance of RRSet from a dict
rr_set_from_dict = RRSet.from_dict(rr_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


