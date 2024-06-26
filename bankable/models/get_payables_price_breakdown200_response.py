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

class GetPayablesPriceBreakdown200Response(BaseModel):
    """
    GetPayablesPriceBreakdown200Response
    """ # noqa: E501
    financing_amount: Optional[Any] = Field(default=None, description="The total amount that a Client desires to finance.")
    repayment_method: Optional[Any] = Field(default=None, description="Whether a Client has requested weekly or monthly instalments.")
    annual_interest_rate: Optional[Any] = Field(default=None, description="The annual interest rate applied to the outstanding loan principal as a periodic interest rate calculated monthly or weekly based on the selected repayment method.")
    fees_rate: Optional[Any] = Field(default=None, description="The fees percentage that is applied to the total financing amount and charged once as part of the first repayment instalment.")
    total_fees_amount: Optional[Any] = Field(default=None, description="The total fees to be paid in the repayment.")
    instalments: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["financing_amount", "repayment_method", "annual_interest_rate", "fees_rate", "total_fees_amount", "instalments"]

    @field_validator('repayment_method')
    def repayment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('weekly_instalments', 'monthly_instalments'):
            raise ValueError("must be one of enum values ('weekly_instalments', 'monthly_instalments')")
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
        """Create an instance of GetPayablesPriceBreakdown200Response from a JSON string"""
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
        # set to None if financing_amount (nullable) is None
        # and model_fields_set contains the field
        if self.financing_amount is None and "financing_amount" in self.model_fields_set:
            _dict['financing_amount'] = None

        # set to None if repayment_method (nullable) is None
        # and model_fields_set contains the field
        if self.repayment_method is None and "repayment_method" in self.model_fields_set:
            _dict['repayment_method'] = None

        # set to None if annual_interest_rate (nullable) is None
        # and model_fields_set contains the field
        if self.annual_interest_rate is None and "annual_interest_rate" in self.model_fields_set:
            _dict['annual_interest_rate'] = None

        # set to None if fees_rate (nullable) is None
        # and model_fields_set contains the field
        if self.fees_rate is None and "fees_rate" in self.model_fields_set:
            _dict['fees_rate'] = None

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
        """Create an instance of GetPayablesPriceBreakdown200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "financing_amount": obj.get("financing_amount"),
            "repayment_method": obj.get("repayment_method"),
            "annual_interest_rate": obj.get("annual_interest_rate"),
            "fees_rate": obj.get("fees_rate"),
            "total_fees_amount": obj.get("total_fees_amount"),
            "instalments": obj.get("instalments")
        })
        return _obj


