# coding: utf-8

"""
    Credit

    # Introduction Description of Bankable Credit RESTful API. Current limitations: - The Credit service does not support [cross origin headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) for security reasons. It is not possible to use Swagger UI and make API calls directly from the browser. - Modification API requests (`POST`, `DELETE`) require additional security scopes granted under the service agreement. - Consider the Bankable limitations for API calls that depend on the contract agreement.

    The version of the OpenAPI document: b6bf82e
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetInvoice200Response(BaseModel):
    """
    GetInvoice200Response
    """ # noqa: E501
    invoice_id: Optional[Any] = Field(default=None, description="Invoice ID provided by Bankable.")
    invoice_number: Optional[Any] = Field(default=None, description="The invoice number as shown on the invoice.")
    invoice_reference: Optional[Any] = Field(default=None, description="If there is no separate payment reference number, this will be the invoice number instead.")
    payment_status: Optional[Any] = Field(default=None, description="The current payment status for the invoice. If Bankable doesn't have information about the payment, the ```payment_status``` can be empty.")
    financing_status: Optional[Any] = Field(default=None, description="The current financing status for the invoice.")
    issuer_name: Optional[Any] = Field(default=None, description="The issuer's company name obtained from public sources.")
    issuer_registration_number: Optional[Any] = Field(default=None, description="The issuer's Company Registration Number.")
    issuer_country_code: Optional[Any] = Field(default=None, description="The issuer's two-letter country code in ISO 3166 format.")
    issuer_grade: Optional[Any] = Field(default=None, description="The issuer's credit rating that was obtained from the credit report at the moment of financing.")
    debtor_name: Optional[Any] = Field(default=None, description="The debtor's company name obtained from public sources.")
    debtor_registration_number: Optional[Any] = Field(default=None, description="The debtor's Company Registration Number.")
    debtor_country_code: Optional[Any] = Field(default=None, description="The debtor's two-letter country code in ISO 3166 format.")
    debtor_grade: Optional[Any] = Field(default=None, description="The debtor's credit rating that was obtained from the credit report at the moment of financing.")
    currency: Optional[Any] = Field(default=None, description="The currency can be either EUR or GBP.")
    issue_date: Optional[Any] = Field(default=None, description="The invoice issue date in RFC3339 format.")
    due_date: Optional[Any] = Field(default=None, description="The invoice due date in RFC3339 format.")
    face_value: Optional[Any] = Field(default=None, description="The face value of the invoice.")
    settlement_date: Optional[Any] = Field(default=None, description="The invoice settlement date in RFC3339 format.")
    rejected_date: Optional[Any] = Field(default=None, description="The invoice rejected date in RFC3339 format.")
    rejected_reason: Optional[Any] = Field(default=None, description="The invoice reject reason.")
    payment_terms: Optional[Any] = Field(default=None, description="The invoice payment terms.")
    financed_percentage: Optional[Any] = Field(default=None, description="The percentage that Bankable financed of the invoice face value (usually between 0.85-1, meaning 85-100%).")
    financed_value: Optional[Any] = Field(default=None, description="Financed value (the amount is usually 85-100% of the invoice face value).")
    financing_duration: Optional[Any] = Field(default=None, description="The total number of days between the financed and maturity date including both days.")
    fees_percentage: Optional[Any] = Field(default=None, description="Total fees amount divided by the financed value.")
    fees_amount: Optional[Any] = Field(default=None, description="The total fees for financing the invoice.")
    overdue_deposit_days: Optional[Any] = Field(default=None, description="In case there is an overdue deposit, it has been calculated for the number of overdue days. If the invoice is overdue for more than the overdue deposit days, the full amount of the deposit will be lost.")
    overdue_deposit_percentage: Optional[Any] = Field(default=None, description="The overdue deposit amount divided by the financed value.")
    overdue_deposit_amount: Optional[Any] = Field(default=None, description="The overdue deposit amount is based on the late payment interest for investors and the number of overdue deposit days.")
    overdue_deposit_daily_amount: Optional[Any] = Field(default=None, description="The daily overdue fee is paid to the investors from the overdue deposit in case the invoice is overdue.")
    proceeds_amount: Optional[Any] = Field(default=None, description="The proceeds amount is transferred to the Issuer when the invoice has been financed. The amount is the financed value less the total fees amount and potential overdue deposit amount.")
    financed_date: Optional[Any] = Field(default=None, description="The invoice financed date in ISO-8601 format.")
    __properties: ClassVar[List[str]] = ["invoice_id", "invoice_number", "invoice_reference", "payment_status", "financing_status", "issuer_name", "issuer_registration_number", "issuer_country_code", "issuer_grade", "debtor_name", "debtor_registration_number", "debtor_country_code", "debtor_grade", "currency", "issue_date", "due_date", "face_value", "settlement_date", "rejected_date", "rejected_reason", "payment_terms", "financed_percentage", "financed_value", "financing_duration", "fees_percentage", "fees_amount", "overdue_deposit_days", "overdue_deposit_percentage", "overdue_deposit_amount", "overdue_deposit_daily_amount", "proceeds_amount", "financed_date"]

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('OUTSTANDING', 'OVERDUE', 'DEFAULTED', 'WRITTEN_OFF', 'SETTLED'):
            raise ValueError("must be one of enum values ('OUTSTANDING', 'OVERDUE', 'DEFAULTED', 'WRITTEN_OFF', 'SETTLED')")
        return value

    @field_validator('financing_status')
    def financing_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ERROR', 'PENDING', 'PRE_APPROVED', 'APPROVED', 'FINANCED', 'REJECTED', 'CANCELLED'):
            raise ValueError("must be one of enum values ('ERROR', 'PENDING', 'PRE_APPROVED', 'APPROVED', 'FINANCED', 'REJECTED', 'CANCELLED')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetInvoice200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if invoice_id (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_id is None and "invoice_id" in self.model_fields_set:
            _dict['invoice_id'] = None

        # set to None if invoice_number (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_number is None and "invoice_number" in self.model_fields_set:
            _dict['invoice_number'] = None

        # set to None if invoice_reference (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_reference is None and "invoice_reference" in self.model_fields_set:
            _dict['invoice_reference'] = None

        # set to None if payment_status (nullable) is None
        # and model_fields_set contains the field
        if self.payment_status is None and "payment_status" in self.model_fields_set:
            _dict['payment_status'] = None

        # set to None if financing_status (nullable) is None
        # and model_fields_set contains the field
        if self.financing_status is None and "financing_status" in self.model_fields_set:
            _dict['financing_status'] = None

        # set to None if issuer_name (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_name is None and "issuer_name" in self.model_fields_set:
            _dict['issuer_name'] = None

        # set to None if issuer_registration_number (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_registration_number is None and "issuer_registration_number" in self.model_fields_set:
            _dict['issuer_registration_number'] = None

        # set to None if issuer_country_code (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_country_code is None and "issuer_country_code" in self.model_fields_set:
            _dict['issuer_country_code'] = None

        # set to None if issuer_grade (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_grade is None and "issuer_grade" in self.model_fields_set:
            _dict['issuer_grade'] = None

        # set to None if debtor_name (nullable) is None
        # and model_fields_set contains the field
        if self.debtor_name is None and "debtor_name" in self.model_fields_set:
            _dict['debtor_name'] = None

        # set to None if debtor_registration_number (nullable) is None
        # and model_fields_set contains the field
        if self.debtor_registration_number is None and "debtor_registration_number" in self.model_fields_set:
            _dict['debtor_registration_number'] = None

        # set to None if debtor_country_code (nullable) is None
        # and model_fields_set contains the field
        if self.debtor_country_code is None and "debtor_country_code" in self.model_fields_set:
            _dict['debtor_country_code'] = None

        # set to None if debtor_grade (nullable) is None
        # and model_fields_set contains the field
        if self.debtor_grade is None and "debtor_grade" in self.model_fields_set:
            _dict['debtor_grade'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if issue_date (nullable) is None
        # and model_fields_set contains the field
        if self.issue_date is None and "issue_date" in self.model_fields_set:
            _dict['issue_date'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        # set to None if face_value (nullable) is None
        # and model_fields_set contains the field
        if self.face_value is None and "face_value" in self.model_fields_set:
            _dict['face_value'] = None

        # set to None if settlement_date (nullable) is None
        # and model_fields_set contains the field
        if self.settlement_date is None and "settlement_date" in self.model_fields_set:
            _dict['settlement_date'] = None

        # set to None if rejected_date (nullable) is None
        # and model_fields_set contains the field
        if self.rejected_date is None and "rejected_date" in self.model_fields_set:
            _dict['rejected_date'] = None

        # set to None if rejected_reason (nullable) is None
        # and model_fields_set contains the field
        if self.rejected_reason is None and "rejected_reason" in self.model_fields_set:
            _dict['rejected_reason'] = None

        # set to None if payment_terms (nullable) is None
        # and model_fields_set contains the field
        if self.payment_terms is None and "payment_terms" in self.model_fields_set:
            _dict['payment_terms'] = None

        # set to None if financed_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.financed_percentage is None and "financed_percentage" in self.model_fields_set:
            _dict['financed_percentage'] = None

        # set to None if financed_value (nullable) is None
        # and model_fields_set contains the field
        if self.financed_value is None and "financed_value" in self.model_fields_set:
            _dict['financed_value'] = None

        # set to None if financing_duration (nullable) is None
        # and model_fields_set contains the field
        if self.financing_duration is None and "financing_duration" in self.model_fields_set:
            _dict['financing_duration'] = None

        # set to None if fees_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.fees_percentage is None and "fees_percentage" in self.model_fields_set:
            _dict['fees_percentage'] = None

        # set to None if fees_amount (nullable) is None
        # and model_fields_set contains the field
        if self.fees_amount is None and "fees_amount" in self.model_fields_set:
            _dict['fees_amount'] = None

        # set to None if overdue_deposit_days (nullable) is None
        # and model_fields_set contains the field
        if self.overdue_deposit_days is None and "overdue_deposit_days" in self.model_fields_set:
            _dict['overdue_deposit_days'] = None

        # set to None if overdue_deposit_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.overdue_deposit_percentage is None and "overdue_deposit_percentage" in self.model_fields_set:
            _dict['overdue_deposit_percentage'] = None

        # set to None if overdue_deposit_amount (nullable) is None
        # and model_fields_set contains the field
        if self.overdue_deposit_amount is None and "overdue_deposit_amount" in self.model_fields_set:
            _dict['overdue_deposit_amount'] = None

        # set to None if overdue_deposit_daily_amount (nullable) is None
        # and model_fields_set contains the field
        if self.overdue_deposit_daily_amount is None and "overdue_deposit_daily_amount" in self.model_fields_set:
            _dict['overdue_deposit_daily_amount'] = None

        # set to None if proceeds_amount (nullable) is None
        # and model_fields_set contains the field
        if self.proceeds_amount is None and "proceeds_amount" in self.model_fields_set:
            _dict['proceeds_amount'] = None

        # set to None if financed_date (nullable) is None
        # and model_fields_set contains the field
        if self.financed_date is None and "financed_date" in self.model_fields_set:
            _dict['financed_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetInvoice200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoice_id": obj.get("invoice_id"),
            "invoice_number": obj.get("invoice_number"),
            "invoice_reference": obj.get("invoice_reference"),
            "payment_status": obj.get("payment_status"),
            "financing_status": obj.get("financing_status"),
            "issuer_name": obj.get("issuer_name"),
            "issuer_registration_number": obj.get("issuer_registration_number"),
            "issuer_country_code": obj.get("issuer_country_code"),
            "issuer_grade": obj.get("issuer_grade"),
            "debtor_name": obj.get("debtor_name"),
            "debtor_registration_number": obj.get("debtor_registration_number"),
            "debtor_country_code": obj.get("debtor_country_code"),
            "debtor_grade": obj.get("debtor_grade"),
            "currency": obj.get("currency"),
            "issue_date": obj.get("issue_date"),
            "due_date": obj.get("due_date"),
            "face_value": obj.get("face_value"),
            "settlement_date": obj.get("settlement_date"),
            "rejected_date": obj.get("rejected_date"),
            "rejected_reason": obj.get("rejected_reason"),
            "payment_terms": obj.get("payment_terms"),
            "financed_percentage": obj.get("financed_percentage"),
            "financed_value": obj.get("financed_value"),
            "financing_duration": obj.get("financing_duration"),
            "fees_percentage": obj.get("fees_percentage"),
            "fees_amount": obj.get("fees_amount"),
            "overdue_deposit_days": obj.get("overdue_deposit_days"),
            "overdue_deposit_percentage": obj.get("overdue_deposit_percentage"),
            "overdue_deposit_amount": obj.get("overdue_deposit_amount"),
            "overdue_deposit_daily_amount": obj.get("overdue_deposit_daily_amount"),
            "proceeds_amount": obj.get("proceeds_amount"),
            "financed_date": obj.get("financed_date")
        })
        return _obj


