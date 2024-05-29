# CreateClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_number** | **object** | Company registration number. | 
**country_code** | **object** | ISO Country Code (two letter country code from ISO 3166). | 
**product** | [**Products**](Products.md) |  | 
**contact** | [**Contact**](Contact.md) |  | 

## Example

```python
from bankable.models.create_client_request import CreateClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientRequest from a JSON string
create_client_request_instance = CreateClientRequest.from_json(json)
# print the JSON string representation of the object
print CreateClientRequest.to_json()

# convert the object into a dict
create_client_request_dict = create_client_request_instance.to_dict()
# create an instance of CreateClientRequest from a dict
create_client_request_form_dict = create_client_request.from_dict(create_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


