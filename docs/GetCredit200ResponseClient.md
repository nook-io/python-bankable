# GetCredit200ResponseClient

Details of the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The unique identifier for the client provided by Bankable. | [optional] 
**name** | **object** | The client&#39;s company name. | [optional] 
**country** | **object** | The client&#39;s two-letter country code in ISO 3166 format. | [optional] 
**registration_number** | **object** | The client&#39;s Company Registration Number. | [optional] 
**credit_rating** | **object** | The client&#39;s credit rating that was obtained from the credit report at the moment of financing. | [optional] 

## Example

```python
from bankable.models.get_credit200_response_client import GetCredit200ResponseClient

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredit200ResponseClient from a JSON string
get_credit200_response_client_instance = GetCredit200ResponseClient.from_json(json)
# print the JSON string representation of the object
print GetCredit200ResponseClient.to_json()

# convert the object into a dict
get_credit200_response_client_dict = get_credit200_response_client_instance.to_dict()
# create an instance of GetCredit200ResponseClient from a dict
get_credit200_response_client_form_dict = get_credit200_response_client.from_dict(get_credit200_response_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


