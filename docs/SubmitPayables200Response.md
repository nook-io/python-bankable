# SubmitPayables200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Payable financing request ID provided by Bankable. | [optional] 
**created_at** | **object** | Timestamp of the payables financing request creation in RFC3339 format. | [optional] 
**state** | **object** | Current state of the payable financing request. | [optional] 
**total_requested_amount** | **object** | The total amount of the payable financing request. | [optional] 
**currency** | **object** | The currency can be either EUR or GBP. | [optional] 
**invoice_payable_count** | **object** | The total number of payables part of the financing request. | [optional] 
**instalments_count** | **object** | The total number of instalments that will be required to repay the credit. | [optional] 
**total_repayment_amount** | **object** | The total amount that the client will need to pay back, including total_fees_amount. | [optional] 
**total_fees_amount** | **object** | The total amount of interest and fees that will be charged for the credit. | [optional] 
**instalments** | **object** |  | [optional] 

## Example

```python
from bankable.models.submit_payables200_response import SubmitPayables200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitPayables200Response from a JSON string
submit_payables200_response_instance = SubmitPayables200Response.from_json(json)
# print the JSON string representation of the object
print SubmitPayables200Response.to_json()

# convert the object into a dict
submit_payables200_response_dict = submit_payables200_response_instance.to_dict()
# create an instance of SubmitPayables200Response from a dict
submit_payables200_response_form_dict = submit_payables200_response.from_dict(submit_payables200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


