# NotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The HTTP status code. | [optional] 
**message** | **object** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**details** | **object** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from bankable.models.not_found import NotFound

# TODO update the JSON string below
json = "{}"
# create an instance of NotFound from a JSON string
not_found_instance = NotFound.from_json(json)
# print the JSON string representation of the object
print NotFound.to_json()

# convert the object into a dict
not_found_dict = not_found_instance.to_dict()
# create an instance of NotFound from a dict
not_found_form_dict = not_found.from_dict(not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


