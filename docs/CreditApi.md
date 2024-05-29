# bankable.CreditApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_credit**](CreditApi.md#cancel_credit) | **POST** /credit/{id}/cancel | Cancel Credit
[**create_credit**](CreditApi.md#create_credit) | **POST** /credit | Submit Credit
[**find_credits**](CreditApi.md#find_credits) | **GET** /credits | List Credits
[**get_credit**](CreditApi.md#get_credit) | **GET** /credit/{id} | Get Credit Details
[**get_credit_price_breakdown**](CreditApi.md#get_credit_price_breakdown) | **GET** /credit/price-breakdown | Get Credit Price Breakdown


# **cancel_credit**
> CancelCredit200Response cancel_credit(id)

Cancel Credit

This endpoint allows cancelling a submitted credit request that Bankable still needs to approve for financing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.cancel_credit200_response import CancelCredit200Response
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
    api_instance = bankable.CreditApi(api_client)
    id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Credit ID provided by Bankable when the Credit was created (see the \"Create Credit\" response).

    try:
        # Cancel Credit
        api_response = api_instance.cancel_credit(id)
        print("The response of CreditApi->cancel_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->cancel_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Credit ID provided by Bankable when the Credit was created (see the \&quot;Create Credit\&quot; response). | 

### Return type

[**CancelCredit200Response**](CancelCredit200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit**
> CreateCredit201Response create_credit(amount, installments, currency, client_id)

Submit Credit

This endpoint allows submitting credit requests for financing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.create_credit201_response import CreateCredit201Response
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
    api_instance = bankable.CreditApi(api_client)
    amount = None # object | The credit amount can only include numbers and dot (.). For example, 100.00.
    installments = None # object | The number of instalments should be a number higher than 0.
    currency = None # object | The currency must be either EUR or GBP.
    client_id = None # object | The unique identifier for the client provided by Bankable.

    try:
        # Submit Credit
        api_response = api_instance.create_credit(amount, installments, currency, client_id)
        print("The response of CreditApi->create_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->create_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | [**object**](object.md)| The credit amount can only include numbers and dot (.). For example, 100.00. | 
 **installments** | [**object**](object.md)| The number of instalments should be a number higher than 0. | 
 **currency** | [**object**](object.md)| The currency must be either EUR or GBP. | 
 **client_id** | [**object**](object.md)| The unique identifier for the client provided by Bankable. | 

### Return type

[**CreateCredit201Response**](CreateCredit201Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_credits**
> FindCredits200Response find_credits(limit=limit, offset=offset, sort_by=sort_by, descending=descending, id=id, number=number, state=state, amount_from=amount_from, amount_to=amount_to, currency=currency, installments=installments, client_id=client_id)

List Credits

This endpoint allows retrieving a paginated list of credits, applying filters and sorting options.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.find_credits200_response import FindCredits200Response
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
    api_instance = bankable.CreditApi(api_client)
    limit = 10 # object | The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. (optional)
    offset = 20 # object | The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. (optional)
    sort_by = created_at # object | Use to determine which value to use to sort the paginated result. The default value is created_at. (optional)
    descending = true # object | Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. (optional)
    id = 'a8168c04-9ee0-4d3a-88b3-2ba644ffce43&id[]=3786dbc1-953e-4c35-9e37-f60e00717d7b' # str | Use to filter the credits list by a collection of credit IDs. You must use this filter by adding multiple times this query parameter with different values. (optional)
    number = 'CL-1&number[]=CL-2' # str | Use to filter the credits list by a collection of credit number. You must use this filter by adding multiple times this query parameter with different values. (optional)
    state = 'APPROVED&state[]=DECLINED' # str | Use to filter the credits list by a collection of credit states. You must use this filter by adding multiple times this query parameter with different values. (optional)
    amount_from = '19195' # str | Use to filter the credits list by amount value above than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. (optional)
    amount_to = '19195' # str | Use to filter the credits list by amount value below than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. (optional)
    currency = 'EUR&currency[]=GBP' # str | Use to filter the credits list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. (optional)
    installments = '6' # str | Use to filter the credits list by the number of instalments given. (optional)
    client_id = '9d4153a3-f708-4e47-967e-bebd619a76a4&client_id[]=db9beb15-ec04-4ff5-9f3f-0f00fd03a9d3' # str | Use to filter the credits list by a collection of client IDs. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. (optional)

    try:
        # List Credits
        api_response = api_instance.find_credits(limit=limit, offset=offset, sort_by=sort_by, descending=descending, id=id, number=number, state=state, amount_from=amount_from, amount_to=amount_to, currency=currency, installments=installments, client_id=client_id)
        print("The response of CreditApi->find_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->find_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. | [optional] 
 **offset** | [**object**](.md)| The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. | [optional] 
 **sort_by** | [**object**](.md)| Use to determine which value to use to sort the paginated result. The default value is created_at. | [optional] 
 **descending** | [**object**](.md)| Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. | [optional] 
 **id** | **str**| Use to filter the credits list by a collection of credit IDs. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **number** | **str**| Use to filter the credits list by a collection of credit number. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **state** | **str**| Use to filter the credits list by a collection of credit states. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **amount_from** | **str**| Use to filter the credits list by amount value above than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. | [optional] 
 **amount_to** | **str**| Use to filter the credits list by amount value below than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. | [optional] 
 **currency** | **str**| Use to filter the credits list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. | [optional] 
 **installments** | **str**| Use to filter the credits list by the number of instalments given. | [optional] 
 **client_id** | **str**| Use to filter the credits list by a collection of client IDs. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. | [optional] 

### Return type

[**FindCredits200Response**](FindCredits200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit**
> GetCredit200Response get_credit(id)

Get Credit Details

This endpoint allows obtaining the current status and details of a credit.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_credit200_response import GetCredit200Response
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
    api_instance = bankable.CreditApi(api_client)
    id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Credit ID provided by Bankable when the credit was created (see the \"Create Credit\" response).

    try:
        # Get Credit Details
        api_response = api_instance.get_credit(id)
        print("The response of CreditApi->get_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->get_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Credit ID provided by Bankable when the credit was created (see the \&quot;Create Credit\&quot; response). | 

### Return type

[**GetCredit200Response**](GetCredit200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_price_breakdown**
> GetCreditPriceBreakdown200Response get_credit_price_breakdown(country, registration_number)

Get Credit Price Breakdown

This endpoint allows obtaining the price breakdown for multiple instalment and credit amount combinations after submitting financial data and before submitting a new credit request.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_credit_price_breakdown200_response import GetCreditPriceBreakdown200Response
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
    api_instance = bankable.CreditApi(api_client)
    country = 'FI' # str | ISO Country Code (two letter country code from ISO 3166).
    registration_number = '09979111' # str | Company registration number.

    try:
        # Get Credit Price Breakdown
        api_response = api_instance.get_credit_price_breakdown(country, registration_number)
        print("The response of CreditApi->get_credit_price_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->get_credit_price_breakdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO Country Code (two letter country code from ISO 3166). | 
 **registration_number** | **str**| Company registration number. | 

### Return type

[**GetCreditPriceBreakdown200Response**](GetCreditPriceBreakdown200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

