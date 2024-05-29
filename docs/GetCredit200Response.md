# GetCredit200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | [**GetCredit200ResponseCredit**](GetCredit200ResponseCredit.md) |  | [optional] 
**client** | [**GetCredit200ResponseClient**](GetCredit200ResponseClient.md) |  | [optional] 
**installments** | **object** | List of instalments. | [optional] 

## Example

```python
from bankable.models.get_credit200_response import GetCredit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredit200Response from a JSON string
get_credit200_response_instance = GetCredit200Response.from_json(json)
# print the JSON string representation of the object
print GetCredit200Response.to_json()

# convert the object into a dict
get_credit200_response_dict = get_credit200_response_instance.to_dict()
# create an instance of GetCredit200Response from a dict
get_credit200_response_form_dict = get_credit200_response.from_dict(get_credit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


