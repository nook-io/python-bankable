# Internal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The HTTP status code. | [optional] 
**message** | **object** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**details** | **object** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from bankable.models.internal import Internal

# TODO update the JSON string below
json = "{}"
# create an instance of Internal from a JSON string
internal_instance = Internal.from_json(json)
# print the JSON string representation of the object
print Internal.to_json()

# convert the object into a dict
internal_dict = internal_instance.to_dict()
# create an instance of Internal from a dict
internal_form_dict = internal.from_dict(internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


