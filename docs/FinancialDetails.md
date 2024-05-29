# FinancialDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_month** | **object** | Period month with format YYYY-MM, for example, 2022-12 | 
**revenue** | **object** | Monthly revenue. | 
**costs** | **object** | Monthly costs total. | [optional] 
**gross_profit** | **object** | Monthly gross profit. | 
**expenses** | **object** | Monthly expenses. | 
**ebitda** | **object** | Monthly earnings before interest, tax, depreciation and amortisation. | 
**depreciation** | **object** | Monthly depreciation. | [optional] 
**amortisation** | **object** | Monthly amortisation. | [optional] 
**ebit** | **object** | Monthly earnings before interest and tax. | 
**taxes** | **object** | Monthly taxes. | 
**interests** | **object** | Can be shares or similar. | [optional] 
**profit_loss** | **object** | Monthly profit and loss. | 
**assets** | **object** | Monthly assets. | 
**current_assets** | **object** | Short term assets. | 
**liabilities** | **object** | Liabilities. | 
**current_liabilities** | **object** | Short term liabilities. | 
**shareholder_equity** | **object** | Share holder equity. | [optional] 

## Example

```python
from bankable.models.financial_details import FinancialDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialDetails from a JSON string
financial_details_instance = FinancialDetails.from_json(json)
# print the JSON string representation of the object
print FinancialDetails.to_json()

# convert the object into a dict
financial_details_dict = financial_details_instance.to_dict()
# create an instance of FinancialDetails from a dict
financial_details_form_dict = financial_details.from_dict(financial_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


