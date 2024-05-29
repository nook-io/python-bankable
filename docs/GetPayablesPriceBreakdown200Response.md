# GetPayablesPriceBreakdown200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financing_amount** | **object** | The total amount that a Client desires to finance. | [optional] 
**repayment_method** | **object** | Whether a Client has requested weekly or monthly instalments. | [optional] 
**annual_interest_rate** | **object** | The annual interest rate applied to the outstanding loan principal as a periodic interest rate calculated monthly or weekly based on the selected repayment method. | [optional] 
**fees_rate** | **object** | The fees percentage that is applied to the total financing amount and charged once as part of the first repayment instalment. | [optional] 
**total_fees_amount** | **object** | The total fees to be paid in the repayment. | [optional] 
**instalments** | **object** |  | [optional] 

## Example

```python
from bankable.models.get_payables_price_breakdown200_response import GetPayablesPriceBreakdown200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayablesPriceBreakdown200Response from a JSON string
get_payables_price_breakdown200_response_instance = GetPayablesPriceBreakdown200Response.from_json(json)
# print the JSON string representation of the object
print GetPayablesPriceBreakdown200Response.to_json()

# convert the object into a dict
get_payables_price_breakdown200_response_dict = get_payables_price_breakdown200_response_instance.to_dict()
# create an instance of GetPayablesPriceBreakdown200Response from a dict
get_payables_price_breakdown200_response_form_dict = get_payables_price_breakdown200_response.from_dict(get_payables_price_breakdown200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


