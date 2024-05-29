# FindClient200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** | Paginated list of clients. | [optional] 
**pagination** | [**FindClient200ResponsePagination**](FindClient200ResponsePagination.md) |  | [optional] 

## Example

```python
from bankable.models.find_client200_response import FindClient200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindClient200Response from a JSON string
find_client200_response_instance = FindClient200Response.from_json(json)
# print the JSON string representation of the object
print FindClient200Response.to_json()

# convert the object into a dict
find_client200_response_dict = find_client200_response_instance.to_dict()
# create an instance of FindClient200Response from a dict
find_client200_response_form_dict = find_client200_response.from_dict(find_client200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


