# CompanyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **object** | Full company name. | 
**registration_number** | **object** | Company registration number. | 
**country_code** | **object** | ISO Country code (two letter country code from ISO 3166). | 
**currency** | **object** | Currency which the company operates. | 
**industry** | **object** | Industry SIC code. | [optional] 
**company_type** | **object** | Company type LTD: Limited Company. UNLTD: Unlimited Company. LLP: Limited Liability Partnership. SOLE: Sole Trader.  | [optional] 

## Example

```python
from bankable.models.company_details import CompanyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetails from a JSON string
company_details_instance = CompanyDetails.from_json(json)
# print the JSON string representation of the object
print CompanyDetails.to_json()

# convert the object into a dict
company_details_dict = company_details_instance.to_dict()
# create an instance of CompanyDetails from a dict
company_details_form_dict = company_details.from_dict(company_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


