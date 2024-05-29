# BaseError

The Problem Details JSON Object [[RFC7807](https://tools.ietf.org/html/rfc7807)].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | The HTTP status code. | [optional] 
**message** | **object** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**details** | **object** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from bankable.models.base_error import BaseError

# TODO update the JSON string below
json = "{}"
# create an instance of BaseError from a JSON string
base_error_instance = BaseError.from_json(json)
# print the JSON string representation of the object
print BaseError.to_json()

# convert the object into a dict
base_error_dict = base_error_instance.to_dict()
# create an instance of BaseError from a dict
base_error_form_dict = base_error.from_dict(base_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


