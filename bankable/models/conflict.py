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

class Conflict(BaseModel):
    """
    Conflict
    """ # noqa: E501
    code: Optional[Any] = Field(default=None, description="The HTTP status code.")
    message: Optional[Any] = Field(default=None, description="A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.")
    details: Optional[Any] = Field(default=None, description="A human-readable explanation specific to this occurrence of the problem.")
    __properties: ClassVar[List[str]] = ["code", "message", "details"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('409'):
            raise ValueError("must be one of enum values ('409')")
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
        """Create an instance of Conflict from a JSON string"""
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
        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Conflict from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "details": obj.get("details")
        })
        return _obj


