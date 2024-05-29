# GetPriceBreakdown200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debtor_grade** | **object** | The debtor&#39;s credit rating obtained from the credit report. | [optional] 
**currency** | **object** | The currency can be either EUR or GBP depending on the partner configuration. | [optional] 
**financed_percentage** | **object** | The percentage that Bankable would finance of the invoice face value (usually between 0.85-1, meaning 85-100%). | [optional] 
**financed_value** | **object** | The value to be financed (the amount is usually 85-100% of the invoice face value). | [optional] 
**financing_duration** | **object** | The total number of days between the financed and maturity date including both days. The maturity date is one business day after the invoice due date. | [optional] 
**fees_amount** | **object** | The total amount of estimated fees for financing the invoice. | [optional] 
**overdue_deposit_days** | **object** | In case there will be an overdue deposit, it will be calculated for the number of overdue days. If the invoice is overdue for more than the overdue deposit days, the full amount of the deposit will be lost. | [optional] 
**overdue_deposit_percentage** | **object** | The estimated overdue deposit amount divided by the estimated financed value. | [optional] 
**overdue_deposit_amount** | **object** | The estimated overdue deposit amount is based on the estimated late payment interest for investors and the number of overdue deposit days. | [optional] 
**overdue_deposit_daily_amount** | **object** | The estimated daily overdue fee would be paid to the investors from the overdue deposit in case the invoice would be overdue. | [optional] 
**proceeds_amount** | **object** | The estimated proceeds amount would be transferred to the Issuer when the invoice has been financed. The amount is the estimated financed value minus the total estimated fees amount and estimated overdue deposit amount. | [optional] 

## Example

```python
from bankable.models.get_price_breakdown200_response import GetPriceBreakdown200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPriceBreakdown200Response from a JSON string
get_price_breakdown200_response_instance = GetPriceBreakdown200Response.from_json(json)
# print the JSON string representation of the object
print GetPriceBreakdown200Response.to_json()

# convert the object into a dict
get_price_breakdown200_response_dict = get_price_breakdown200_response_instance.to_dict()
# create an instance of GetPriceBreakdown200Response from a dict
get_price_breakdown200_response_form_dict = get_price_breakdown200_response.from_dict(get_price_breakdown200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


