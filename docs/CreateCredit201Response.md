# CreateCredit201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Please, persist the Bankable Credit ID to get further updates and details about the credit. | [optional] 

## Example

```python
from bankable.models.create_credit201_response import CreateCredit201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredit201Response from a JSON string
create_credit201_response_instance = CreateCredit201Response.from_json(json)
# print the JSON string representation of the object
print CreateCredit201Response.to_json()

# convert the object into a dict
create_credit201_response_dict = create_credit201_response_instance.to_dict()
# create an instance of CreateCredit201Response from a dict
create_credit201_response_form_dict = create_credit201_response.from_dict(create_credit201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


