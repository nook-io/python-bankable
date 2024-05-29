# bankable.ClientFinancialsApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_financing_indicator**](ClientFinancialsApi.md#get_financing_indicator) | **GET** /client/{client_id}/financial-status | Get financing indicator
[**import_financial**](ClientFinancialsApi.md#import_financial) | **POST** /client/{client_id}/financial | Submit Financial Data


# **get_financing_indicator**
> GetFinancingIndicator200Response get_financing_indicator(client_id)

Get financing indicator

Get a Client's eligibility status and financing limit indicator.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_financing_indicator200_response import GetFinancingIndicator200Response
from bankable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bnkbl.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bankable.Configuration(
    host = "https://api.bnkbl.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bankable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bankable.ClientFinancialsApi(api_client)
    client_id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Credit Client ID provided by Bankable. when the client was created (see the \"Create Client\" response).

    try:
        # Get financing indicator
        api_response = api_instance.get_financing_indicator(client_id)
        print("The response of ClientFinancialsApi->get_financing_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientFinancialsApi->get_financing_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)| This is the Credit Client ID provided by Bankable. when the client was created (see the \&quot;Create Client\&quot; response). | 

### Return type

[**GetFinancingIndicator200Response**](GetFinancingIndicator200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**404** | Client not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_financial**
> import_financial(client_id, body=body)

Submit Financial Data

This endpoint allows submitting client's financial information.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bnkbl.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bankable.Configuration(
    host = "https://api.bnkbl.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bankable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bankable.ClientFinancialsApi(api_client)
    client_id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Credit Client ID provided by Bankable. when the client was created (see the \"Create Client\" response).
    body = None # object |  (optional)

    try:
        # Submit Financial Data
        api_instance.import_financial(client_id, body=body)
    except Exception as e:
        print("Exception when calling ClientFinancialsApi->import_financial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)| This is the Credit Client ID provided by Bankable. when the client was created (see the \&quot;Create Client\&quot; response). | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

