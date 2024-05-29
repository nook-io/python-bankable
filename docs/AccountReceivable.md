# AccountReceivable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **object** | Unique identifier for the invoice. | 
**due_date** | **object** | The agreed date of when the company needs to pay the creditor in format YYYY-MM-DD, for example, 2022-01-01. | 
**settled_date** | **object** | The actual date the payment was made in format YYYY-MM-DD, for example, 2022-01-01. | 
**debtor_id** | **object** | Any information that could identify unique debtors per transaction. | 
**face_value** | **object** | The value of the transaction. | 

## Example

```python
from bankable.models.account_receivable import AccountReceivable

# TODO update the JSON string below
json = "{}"
# create an instance of AccountReceivable from a JSON string
account_receivable_instance = AccountReceivable.from_json(json)
# print the JSON string representation of the object
print AccountReceivable.to_json()

# convert the object into a dict
account_receivable_dict = account_receivable_instance.to_dict()
# create an instance of AccountReceivable from a dict
account_receivable_form_dict = account_receivable.from_dict(account_receivable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


