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

class SubmitPayables200Response(BaseModel):
    """
    SubmitPayables200Response
    """ # noqa: E501
    id: Optional[Any] = Field(default=None, description="Payable financing request ID provided by Bankable.")
    created_at: Optional[Any] = Field(default=None, description="Timestamp of the payables financing request creation in RFC3339 format.")
    state: Optional[Any] = Field(default=None, description="Current state of the payable financing request.")
    total_requested_amount: Optional[Any] = Field(default=None, description="The total amount of the payable financing request.")
    currency: Optional[Any] = Field(default=None, description="The currency can be either EUR or GBP.")
    invoice_payable_count: Optional[Any] = Field(default=None, description="The total number of payables part of the financing request.")
    instalments_count: Optional[Any] = Field(default=None, description="The total number of instalments that will be required to repay the credit.")
    total_repayment_amount: Optional[Any] = Field(default=None, description="The total amount that the client will need to pay back, including total_fees_amount.")
    total_fees_amount: Optional[Any] = Field(default=None, description="The total amount of interest and fees that will be charged for the credit.")
    instalments: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "state", "total_requested_amount", "currency", "invoice_payable_count", "instalments_count", "total_repayment_amount", "total_fees_amount", "instalments"]

    @field_validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EUR', 'GBP'):
            raise ValueError("must be one of enum values ('EUR', 'GBP')")
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
        """Create an instance of SubmitPayables200Response from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if total_requested_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_requested_amount is None and "total_requested_amount" in self.model_fields_set:
            _dict['total_requested_amount'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if invoice_payable_count (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_payable_count is None and "invoice_payable_count" in self.model_fields_set:
            _dict['invoice_payable_count'] = None

        # set to None if instalments_count (nullable) is None
        # and model_fields_set contains the field
        if self.instalments_count is None and "instalments_count" in self.model_fields_set:
            _dict['instalments_count'] = None

        # set to None if total_repayment_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_repayment_amount is None and "total_repayment_amount" in self.model_fields_set:
            _dict['total_repayment_amount'] = None

        # set to None if total_fees_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_fees_amount is None and "total_fees_amount" in self.model_fields_set:
            _dict['total_fees_amount'] = None

        # set to None if instalments (nullable) is None
        # and model_fields_set contains the field
        if self.instalments is None and "instalments" in self.model_fields_set:
            _dict['instalments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SubmitPayables200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "state": obj.get("state"),
            "total_requested_amount": obj.get("total_requested_amount"),
            "currency": obj.get("currency"),
            "invoice_payable_count": obj.get("invoice_payable_count"),
            "instalments_count": obj.get("instalments_count"),
            "total_repayment_amount": obj.get("total_repayment_amount"),
            "total_fees_amount": obj.get("total_fees_amount"),
            "instalments": obj.get("instalments")
        })
        return _obj


