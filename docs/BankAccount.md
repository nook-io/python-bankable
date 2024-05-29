# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **object** | Standard International Bank Account Number. | 
**bic** | **object** | The Bank Identifier Code or SWIFT Code, made up of 8 or 11 characters. | 
**sort_code** | **object** | The 6 digit sort code that identifies the Client bank. | 
**account_number** | **object** | Client bank account number. | 

## Example

```python
from bankable.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print BankAccount.to_json()

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_form_dict = bank_account.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


