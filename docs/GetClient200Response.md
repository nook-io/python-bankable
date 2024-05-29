# GetClient200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Credit Client ID provided by Bankable. | [optional] 
**company_name** | **object** | Full company name. | [optional] 
**state** | **object** | The onboarding state. | [optional] 
**product_id** | **object** | Product identifier. The current options are **ETR** and **ETC**. | [optional] 
**country_code** | **object** | ISO Country code (two letter country code from ISO 3166). | [optional] 
**registration_number** | **object** | Company registration number. | [optional] 
**iban** | **object** | Standard International Bank Account Number. | [optional] 
**bic** | **object** | The Bank Identifier Code or SWIFT Code, made up of 8 or 11 characters. | [optional] 
**sort_code** | **object** | The 6 digit sort code that identifies the Client bank. | [optional] 
**account_number** | **object** | Client bank account number. | [optional] 
**created_at** | **object** | Date at which the client was created. | [optional] 
**updated_at** | **object** | Date at which the client was last updated. | [optional] 

## Example

```python
from bankable.models.get_client200_response import GetClient200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClient200Response from a JSON string
get_client200_response_instance = GetClient200Response.from_json(json)
# print the JSON string representation of the object
print GetClient200Response.to_json()

# convert the object into a dict
get_client200_response_dict = get_client200_response_instance.to_dict()
# create an instance of GetClient200Response from a dict
get_client200_response_form_dict = get_client200_response.from_dict(get_client200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


