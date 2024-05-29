# IBAN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **object** | Standard International Bank Account Number. | 
**bic** | **object** | The Bank Identifier Code or SWIFT Code, made up of 8 or 11 characters. | 

## Example

```python
from bankable.models.iban import IBAN

# TODO update the JSON string below
json = "{}"
# create an instance of IBAN from a JSON string
iban_instance = IBAN.from_json(json)
# print the JSON string representation of the object
print IBAN.to_json()

# convert the object into a dict
iban_dict = iban_instance.to_dict()
# create an instance of IBAN from a dict
iban_form_dict = iban.from_dict(iban_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


