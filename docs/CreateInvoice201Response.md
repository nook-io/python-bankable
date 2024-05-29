# CreateInvoice201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **object** | Please persist the Bankable invoice ID to get further updates and details about the invoice. | [optional] 

## Example

```python
from bankable.models.create_invoice201_response import CreateInvoice201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoice201Response from a JSON string
create_invoice201_response_instance = CreateInvoice201Response.from_json(json)
# print the JSON string representation of the object
print CreateInvoice201Response.to_json()

# convert the object into a dict
create_invoice201_response_dict = create_invoice201_response_instance.to_dict()
# create an instance of CreateInvoice201Response from a dict
create_invoice201_response_form_dict = create_invoice201_response.from_dict(create_invoice201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


