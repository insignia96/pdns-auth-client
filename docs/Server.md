# Server


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_url** | **str** | The API endpoint for this server’s configuration | [optional] 
**daemon_type** | **str** | “recursor” for the PowerDNS Recursor and “authoritative” for the Authoritative Server | [optional] 
**id** | **str** | The id of the server, “localhost” | [optional] 
**type** | **str** | Set to “Server” | [optional] 
**url** | **str** | The API endpoint for this server | [optional] 
**version** | **str** | The version of the server software | [optional] 
**zones_url** | **str** | The API endpoint for this server’s zones | [optional] 

## Example

```python
from pdns_auth_client.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


