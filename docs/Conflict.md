# Conflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The HTTP status code. | [optional] 
**message** | **object** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**details** | **object** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from bankable.models.conflict import Conflict

# TODO update the JSON string below
json = "{}"
# create an instance of Conflict from a JSON string
conflict_instance = Conflict.from_json(json)
# print the JSON string representation of the object
print Conflict.to_json()

# convert the object into a dict
conflict_dict = conflict_instance.to_dict()
# create an instance of Conflict from a dict
conflict_form_dict = conflict.from_dict(conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


