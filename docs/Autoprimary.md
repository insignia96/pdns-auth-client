# Autoprimary

An autoprimary server that can provision new domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name for the autoprimary server | [optional] 
**ip** | **str** | IP address of the autoprimary server | [optional] 
**nameserver** | **str** | DNS name of the autoprimary server | [optional] 

## Example

```python
from pdns_auth_client.models.autoprimary import Autoprimary

# TODO update the JSON string below
json = "{}"
# create an instance of Autoprimary from a JSON string
autoprimary_instance = Autoprimary.from_json(json)
# print the JSON string representation of the object
print(Autoprimary.to_json())

# convert the object into a dict
autoprimary_dict = autoprimary_instance.to_dict()
# create an instance of Autoprimary from a dict
autoprimary_from_dict = Autoprimary.from_dict(autoprimary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


