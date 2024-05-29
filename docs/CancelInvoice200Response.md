# CancelInvoice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **object** | The invoice ID provided by Bankable. | [optional] 
**financing_status** | **object** | The current financing status for the invoice. | [optional] 

## Example

```python
from bankable.models.cancel_invoice200_response import CancelInvoice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelInvoice200Response from a JSON string
cancel_invoice200_response_instance = CancelInvoice200Response.from_json(json)
# print the JSON string representation of the object
print CancelInvoice200Response.to_json()

# convert the object into a dict
cancel_invoice200_response_dict = cancel_invoice200_response_instance.to_dict()
# create an instance of CancelInvoice200Response from a dict
cancel_invoice200_response_form_dict = cancel_invoice200_response.from_dict(cancel_invoice200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


