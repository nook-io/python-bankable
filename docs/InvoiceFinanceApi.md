# bankable.InvoiceFinanceApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_invoice**](InvoiceFinanceApi.md#cancel_invoice) | **POST** /invoice/{id}/cancel | Cancel Invoice Finance
[**create_invoice**](InvoiceFinanceApi.md#create_invoice) | **POST** /invoice | Submit Invoice
[**find_invoices**](InvoiceFinanceApi.md#find_invoices) | **GET** /invoices | List Invoices
[**get_invoice**](InvoiceFinanceApi.md#get_invoice) | **GET** /invoice/{id} | Get Invoice Details
[**get_price_breakdown**](InvoiceFinanceApi.md#get_price_breakdown) | **GET** /invoice/price-breakdown | Get Invoice Finance Price Breakdown


# **cancel_invoice**
> CancelInvoice200Response cancel_invoice(id)

Cancel Invoice Finance

This endpoint allows to cancel an invoice's financing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.cancel_invoice200_response import CancelInvoice200Response
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
    api_instance = bankable.InvoiceFinanceApi(api_client)
    id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Invoice ID provided by Bankable when the invoice was created (see the \"Create invoice\" response).

    try:
        # Cancel Invoice Finance
        api_response = api_instance.cancel_invoice(id)
        print("The response of InvoiceFinanceApi->cancel_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceFinanceApi->cancel_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Invoice ID provided by Bankable when the invoice was created (see the \&quot;Create invoice\&quot; response). | 

### Return type

[**CancelInvoice200Response**](CancelInvoice200Response.md)

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

# **create_invoice**
> CreateInvoice201Response create_invoice(amount, issuer_country_code, issuer_registration_number, debtor_country_code, debtor_registration_number, invoice_number, currency, issue_date, due_date, payment_reference, pdf)

Submit Invoice

This endpoint allows submitting invoices for financing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.create_invoice201_response import CreateInvoice201Response
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
    api_instance = bankable.InvoiceFinanceApi(api_client)
    amount = None # object | The invoice amount can only include numbers and dot (.) must be presented in (EUR) or pence (GBP). For example, 100.00 EUR.
    issuer_country_code = None # object | The issuer's two-letter country code in ISO 3166 format.
    issuer_registration_number = None # object | The issuer's Company Registration Number.
    debtor_country_code = None # object | The debtor's two-letter country code in ISO 3166 format.
    debtor_registration_number = None # object | The debtor's Company Registration Number.
    invoice_number = None # object | The invoice number as shown on the invoice.
    currency = None # object | The currency must be either EUR or GBP.
    issue_date = None # object | The issue date should be in format YYYY-MM-DD, for example, 2022-01-01.
    due_date = None # object | The due date should be in format YYYY-MM-DD, for example, 2022-01-01.
    payment_reference = None # object | If there is no separate payment reference number, you can use the invoice number instead.
    pdf = None # object | The invoice PDF file.

    try:
        # Submit Invoice
        api_response = api_instance.create_invoice(amount, issuer_country_code, issuer_registration_number, debtor_country_code, debtor_registration_number, invoice_number, currency, issue_date, due_date, payment_reference, pdf)
        print("The response of InvoiceFinanceApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceFinanceApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | [**object**](object.md)| The invoice amount can only include numbers and dot (.) must be presented in (EUR) or pence (GBP). For example, 100.00 EUR. | 
 **issuer_country_code** | [**object**](object.md)| The issuer&#39;s two-letter country code in ISO 3166 format. | 
 **issuer_registration_number** | [**object**](object.md)| The issuer&#39;s Company Registration Number. | 
 **debtor_country_code** | [**object**](object.md)| The debtor&#39;s two-letter country code in ISO 3166 format. | 
 **debtor_registration_number** | [**object**](object.md)| The debtor&#39;s Company Registration Number. | 
 **invoice_number** | [**object**](object.md)| The invoice number as shown on the invoice. | 
 **currency** | [**object**](object.md)| The currency must be either EUR or GBP. | 
 **issue_date** | [**object**](object.md)| The issue date should be in format YYYY-MM-DD, for example, 2022-01-01. | 
 **due_date** | [**object**](object.md)| The due date should be in format YYYY-MM-DD, for example, 2022-01-01. | 
 **payment_reference** | [**object**](object.md)| If there is no separate payment reference number, you can use the invoice number instead. | 
 **pdf** | [**object**](object.md)| The invoice PDF file. | 

### Return type

[**CreateInvoice201Response**](CreateInvoice201Response.md)

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
**409** | Conflict |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_invoices**
> FindInvoices200Response find_invoices(limit=limit, offset=offset, sort_by=sort_by, descending=descending, invoice_number=invoice_number, invoice_number2=invoice_number2, payment_reference=payment_reference, payment_reference2=payment_reference2, face_value_from=face_value_from, face_value_to=face_value_to, currency=currency, currency2=currency2, issuer_name_like=issuer_name_like, issuer_country=issuer_country, issuer_registration_number=issuer_registration_number, issuer_registration_number2=issuer_registration_number2, debtor_name_like=debtor_name_like, debtor_country=debtor_country, debtor_registration_number=debtor_registration_number, debtor_registration_number2=debtor_registration_number2)

List Invoices

This endpoint allows retrieving a paginated list of invoices, applying filters and sorting options.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.find_invoices200_response import FindInvoices200Response
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
    api_instance = bankable.InvoiceFinanceApi(api_client)
    limit = '10' # str | The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. (optional)
    offset = '20' # str | The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. (optional)
    sort_by = created_at # object | Use to determine which value to use to sort the paginated result. The default value is created_at. (optional)
    descending = 'true' # str | Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. (optional)
    invoice_number = '1038' # str | Use to filter the invoice list by the invoice number given. (optional)
    invoice_number2 = '1038&invoice_number[]=1037' # str | Use to filter the invoice list by a collection of invoice number. You must use this filter by adding multiple times this query parameter with different values. (optional)
    payment_reference = '4599' # str | Use to filter the invoice list by the payment reference given. (optional)
    payment_reference2 = '1038&payment_reference[]=1037' # str | Use to filter the invoice list by a collection of payment references. You must use this filter by adding multiple times this query parameter with different values. (optional)
    face_value_from = '19195' # str | Use to filter the invoice list by face value above than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. (optional)
    face_value_to = '19195' # str | Use to filter the invoice list by face value below than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. (optional)
    currency = 'EUR' # str | Use to filter the invoice list by the currency code given. The format is ISO 4217. (optional)
    currency2 = 'EUR&currency[]=GBP' # str | Use to filter the invoice list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. (optional)
    issuer_name_like = 'House' # str | Use to filter the invoice list by the given issuer name. The like suffix determines that the query we end up doing is a LIKE %VALUE%. (optional)
    issuer_country = 'ES&issuer_country[]=GB' # str | Use to filter the invoice list by a collection of issuer country codes in ISO 3166 format. You must use this filter by adding multiple times this query parameter with different values. (optional)
    issuer_registration_number = '324234' # str | Use to filter the invoice list by the issuer registration number given. (optional)
    issuer_registration_number2 = '33343&issuer_registration_number[]=5554454' # str | Use to filter the invoice list by a collection of issuer registration numbers. You must use this filter by adding multiple times this query parameter with different values. (optional)
    debtor_name_like = 'John Smith' # str | Use to filter the invoice list by the given debtor name. The like suffix determines that the query we end up doing is a LIKE %VALUE%. (optional)
    debtor_country = 'ES&debtor_country[]=GB' # str | Use to filter the invoice list by a collection of debtor countries in ISO 3166 format. You must use this filter by adding multiple times this query parameter with different values. (optional)
    debtor_registration_number = '324234' # str | Use to filter the invoice list by the debtor registration number given. (optional)
    debtor_registration_number2 = '33343&debtor_registration_number[]=5554454' # str | Use to filter the invoice list by a collection of debtor registration numbers. You must use this filter by adding multiple times this query parameter with different values. (optional)

    try:
        # List Invoices
        api_response = api_instance.find_invoices(limit=limit, offset=offset, sort_by=sort_by, descending=descending, invoice_number=invoice_number, invoice_number2=invoice_number2, payment_reference=payment_reference, payment_reference2=payment_reference2, face_value_from=face_value_from, face_value_to=face_value_to, currency=currency, currency2=currency2, issuer_name_like=issuer_name_like, issuer_country=issuer_country, issuer_registration_number=issuer_registration_number, issuer_registration_number2=issuer_registration_number2, debtor_name_like=debtor_name_like, debtor_country=debtor_country, debtor_registration_number=debtor_registration_number, debtor_registration_number2=debtor_registration_number2)
        print("The response of InvoiceFinanceApi->find_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceFinanceApi->find_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| The number of items to obtain per response. The limit/offset schema is used for pagination. The default value is 10. The maximum allowed value is 100. | [optional] 
 **offset** | **str**| The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. | [optional] 
 **sort_by** | [**object**](.md)| Use to determine which value to use to sort the paginated result. The default value is created_at. | [optional] 
 **descending** | **str**| Use to determine the sorting order as either descending or ascending. The default value is false, which corresponds to ascending order. | [optional] 
 **invoice_number** | **str**| Use to filter the invoice list by the invoice number given. | [optional] 
 **invoice_number2** | **str**| Use to filter the invoice list by a collection of invoice number. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **payment_reference** | **str**| Use to filter the invoice list by the payment reference given. | [optional] 
 **payment_reference2** | **str**| Use to filter the invoice list by a collection of payment references. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **face_value_from** | **str**| Use to filter the invoice list by face value above than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. | [optional] 
 **face_value_to** | **str**| Use to filter the invoice list by face value below than the given one. It must be sent as cents. For example, the value 191.95 has to be sent as 19195. | [optional] 
 **currency** | **str**| Use to filter the invoice list by the currency code given. The format is ISO 4217. | [optional] 
 **currency2** | **str**| Use to filter the invoice list by a collection of currencies. You must use this filter by adding multiple times this query parameter with different values. The format is ISO 4217. | [optional] 
 **issuer_name_like** | **str**| Use to filter the invoice list by the given issuer name. The like suffix determines that the query we end up doing is a LIKE %VALUE%. | [optional] 
 **issuer_country** | **str**| Use to filter the invoice list by a collection of issuer country codes in ISO 3166 format. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **issuer_registration_number** | **str**| Use to filter the invoice list by the issuer registration number given. | [optional] 
 **issuer_registration_number2** | **str**| Use to filter the invoice list by a collection of issuer registration numbers. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **debtor_name_like** | **str**| Use to filter the invoice list by the given debtor name. The like suffix determines that the query we end up doing is a LIKE %VALUE%. | [optional] 
 **debtor_country** | **str**| Use to filter the invoice list by a collection of debtor countries in ISO 3166 format. You must use this filter by adding multiple times this query parameter with different values. | [optional] 
 **debtor_registration_number** | **str**| Use to filter the invoice list by the debtor registration number given. | [optional] 
 **debtor_registration_number2** | **str**| Use to filter the invoice list by a collection of debtor registration numbers. You must use this filter by adding multiple times this query parameter with different values. | [optional] 

### Return type

[**FindInvoices200Response**](FindInvoices200Response.md)

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

# **get_invoice**
> GetInvoice200Response get_invoice(id)

Get Invoice Details

This endpoint allows obtaining the current status and details of an invoice.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_invoice200_response import GetInvoice200Response
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
    api_instance = bankable.InvoiceFinanceApi(api_client)
    id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Invoice ID provided by Bankable when the invoice was created (see the \"Create invoice\" response).

    try:
        # Get Invoice Details
        api_response = api_instance.get_invoice(id)
        print("The response of InvoiceFinanceApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceFinanceApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Invoice ID provided by Bankable when the invoice was created (see the \&quot;Create invoice\&quot; response). | 

### Return type

[**GetInvoice200Response**](GetInvoice200Response.md)

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

# **get_price_breakdown**
> GetPriceBreakdown200Response get_price_breakdown(debtor_country_code, debtor_crn, issuer_country_code, issuer_crn, face_value, due_date)

Get Invoice Finance Price Breakdown

This endpoint allows obtaining an estimated price breakdown before financing an invoice.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_price_breakdown200_response import GetPriceBreakdown200Response
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
    api_instance = bankable.InvoiceFinanceApi(api_client)
    debtor_country_code = 'ES' # str | The debtor's two-letter country code in ISO 3166 format.
    debtor_crn = '12345678' # str | The debtor's Company Registration Number.
    issuer_country_code = 'ES' # str | The issuer's two-letter country code in ISO 3166 format.
    issuer_crn = '12345678' # str | The issuer's Company Registration Number.
    face_value = 4712 # object | The invoice face value can only include numbers and dot (.) must be presented in (EUR) or pence (GBP). For example, 100.00 EUR .
    due_date = '2022-10-13' # str | The due date as shown on the potential invoice to be financed. Should be in format YYYY-MM-DD, for example, 2022-01-01.

    try:
        # Get Invoice Finance Price Breakdown
        api_response = api_instance.get_price_breakdown(debtor_country_code, debtor_crn, issuer_country_code, issuer_crn, face_value, due_date)
        print("The response of InvoiceFinanceApi->get_price_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceFinanceApi->get_price_breakdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debtor_country_code** | **str**| The debtor&#39;s two-letter country code in ISO 3166 format. | 
 **debtor_crn** | **str**| The debtor&#39;s Company Registration Number. | 
 **issuer_country_code** | **str**| The issuer&#39;s two-letter country code in ISO 3166 format. | 
 **issuer_crn** | **str**| The issuer&#39;s Company Registration Number. | 
 **face_value** | [**object**](.md)| The invoice face value can only include numbers and dot (.) must be presented in (EUR) or pence (GBP). For example, 100.00 EUR . | 
 **due_date** | **str**| The due date as shown on the potential invoice to be financed. Should be in format YYYY-MM-DD, for example, 2022-01-01. | 

### Return type

[**GetPriceBreakdown200Response**](GetPriceBreakdown200Response.md)

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

