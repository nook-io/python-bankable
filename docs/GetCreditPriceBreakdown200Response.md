# GetCreditPriceBreakdown200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_ok** | **object** | Whether the credit request has been approved or not. | [optional] 
**expiration_date** | **object** | The date at which the credit offer will expire. After this date, the offer will no longer be valid and the client will need to request pricing for a new credit. | [optional] 
**score** | **object** | Internal credit score (0-100) used to define pricing. Based on the financial data of the client. | [optional] 
**min_annual_percentage_rate** | **object** | The minimum annual percentage rate (APR). Obtainable by requesting any financing option with the maximum amount of instalments offered. | [optional] 
**max_annual_percentage_rate** | **object** | The maximum annual percentage rate (APR). Obtainable by requesting any financing option with the minimum amount of instalments offered. | [optional] 
**matrix** | **object** | Contains information for the different credit amounts and durations. | [optional] 

## Example

```python
from bankable.models.get_credit_price_breakdown200_response import GetCreditPriceBreakdown200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditPriceBreakdown200Response from a JSON string
get_credit_price_breakdown200_response_instance = GetCreditPriceBreakdown200Response.from_json(json)
# print the JSON string representation of the object
print GetCreditPriceBreakdown200Response.to_json()

# convert the object into a dict
get_credit_price_breakdown200_response_dict = get_credit_price_breakdown200_response_instance.to_dict()
# create an instance of GetCreditPriceBreakdown200Response from a dict
get_credit_price_breakdown200_response_form_dict = get_credit_price_breakdown200_response.from_dict(get_credit_price_breakdown200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


