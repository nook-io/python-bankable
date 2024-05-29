# bankable.AuthenticationApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](AuthenticationApi.md#get_token) | **POST** /oauth/token | Get Authentication Token


# **get_token**
> GetToken200Response get_token(client_id, client_secret)

Get Authentication Token

This is the OAuth 2.0 grant that server processes use to access an API. Use this endpoint to directly request an Access Token by using the Client's credentials (a Client ID and a Client Secret).

### Example


```python
import time
import os
import bankable
from bankable.models.get_token200_response import GetToken200Response
from bankable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bnkbl.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bankable.Configuration(
    host = "https://api.bnkbl.io"
)


# Enter a context with an instance of the API client
with bankable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bankable.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 

    try:
        # Get Authentication Token
        api_response = api_instance.get_token(client_id, client_secret)
        print("The response of AuthenticationApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**GetToken200Response**](GetToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

