# bankable.ClientOnboardingApi

All URIs are relative to *https://api.bnkbl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientOnboardingApi.md#create_client) | **POST** /client | Create Client
[**find_client**](ClientOnboardingApi.md#find_client) | **GET** /clients | List Clients
[**get_client**](ClientOnboardingApi.md#get_client) | **GET** /client/{id} | Get Client Details
[**get_contract_signers**](ClientOnboardingApi.md#get_contract_signers) | **GET** /client/{client_id}/product/{product}/contract/signers | Get Contract Signers
[**request_contract**](ClientOnboardingApi.md#request_contract) | **POST** /client/{client_id}/product/{product}/contract/request | Request Contract
[**submit_bank_data**](ClientOnboardingApi.md#submit_bank_data) | **POST** /client/{id}/bankdata | Submit Bank Data
[**submit_kyb**](ClientOnboardingApi.md#submit_kyb) | **POST** /client/{client_id}/product/{product}/kyb | Submit KYB Form
[**upload_proof_of_address**](ClientOnboardingApi.md#upload_proof_of_address) | **POST** /client/{client_id}/product/{product}/contract/signers/proof-of-address | Upload Proof of Address


# **create_client**
> CreateClient201Response create_client(create_client_request=create_client_request)

Create Client

Use this operation to create a client.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.create_client201_response import CreateClient201Response
from bankable.models.create_client_request import CreateClientRequest
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    create_client_request = bankable.CreateClientRequest() # CreateClientRequest |  (optional)

    try:
        # Create Client
        api_response = api_instance.create_client(create_client_request=create_client_request)
        print("The response of ClientOnboardingApi->create_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->create_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_request** | [**CreateClientRequest**](CreateClientRequest.md)|  | [optional] 

### Return type

[**CreateClient201Response**](CreateClient201Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**404** | Company not found. |  -  |
**409** | Already created client for product. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_client**
> FindClient200Response find_client(limit, offset, id=id, state=state, missing_bank_details=missing_bank_details, crn=crn, product_id=product_id)

List Clients

Use this operation to obtain a list of clients.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.find_client200_response import FindClient200Response
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    limit = 10 # object | The number of items to obtain per response. The limit/offset schema is used for pagination. The maximum allowed value is 100.
    offset = 10 # object | The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0.
    id = '665eac4d-e843-4dfa-a984-114670a39aff' # str | Use to filter the result using a client ID. Multiple IDs in the query are supported using `key=value` pairs. (optional)
    state = NEW_LEAD # object | Use to filter the result using client state. Multiple states in the query are supported using `key=value` pairs. (optional)
    missing_bank_details = true # object | Use to filter the results to show companies that are missing only the bank details to complete the onboarding. (optional)
    crn = 'GB11822335' # str | Use to filter the result using CRN (country code + registration number). Multiple CRNs in the query are supported using `key=value` pairs. (optional)
    product_id = ETC # object | Use to filter the result using a product ID. Multiple product IDs in the query are supported using `key=value` pairs. (optional)

    try:
        # List Clients
        api_response = api_instance.find_client(limit, offset, id=id, state=state, missing_bank_details=missing_bank_details, crn=crn, product_id=product_id)
        print("The response of ClientOnboardingApi->find_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->find_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| The number of items to obtain per response. The limit/offset schema is used for pagination. The maximum allowed value is 100. | 
 **offset** | [**object**](.md)| The number of items to skip in the response. The limit/offset schema is used for pagination. The default value is 0. | 
 **id** | **str**| Use to filter the result using a client ID. Multiple IDs in the query are supported using &#x60;key&#x3D;value&#x60; pairs. | [optional] 
 **state** | [**object**](.md)| Use to filter the result using client state. Multiple states in the query are supported using &#x60;key&#x3D;value&#x60; pairs. | [optional] 
 **missing_bank_details** | [**object**](.md)| Use to filter the results to show companies that are missing only the bank details to complete the onboarding. | [optional] 
 **crn** | **str**| Use to filter the result using CRN (country code + registration number). Multiple CRNs in the query are supported using &#x60;key&#x3D;value&#x60; pairs. | [optional] 
 **product_id** | [**object**](.md)| Use to filter the result using a product ID. Multiple product IDs in the query are supported using &#x60;key&#x3D;value&#x60; pairs. | [optional] 

### Return type

[**FindClient200Response**](FindClient200Response.md)

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

# **get_client**
> GetClient200Response get_client(id, product_id)

Get Client Details

Use this operation to obtain the current status and details of a client.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.get_client200_response import GetClient200Response
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    id = cbbd0a65-a149-436a-99bd-06e819a44da9 # object | This is the Credit Client ID provided by Bankable. when the client was created (see the \"Create Client\" response).
    product_id = 'ETC' # str | Product identifier. The current options are **ETR** and **ETC**.

    try:
        # Get Client Details
        api_response = api_instance.get_client(id, product_id)
        print("The response of ClientOnboardingApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->get_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| This is the Credit Client ID provided by Bankable. when the client was created (see the \&quot;Create Client\&quot; response). | 
 **product_id** | **str**| Product identifier. The current options are **ETR** and **ETC**. | 

### Return type

[**GetClient200Response**](GetClient200Response.md)

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
**404** | Resource not found |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_signers**
> object get_contract_signers(client_id, product)

Get Contract Signers

List contract signers and their status.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.products import Products
from bankable.models.object import object
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    client_id = eed517c8-fce6-425e-96a1-105fc15ad09d # object | 
    product = bankable.Products() # Products | 

    try:
        # Get Contract Signers
        api_response = api_instance.get_contract_signers(client_id, product)
        print("The response of ClientOnboardingApi->get_contract_signers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->get_contract_signers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 
 **product** | [**Products**](.md)|  | 

### Return type

**object**

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | invalid values |  -  |
**404** | client not found |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_contract**
> object request_contract(client_id, product, request_contract_request=request_contract_request)

Request Contract

Use this operation to obtain URLs for contract signing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.products import Products
from bankable.models.request_contract_request import RequestContractRequest
from bankable.models.object import object
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    client_id = eed517c8-fce6-425e-96a1-105fc15ad09d # object | 
    product = bankable.Products() # Products | 
    request_contract_request = bankable.RequestContractRequest() # RequestContractRequest |  (optional)

    try:
        # Request Contract
        api_response = api_instance.request_contract(client_id, product, request_contract_request=request_contract_request)
        print("The response of ClientOnboardingApi->request_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->request_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 
 **product** | [**Products**](.md)|  | 
 **request_contract_request** | [**RequestContractRequest**](RequestContractRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract requested |  -  |
**400** | invalid form values |  -  |
**404** | client not found |  -  |
**409** | Contract already requested |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_bank_data**
> submit_bank_data(id, bank_account=bank_account)

Submit Bank Data

Use this operation to submit Bank Data for the client onboarding process.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.bank_account import BankAccount
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    id = eed517c8-fce6-425e-96a1-105fc15ad09d # object | 
    bank_account = bankable.BankAccount() # BankAccount |  (optional)

    try:
        # Submit Bank Data
        api_instance.submit_bank_data(id, bank_account=bank_account)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->submit_bank_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **bank_account** | [**BankAccount**](BankAccount.md)|  | [optional] 

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
**201** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_kyb**
> submit_kyb(client_id, product, submit_kyb_request=submit_kyb_request)

Submit KYB Form

Use this operation to submit a KYB form for the client onboarding process.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.products import Products
from bankable.models.submit_kyb_request import SubmitKYBRequest
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    client_id = eed517c8-fce6-425e-96a1-105fc15ad09d # object | 
    product = bankable.Products() # Products | 
    submit_kyb_request = bankable.SubmitKYBRequest() # SubmitKYBRequest |  (optional)

    try:
        # Submit KYB Form
        api_instance.submit_kyb(client_id, product, submit_kyb_request=submit_kyb_request)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->submit_kyb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 
 **product** | [**Products**](.md)|  | 
 **submit_kyb_request** | [**SubmitKYBRequest**](SubmitKYBRequest.md)|  | [optional] 

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
**400** | invalid form values |  -  |
**404** | client not found |  -  |
**409** | Data already submitted. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_proof_of_address**
> UploadProofOfAddress201Response upload_proof_of_address(client_id, product, file)

Upload Proof of Address

Use this operation to upload a proof of address file, a requirement for UK company contract signing.

### Example

* OAuth Authentication (ClientCredentials):

```python
import time
import os
import bankable
from bankable.models.products import Products
from bankable.models.upload_proof_of_address201_response import UploadProofOfAddress201Response
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
    api_instance = bankable.ClientOnboardingApi(api_client)
    client_id = eed517c8-fce6-425e-96a1-105fc15ad09d # object | 
    product = bankable.Products() # Products | 
    file = None # object | The file to use to proving address.

    try:
        # Upload Proof of Address
        api_response = api_instance.upload_proof_of_address(client_id, product, file)
        print("The response of ClientOnboardingApi->upload_proof_of_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOnboardingApi->upload_proof_of_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 
 **product** | [**Products**](.md)|  | 
 **file** | [**object**](object.md)| The file to use to proving address. | 

### Return type

[**UploadProofOfAddress201Response**](UploadProofOfAddress201Response.md)

### Authorization

[ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attachment created |  -  |
**400** |  |  -  |
**404** | client not found |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

