# FindClient200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **object** | The number of items in the response. The limit/offset schema is used for pagination. | [optional] 
**offset** | **object** | The number of items to skip in the response. The limit/offset schema is used for pagination. | [optional] 
**total_items** | **object** | The total number of items available in the dataset, which can be larger than the number of items included in the response. | [optional] 

## Example

```python
from bankable.models.find_client200_response_pagination import FindClient200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of FindClient200ResponsePagination from a JSON string
find_client200_response_pagination_instance = FindClient200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print FindClient200ResponsePagination.to_json()

# convert the object into a dict
find_client200_response_pagination_dict = find_client200_response_pagination_instance.to_dict()
# create an instance of FindClient200ResponsePagination from a dict
find_client200_response_pagination_form_dict = find_client200_response_pagination.from_dict(find_client200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


