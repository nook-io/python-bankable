# SubmitKYBRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_revenue** | **object** | Annual revenue of the company | 
**incorporation_date** | **object** | The incorporation date of the company | 
**financial_institution** | **object** | The company is a financial institution. False is obligatory to be able to onboard. We give out an error if true. | 
**income_source** | **object** | Source of income. | 
**trading_name** | **object** | The trading name of the company if different from the legal name. | [optional] 
**industry** | **object** | Standard Industrial Classification code. | [optional] 
**financing_frequency** | **object** | The financing frequency. | 
**financing_needed** | **object** | Amount of financing needed. | [optional] 
**comments** | **object** | Extra comment. | [optional] 
**ultimate_beneficial_owners** | **object** | Array of objects where each object is an owner with at least 25% ownership. 0-4 people. | [optional] 
**directors** | **object** | Array of objects where each object is a director of the company. | 
**corporate_structure** | **object** | Array of objects where each object is a company with at least 25% ownership. Unlimited companies. | [optional] 

## Example

```python
from bankable.models.submit_kyb_request import SubmitKYBRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitKYBRequest from a JSON string
submit_kyb_request_instance = SubmitKYBRequest.from_json(json)
# print the JSON string representation of the object
print SubmitKYBRequest.to_json()

# convert the object into a dict
submit_kyb_request_dict = submit_kyb_request_instance.to_dict()
# create an instance of SubmitKYBRequest from a dict
submit_kyb_request_form_dict = submit_kyb_request.from_dict(submit_kyb_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


