# GetFinancingIndicator200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility_status** | **object** | Eligibilty Status of the payable. | [optional] 
**financing_indicator** | [**GetFinancingIndicator200ResponseFinancingIndicator**](GetFinancingIndicator200ResponseFinancingIndicator.md) |  | [optional] 

## Example

```python
from bankable.models.get_financing_indicator200_response import GetFinancingIndicator200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFinancingIndicator200Response from a JSON string
get_financing_indicator200_response_instance = GetFinancingIndicator200Response.from_json(json)
# print the JSON string representation of the object
print GetFinancingIndicator200Response.to_json()

# convert the object into a dict
get_financing_indicator200_response_dict = get_financing_indicator200_response_instance.to_dict()
# create an instance of GetFinancingIndicator200Response from a dict
get_financing_indicator200_response_form_dict = get_financing_indicator200_response.from_dict(get_financing_indicator200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


