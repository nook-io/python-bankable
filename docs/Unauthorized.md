# Unauthorized


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The HTTP status code. | [optional] 
**message** | **object** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**details** | **object** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from bankable.models.unauthorized import Unauthorized

# TODO update the JSON string below
json = "{}"
# create an instance of Unauthorized from a JSON string
unauthorized_instance = Unauthorized.from_json(json)
# print the JSON string representation of the object
print Unauthorized.to_json()

# convert the object into a dict
unauthorized_dict = unauthorized_instance.to_dict()
# create an instance of Unauthorized from a dict
unauthorized_form_dict = unauthorized.from_dict(unauthorized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


