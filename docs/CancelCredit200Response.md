# CancelCredit200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_id** | **object** | The Credit ID provided by Bankable. | [optional] 
**state** | **object** | The state of the Credit after cancellation. | [optional] 

## Example

```python
from bankable.models.cancel_credit200_response import CancelCredit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCredit200Response from a JSON string
cancel_credit200_response_instance = CancelCredit200Response.from_json(json)
# print the JSON string representation of the object
print CancelCredit200Response.to_json()

# convert the object into a dict
cancel_credit200_response_dict = cancel_credit200_response_instance.to_dict()
# create an instance of CancelCredit200Response from a dict
cancel_credit200_response_form_dict = cancel_credit200_response.from_dict(cancel_credit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


