# SCAN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_code** | **object** | The 6 digit sort code that identifies the Client bank. | 
**account_number** | **object** | Client bank account number. | 

## Example

```python
from bankable.models.scan import SCAN

# TODO update the JSON string below
json = "{}"
# create an instance of SCAN from a JSON string
scan_instance = SCAN.from_json(json)
# print the JSON string representation of the object
print SCAN.to_json()

# convert the object into a dict
scan_dict = scan_instance.to_dict()
# create an instance of SCAN from a dict
scan_form_dict = scan.from_dict(scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


