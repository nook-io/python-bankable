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
from pydantic import BaseModel
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetPriceBreakdown200Response(BaseModel):
    """
    GetPriceBreakdown200Response
    """ # noqa: E501
    debtor_grade: Optional[Any] = Field(default=None, description="The debtor's credit rating obtained from the credit report.")
    currency: Optional[Any] = Field(default=None, description="The currency can be either EUR or GBP depending on the partner configuration.")
    financed_percentage: Optional[Any] = Field(default=None, description="The percentage that Bankable would finance of the invoice face value (usually between 0.85-1, meaning 85-100%).")
    financed_value: Optional[Any] = Field(default=None, description="The value to be financed (the amount is usually 85-100% of the invoice face value).")
    financing_duration: Optional[Any] = Field(default=None, description="The total number of days between the financed and maturity date including both days. The maturity date is one business day after the invoice due date.")
    fees_amount: Optional[Any] = Field(default=None, description="The total amount of estimated fees for financing the invoice.")
    overdue_deposit_days: Optional[Any] = Field(default=None, description="In case there will be an overdue deposit, it will be calculated for the number of overdue days. If the invoice is overdue for more than the overdue deposit days, the full amount of the deposit will be lost.")
    overdue_deposit_percentage: Optional[Any] = Field(default=None, description="The estimated overdue deposit amount divided by the estimated financed value.")
    overdue_deposit_amount: Optional[Any] = Field(default=None, description="The estimated overdue deposit amount is based on the estimated late payment interest for investors and the number of overdue deposit days.")
    overdue_deposit_daily_amount: Optional[Any] = Field(default=None, description="The estimated daily overdue fee would be paid to the investors from the overdue deposit in case the invoice would be overdue.")
    proceeds_amount: Optional[Any] = Field(default=None, description="The estimated proceeds amount would be transferred to the Issuer when the invoice has been financed. The amount is the estimated financed value minus the total estimated fees amount and estimated overdue deposit amount.")
    __properties: ClassVar[List[str]] = ["debtor_grade", "currency", "financed_percentage", "financed_value", "financing_duration", "fees_amount", "overdue_deposit_days", "overdue_deposit_percentage", "overdue_deposit_amount", "overdue_deposit_daily_amount", "proceeds_amount"]

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
        """Create an instance of GetPriceBreakdown200Response from a JSON string"""
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
        # set to None if debtor_grade (nullable) is None
        # and model_fields_set contains the field
        if self.debtor_grade is None and "debtor_grade" in self.model_fields_set:
            _dict['debtor_grade'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetPriceBreakdown200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "debtor_grade": obj.get("debtor_grade"),
            "currency": obj.get("currency"),
            "financed_percentage": obj.get("financed_percentage"),
            "financed_value": obj.get("financed_value"),
            "financing_duration": obj.get("financing_duration"),
            "fees_amount": obj.get("fees_amount"),
            "overdue_deposit_days": obj.get("overdue_deposit_days"),
            "overdue_deposit_percentage": obj.get("overdue_deposit_percentage"),
            "overdue_deposit_amount": obj.get("overdue_deposit_amount"),
            "overdue_deposit_daily_amount": obj.get("overdue_deposit_daily_amount"),
            "proceeds_amount": obj.get("proceeds_amount")
        })
        return _obj


