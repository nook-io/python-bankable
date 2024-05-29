# GetPayableDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Payable request ID provided by Bankable. | [optional] 
**created_at** | **object** | Timestamp of the payable request creation in RFC3339 format. | [optional] 
**updated_at** | **object** | Timestamp of the last update in RFC3339 format. | [optional] 
**state** | **object** | Current status of the payable request. | [optional] 
**reject_reason** | **object** | The rejection reason for the payable request. | [optional] 
**decline_reason** | **object** | The decline reason provided by the client. | [optional] 
**total_requested_amount** | **object** | The total amount of the payable financing request. | [optional] 
**currency** | **object** | The currency can be either EUR or GBP. | [optional] 
**invoice_payable_count** | **object** | The total number of payables part of the financing request. | [optional] 
**instalments_count** | **object** | The total number of instalments that will be required to repay the credit. The maximum values are 51 for weekly and 11 for monthly instalments. | [optional] 
**repayment_method** | **object** | If the repayment plan is in weekly or monthly instalments. | [optional] 
**annual_interest_rate** | **object** | The annual interest rate applied to the outstanding loan principal as a periodic interest rate calculated monthly or weekly based on the selected repayment method. | [optional] 
**fees_rate** | **object** | The fees percentage that is applied to the total financing amount and charged once as part of the first repayment instalment. | [optional] 
**total_repayment_amount** | **object** | The total amount that the client will need to pay back, including total_fees_amount. | [optional] 
**total_interest_amount** | **object** | The total amount of interest that will be charged for the financing. | [optional] 
**total_fees_amount** | **object** | The total amount of fees that will be charged for the financing. | [optional] 
**instalments** | **object** |  | [optional] 

## Example

```python
from bankable.models.get_payable_details200_response import GetPayableDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayableDetails200Response from a JSON string
get_payable_details200_response_instance = GetPayableDetails200Response.from_json(json)
# print the JSON string representation of the object
print GetPayableDetails200Response.to_json()

# convert the object into a dict
get_payable_details200_response_dict = get_payable_details200_response_instance.to_dict()
# create an instance of GetPayableDetails200Response from a dict
get_payable_details200_response_form_dict = get_payable_details200_response.from_dict(get_payable_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


