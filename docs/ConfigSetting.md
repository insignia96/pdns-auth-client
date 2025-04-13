# ConfigSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | set to \&quot;ConfigSetting\&quot; | [optional] 
**type** | **str** | The name of this setting (e.g. ‘webserver-port’) | [optional] 
**value** | **str** | The value of setting name | [optional] 

## Example

```python
from pdns_auth_client.models.config_setting import ConfigSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSetting from a JSON string
config_setting_instance = ConfigSetting.from_json(json)
# print the JSON string representation of the object
print(ConfigSetting.to_json())

# convert the object into a dict
config_setting_dict = config_setting_instance.to_dict()
# create an instance of ConfigSetting from a dict
config_setting_from_dict = ConfigSetting.from_dict(config_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


