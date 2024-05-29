# RequestContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signers** | **object** | List of signing parties. | 

## Example

```python
from bankable.models.request_contract_request import RequestContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestContractRequest from a JSON string
request_contract_request_instance = RequestContractRequest.from_json(json)
# print the JSON string representation of the object
print RequestContractRequest.to_json()

# convert the object into a dict
request_contract_request_dict = request_contract_request_instance.to_dict()
# create an instance of RequestContractRequest from a dict
request_contract_request_form_dict = request_contract_request.from_dict(request_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


