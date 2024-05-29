# FindCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** | List of paginated credits. | [optional] 

## Example

```python
from bankable.models.find_credits200_response import FindCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindCredits200Response from a JSON string
find_credits200_response_instance = FindCredits200Response.from_json(json)
# print the JSON string representation of the object
print FindCredits200Response.to_json()

# convert the object into a dict
find_credits200_response_dict = find_credits200_response_instance.to_dict()
# create an instance of FindCredits200Response from a dict
find_credits200_response_form_dict = find_credits200_response.from_dict(find_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


