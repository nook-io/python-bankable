# AccountPayable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **object** | Unique identifier for the invoice. | 
**due_date** | **object** | The agreed date of when the company needs to pay the creditor in format YYYY-MM-DD, for example, 2022-01-01. | 
**settled_date** | **object** | The actual date the payment was made in format YYYY-MM-DD, for example, 2022-01-01. | 
**creditor_id** | **object** | Any information that could identify unique creditors per transaction. | 
**face_value** | **object** | The value of the transaction. | 

## Example

```python
from bankable.models.account_payable import AccountPayable

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPayable from a JSON string
account_payable_instance = AccountPayable.from_json(json)
# print the JSON string representation of the object
print AccountPayable.to_json()

# convert the object into a dict
account_payable_dict = account_payable_instance.to_dict()
# create an instance of AccountPayable from a dict
account_payable_form_dict = account_payable.from_dict(account_payable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


