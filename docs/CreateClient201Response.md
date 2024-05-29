# CreateClient201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID provided by Bankable. | [optional] 

## Example

```python
from bankable.models.create_client201_response import CreateClient201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClient201Response from a JSON string
create_client201_response_instance = CreateClient201Response.from_json(json)
# print the JSON string representation of the object
print CreateClient201Response.to_json()

# convert the object into a dict
create_client201_response_dict = create_client201_response_instance.to_dict()
# create an instance of CreateClient201Response from a dict
create_client201_response_form_dict = create_client201_response.from_dict(create_client201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


