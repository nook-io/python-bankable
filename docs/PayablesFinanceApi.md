# bankable.PayablesFinanceApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_repayment_plan**](PayablesFinanceApi.md#approve_repayment_plan) | **PUT** /payables/{id}/approve | Approve Repayment Plan
[**decline_repayment_plan**](PayablesFinanceApi.md#decline_repayment_plan) | **PUT** /payables/{id}/decline | Decline Repayment Plan
[**find_payables**](PayablesFinanceApi.md#find_payables) | **GET** /payables | List Payables
[**get_payable_details**](PayablesFinanceApi.md#get_payable_details) | **GET** /payables/{id} | Get Payable Details
[**get_payables_price_breakdown**](PayablesFinanceApi.md#get_payables_price_breakdown) | **GET** /payables/price-breakdown | Get Payables Finance Price Breakdown
[**submit_payables**](PayablesFinanceApi.md#submit_payables) | **POST** /payables | Submit Payables


# **approve_repayment_plan**
> approve_repayment_plan(id)

Approve Repayment Plan

This endpoint allows the approval of the repayment plan for submitted payables.

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
    api_instance = bankable.PayablesFinanceApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | This is the Payable financing request ID provided by Bankable when the Payables were submitted

    try:
        # Approve Repayment Plan
        api_instance.approve_repayment_plan(id)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->approve_repayment_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| This is the Payable financing request ID provided by Bankable when the Payables were submitted | 

### Return type

void (empty response body)

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
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_repayment_plan**
> decline_repayment_plan(id, decline_reason)

Decline Repayment Plan

This endpoint allows declining the repayment plan for submitted payables.

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
    api_instance = bankable.PayablesFinanceApi(api_client)
    id = 550e8400-e29b-41d4-a716-446655440000 # object | This is the Payable financing request ID provided by Bankable when the Payables were submitted
    decline_reason = 'Free input.' # str | The reason for declining the financing request

    try:
        # Decline Repayment Plan
        api_instance.decline_repayment_plan(id, decline_reason)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->decline_repayment_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Payable financing request ID provided by Bankable when the Payables were submitted | 
 **decline_reason** | **str**| The reason for declining the financing request | 

### Return type

void (empty response body)

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
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_payables**
> FindPayables200Response find_payables(limit=limit, offset=offset, sort_by=sort_by, descending=descending, id=id, state=state, client_id=client_id, total_requested_amount_from=total_requested_amount_from, total_requested_amount_to=total_requested_amount_to, currency=currency)

List Payables

This endpoint allows retrieving a paginated list of payable financing requests, applying filters and sorting options.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.find_payables200_response import FindPayables200Response
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
    api_instance = bankable.PayablesFinanceApi(api_client)
    limit = 10 # object | The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. (optional)
    offset = 20 # object | The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. (optional)
    sort_by = created_at # object | Use to determine which value to use to sort the paginated result. The default value is created_at. (optional)
    descending = true # object | Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. (optional)
    id = 'a8168c04-9ee0-4d3a-88b3-2ba644ffce43&id[]=3786dbc1-953e-4c35-9e37-f60e00717d7b' # str | Use to filter the payable list by a collection of payable financing request IDs. You must use this filter by adding multiple times this query parameter with different values. (optional)
    state = APPROVED&state[]=REJECTED # object | Use to filter the payable request list by a collection of payable financing request states. You must use this filter by adding multiple times this query parameter with different values. (optional)
    client_id = 9d4153a3-f708-4e47-967e-bebd619a76a4&client_id[]=db9beb15-ec04-4ff5-9f3f-0f00fd03a9d3 # object | Use to filter the payable request list by a collection of client IDs. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. (optional)
    total_requested_amount_from = 100.00 # object | Use to filter the payable request list by amount value greater than the given one. The amount can only include numbers and dot (.), and it must be presented in (EUR) or pence (GBP). For example, 100.00. (optional)
    total_requested_amount_to = 200.00 # object | Use to filter the payable request list by amount value less than the given one. The amount can only include numbers and dot (.), and it must be presented in (EUR) or pence (GBP). For example, 200.00. (optional)
    currency = 'EUR&currency[]=GBP' # str | Use to filter the payable request list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. (optional)

    try:
        # List Payables
        api_response = api_instance.find_payables(limit=limit, offset=offset, sort_by=sort_by, descending=descending, id=id, state=state, client_id=client_id, total_requested_amount_from=total_requested_amount_from, total_requested_amount_to=total_requested_amount_to, currency=currency)
        print("The response of PayablesFinanceApi->find_payables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->find_payables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. | [optional] 
 **offset** | [**object**](.md)| The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. | [optional] 
 **sort_by** | [**object**](.md)| Use to determine which value to use to sort the paginated result. The default value is created_at. | [optional] 
 **descending** | [**object**](.md)| Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. | [optional] 
 **id** | **str**| Use to filter the payable list by a collection of payable financing request IDs. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **state** | [**object**](.md)| Use to filter the payable request list by a collection of payable financing request states. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **client_id** | [**object**](.md)| Use to filter the payable request list by a collection of client IDs. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. | [optional] 
 **total_requested_amount_from** | [**object**](.md)| Use to filter the payable request list by amount value greater than the given one. The amount can only include numbers and dot (.), and it must be presented in (EUR) or pence (GBP). For example, 100.00. | [optional] 
 **total_requested_amount_to** | [**object**](.md)| Use to filter the payable request list by amount value less than the given one. The amount can only include numbers and dot (.), and it must be presented in (EUR) or pence (GBP). For example, 200.00. | [optional] 
 **currency** | **str**| Use to filter the payable request list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. | [optional] 

### Return type

[**FindPayables200Response**](FindPayables200Response.md)

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

# **get_payable_details**
> GetPayableDetails200Response get_payable_details(id)

Get Payable Details

Use this endpoint to retrieve the status, details, and repayment plan of a payable financing request.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_payable_details200_response import GetPayableDetails200Response
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
    api_instance = bankable.PayablesFinanceApi(api_client)
    id = 550e8400-e29b-41d4-a716-446655440000 # object | This is the ID provided by Bankable when the payable was created (see the \"Submit Payables\" response).

    try:
        # Get Payable Details
        api_response = api_instance.get_payable_details(id)
        print("The response of PayablesFinanceApi->get_payable_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->get_payable_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the ID provided by Bankable when the payable was created (see the \&quot;Submit Payables\&quot; response). | 

### Return type

[**GetPayableDetails200Response**](GetPayableDetails200Response.md)

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

# **get_payables_price_breakdown**
> GetPayablesPriceBreakdown200Response get_payables_price_breakdown(id, financing_amount, repayment_method)

Get Payables Finance Price Breakdown

This endpoint allows obtaining a price breakdown before financing payables.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_payables_price_breakdown200_response import GetPayablesPriceBreakdown200Response
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
    api_instance = bankable.PayablesFinanceApi(api_client)
    id = 'e4fc84a1-ed7f-48a3-a77c-db323af93c92' # str | The unique identifier for the client provided by Bankable.
    financing_amount = 500 # object | The total amount that a Client desires to finance (1 or more payables).
    repayment_method = weekly_instalments # object | Whether a Client wants to repay the financing in weekly or monthly instalments.

    try:
        # Get Payables Finance Price Breakdown
        api_response = api_instance.get_payables_price_breakdown(id, financing_amount, repayment_method)
        print("The response of PayablesFinanceApi->get_payables_price_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->get_payables_price_breakdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the client provided by Bankable. | 
 **financing_amount** | [**object**](.md)| The total amount that a Client desires to finance (1 or more payables). | 
 **repayment_method** | [**object**](.md)| Whether a Client wants to repay the financing in weekly or monthly instalments. | 

### Return type

[**GetPayablesPriceBreakdown200Response**](GetPayablesPriceBreakdown200Response.md)

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
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_payables**
> SubmitPayables200Response submit_payables(client_id, repayment_method, instalment_count, currency, payment_date=payment_date, payable=payable)

Submit Payables

This endpoint allows submitting one or more payables for financing and receive a payment plan to review.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.submit_payables200_response import SubmitPayables200Response
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
    api_instance = bankable.PayablesFinanceApi(api_client)
    client_id = None # object | The unique identifier for the client provided by Bankable.
    repayment_method = None # object | Whether a Client has chosen to repay the financing in weekly or monthly instalments.
    instalment_count = None # object | The requested number of instalments. The maximum values are 51 for weekly and 11 for monthly instalments.
    currency = None # object | The currency must be either EUR or GBP. All the payables within a request must use the same currency.
    payment_date = None # object | The desired day that the payables should be paid if financed successfully. If not provided, the payables will be paid in the next possible time after financing. The payment date should be in format YYYY-MM-DD, for example, 2024-01-01, and cannot be in the past. (optional)
    payable = None # object |  (optional)

    try:
        # Submit Payables
        api_response = api_instance.submit_payables(client_id, repayment_method, instalment_count, currency, payment_date=payment_date, payable=payable)
        print("The response of PayablesFinanceApi->submit_payables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayablesFinanceApi->submit_payables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](object.md)| The unique identifier for the client provided by Bankable. | 
 **repayment_method** | [**object**](object.md)| Whether a Client has chosen to repay the financing in weekly or monthly instalments. | 
 **instalment_count** | [**object**](object.md)| The requested number of instalments. The maximum values are 51 for weekly and 11 for monthly instalments. | 
 **currency** | [**object**](object.md)| The currency must be either EUR or GBP. All the payables within a request must use the same currency. | 
 **payment_date** | [**object**](object.md)| The desired day that the payables should be paid if financed successfully. If not provided, the payables will be paid in the next possible time after financing. The payment date should be in format YYYY-MM-DD, for example, 2024-01-01, and cannot be in the past. | [optional] 
 **payable** | [**object**](object.md)|  | [optional] 

### Return type

[**SubmitPayables200Response**](SubmitPayables200Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

