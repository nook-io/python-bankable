# GetInvoice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **object** | Invoice ID provided by Bankable. | [optional] 
**invoice_number** | **object** | The invoice number as shown on the invoice. | [optional] 
**invoice_reference** | **object** | If there is no separate payment reference number, this will be the invoice number instead. | [optional] 
**payment_status** | **object** | The current payment status for the invoice. If Bankable doesn&#39;t have information about the payment, the &#x60;&#x60;&#x60;payment_status&#x60;&#x60;&#x60; can be empty. | [optional] 
**financing_status** | **object** | The current financing status for the invoice. | [optional] 
**issuer_name** | **object** | The issuer&#39;s company name obtained from public sources. | [optional] 
**issuer_registration_number** | **object** | The issuer&#39;s Company Registration Number. | [optional] 
**issuer_country_code** | **object** | The issuer&#39;s two-letter country code in ISO 3166 format. | [optional] 
**issuer_grade** | **object** | The issuer&#39;s credit rating that was obtained from the credit report at the moment of financing. | [optional] 
**debtor_name** | **object** | The debtor&#39;s company name obtained from public sources. | [optional] 
**debtor_registration_number** | **object** | The debtor&#39;s Company Registration Number. | [optional] 
**debtor_country_code** | **object** | The debtor&#39;s two-letter country code in ISO 3166 format. | [optional] 
**debtor_grade** | **object** | The debtor&#39;s credit rating that was obtained from the credit report at the moment of financing. | [optional] 
**currency** | **object** | The currency can be either EUR or GBP. | [optional] 
**issue_date** | **object** | The invoice issue date in RFC3339 format. | [optional] 
**due_date** | **object** | The invoice due date in RFC3339 format. | [optional] 
**face_value** | **object** | The face value of the invoice. | [optional] 
**settlement_date** | **object** | The invoice settlement date in RFC3339 format. | [optional] 
**rejected_date** | **object** | The invoice rejected date in RFC3339 format. | [optional] 
**rejected_reason** | **object** | The invoice reject reason. | [optional] 
**payment_terms** | **object** | The invoice payment terms. | [optional] 
**financed_percentage** | **object** | The percentage that Bankable financed of the invoice face value (usually between 0.85-1, meaning 85-100%). | [optional] 
**financed_value** | **object** | Financed value (the amount is usually 85-100% of the invoice face value). | [optional] 
**financing_duration** | **object** | The total number of days between the financed and maturity date including both days. | [optional] 
**fees_percentage** | **object** | Total fees amount divided by the financed value. | [optional] 
**fees_amount** | **object** | The total fees for financing the invoice. | [optional] 
**overdue_deposit_days** | **object** | In case there is an overdue deposit, it has been calculated for the number of overdue days. If the invoice is overdue for more than the overdue deposit days, the full amount of the deposit will be lost. | [optional] 
**overdue_deposit_percentage** | **object** | The overdue deposit amount divided by the financed value. | [optional] 
**overdue_deposit_amount** | **object** | The overdue deposit amount is based on the late payment interest for investors and the number of overdue deposit days. | [optional] 
**overdue_deposit_daily_amount** | **object** | The daily overdue fee is paid to the investors from the overdue deposit in case the invoice is overdue. | [optional] 
**proceeds_amount** | **object** | The proceeds amount is transferred to the Issuer when the invoice has been financed. The amount is the financed value less the total fees amount and potential overdue deposit amount. | [optional] 
**financed_date** | **object** | The invoice financed date in ISO-8601 format. | [optional] 

## Example

```python
from bankable.models.get_invoice200_response import GetInvoice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoice200Response from a JSON string
get_invoice200_response_instance = GetInvoice200Response.from_json(json)
# print the JSON string representation of the object
print GetInvoice200Response.to_json()

# convert the object into a dict
get_invoice200_response_dict = get_invoice200_response_instance.to_dict()
# create an instance of GetInvoice200Response from a dict
get_invoice200_response_form_dict = get_invoice200_response.from_dict(get_invoice200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


