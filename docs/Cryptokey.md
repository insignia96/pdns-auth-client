# Cryptokey

Describes a DNSSEC cryptographic key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the key is in active use | [optional] 
**algorithm** | **str** | The name of the algorithm of the key, should be a mnemonic | [optional] 
**bits** | **int** | The size of the key | [optional] 
**cds** | **List[str]** | An array of DS records for this key, filtered by CDS publication settings | [optional] 
**dnskey** | **str** | The DNSKEY record for this key | [optional] 
**ds** | **List[str]** | An array of DS records for this key | [optional] 
**id** | **int** | The internal identifier, read only | [optional] 
**keytype** | **str** |  | [optional] 
**privatekey** | **str** | The private key in ISC format | [optional] 
**published** | **bool** | Whether or not the DNSKEY record is published in the zone | [optional] 
**type** | **str** | set to \&quot;Cryptokey\&quot; | [optional] 

## Example

```python
from pdns_auth_client.models.cryptokey import Cryptokey

# TODO update the JSON string below
json = "{}"
# create an instance of Cryptokey from a JSON string
cryptokey_instance = Cryptokey.from_json(json)
# print the JSON string representation of the object
print(Cryptokey.to_json())

# convert the object into a dict
cryptokey_dict = cryptokey_instance.to_dict()
# create an instance of Cryptokey from a dict
cryptokey_from_dict = Cryptokey.from_dict(cryptokey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


