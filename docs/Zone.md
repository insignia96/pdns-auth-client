# Zone

This represents an authoritative DNS Zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | MAY be set. Its value is defined by local policy | [optional] 
**api_rectify** | **bool** | Whether or not the zone will be rectified on data changes via the API | [optional] 
**catalog** | **str** | The catalog this zone is a member of | [optional] 
**dnssec** | **bool** | Whether or not this zone is DNSSEC signed (inferred from presigned being true XOR presence of at least one cryptokey with active being true) | [optional] 
**edited_serial** | **int** | The SOA serial as seen in query responses. Calculated using the SOA-EDIT metadata, default-soa-edit and default-soa-edit-signed settings | [optional] 
**id** | **str** | Opaque zone id (string), assigned by the server, should not be interpreted by the application. Guaranteed to be safe for embedding in URLs. | [optional] 
**kind** | **str** | Zone kind, one of “Native”, “Master”, “Slave”, “Producer”, “Consumer” | [optional] 
**master_tsig_key_ids** | **List[str]** | The id of the TSIG keys used for master operation in this zone | [optional] 
**masters** | **List[str]** |  List of IP addresses configured as a master for this zone (“Slave” type zones only) | [optional] 
**name** | **str** | Name of the zone (e.g. “example.com.”) MUST have a trailing dot | [optional] 
**nameservers** | **List[str]** | MAY be sent in client bodies during creation, and MUST NOT be sent by the server. Simple list of strings of nameserver names, including the trailing dot. Not required for slave zones. | [optional] 
**notified_serial** | **int** | The SOA serial notifications have been sent out for | [optional] 
**nsec3narrow** | **bool** | Whether or not the zone uses NSEC3 narrow | [optional] 
**nsec3param** | **str** | The NSEC3PARAM record | [optional] 
**presigned** | **bool** | Whether or not the zone is pre-signed | [optional] 
**rrsets** | [**List[RRSet]**](RRSet.md) | RRSets in this zone (for zones/{zone_id} endpoint only; omitted during GET on the .../zones list endpoint) | [optional] 
**serial** | **int** | The SOA serial number | [optional] 
**slave_tsig_key_ids** | **List[str]** | The id of the TSIG keys used for slave operation in this zone | [optional] 
**soa_edit** | **str** | The SOA-EDIT metadata item | [optional] 
**soa_edit_api** | **str** | The SOA-EDIT-API metadata item | [optional] 
**type** | **str** | Set to “Zone” | [optional] 
**url** | **str** | API endpoint for this zone | [optional] 
**zone** | **str** | MAY contain a BIND-style zone file when creating a zone | [optional] 

## Example

```python
from pdns_auth_client.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print(Zone.to_json())

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_from_dict = Zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


