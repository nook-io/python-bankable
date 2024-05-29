# Crn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_number** | **object** | Company registration number. | 
**country_code** | **object** | ISO Country Code (two letter country code from ISO 3166). | 

## Example

```python
from bankable.models.crn import Crn

# TODO update the JSON string below
json = "{}"
# create an instance of Crn from a JSON string
crn_instance = Crn.from_json(json)
# print the JSON string representation of the object
print Crn.to_json()

# convert the object into a dict
crn_dict = crn_instance.to_dict()
# create an instance of Crn from a dict
crn_form_dict = crn.from_dict(crn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


