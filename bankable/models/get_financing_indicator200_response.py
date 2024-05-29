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
from bankable.models.get_financing_indicator200_response_financing_indicator import GetFinancingIndicator200ResponseFinancingIndicator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetFinancingIndicator200Response(BaseModel):
    """
    GetFinancingIndicator200Response
    """ # noqa: E501
    eligibility_status: Optional[Any] = Field(default=None, description="Eligibilty Status of the payable.")
    financing_indicator: Optional[GetFinancingIndicator200ResponseFinancingIndicator] = None
    __properties: ClassVar[List[str]] = ["eligibility_status", "financing_indicator"]

    @field_validator('eligibility_status')
    def eligibility_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('pre-approved', 'declined'):
            raise ValueError("must be one of enum values ('pre-approved', 'declined')")
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
        """Create an instance of GetFinancingIndicator200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of financing_indicator
        if self.financing_indicator:
            _dict['financing_indicator'] = self.financing_indicator.to_dict()
        # set to None if eligibility_status (nullable) is None
        # and model_fields_set contains the field
        if self.eligibility_status is None and "eligibility_status" in self.model_fields_set:
            _dict['eligibility_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetFinancingIndicator200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eligibility_status": obj.get("eligibility_status"),
            "financing_indicator": GetFinancingIndicator200ResponseFinancingIndicator.from_dict(obj.get("financing_indicator")) if obj.get("financing_indicator") is not None else None
        })
        return _obj

