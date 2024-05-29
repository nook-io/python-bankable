# GetCredit200ResponseCredit

Details of the credit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Credit ID provided by Bankable. | [optional] 
**created_at** | **object** | Timestamp of the Credit creation in RFC3339 format. | [optional] 
**updated_at** | **object** | Timestamp of the last update in RFC3339 format. | [optional] 
**number** | **object** | The Credit number provided by Bankable. | [optional] 
**state** | **object** | The current payment status for the credit. | [optional] 
**installments_count** | **object** | Requested number of instalments. | [optional] 
**requested_amount** | **object** | Requested credit amount. | [optional] 
**currency** | **object** | The currency can be either EUR or GBP. | [optional] 
**evaluation_passed** | **object** | Evaluation result is based on the automatic underwriting model and it can be either true or false. | [optional] 
**maximum_limit_exceeded** | **object** | If the requested amount exceeds the maximum limit account, this value will be true, otherwise false. | [optional] 
**isin** | **object** | International Securities Identification Number (ISIN) of the ETC. | [optional] 

## Example

```python
from bankable.models.get_credit200_response_credit import GetCredit200ResponseCredit

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredit200ResponseCredit from a JSON string
get_credit200_response_credit_instance = GetCredit200ResponseCredit.from_json(json)
# print the JSON string representation of the object
print GetCredit200ResponseCredit.to_json()

# convert the object into a dict
get_credit200_response_credit_dict = get_credit200_response_credit_instance.to_dict()
# create an instance of GetCredit200ResponseCredit from a dict
get_credit200_response_credit_form_dict = get_credit200_response_credit.from_dict(get_credit200_response_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


