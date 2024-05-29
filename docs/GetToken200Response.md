# GetToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Authentication token. | [optional] 
**token_type** | **str** | The type of the authentication token. | [optional] 
**expires_in** | **int** | The lifetime (in seconds) of the token. | [optional] 

## Example

```python
from bankable.models.get_token200_response import GetToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetToken200Response from a JSON string
get_token200_response_instance = GetToken200Response.from_json(json)
# print the JSON string representation of the object
print GetToken200Response.to_json()

# convert the object into a dict
get_token200_response_dict = get_token200_response_instance.to_dict()
# create an instance of GetToken200Response from a dict
get_token200_response_form_dict = get_token200_response.from_dict(get_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


