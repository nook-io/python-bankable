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

class AccountPayable(BaseModel):
    """
    AccountPayable
    """ # noqa: E501
    invoice_id: Optional[Any] = Field(description="Unique identifier for the invoice.")
    due_date: Optional[Any] = Field(description="The agreed date of when the company needs to pay the creditor in format YYYY-MM-DD, for example, 2022-01-01.")
    settled_date: Optional[Any] = Field(description="The actual date the payment was made in format YYYY-MM-DD, for example, 2022-01-01.")
    creditor_id: Optional[Any] = Field(description="Any information that could identify unique creditors per transaction.")
    face_value: Optional[Any] = Field(description="The value of the transaction.")
    __properties: ClassVar[List[str]] = ["invoice_id", "due_date", "settled_date", "creditor_id", "face_value"]

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
        """Create an instance of AccountPayable from a JSON string"""
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

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        # set to None if settled_date (nullable) is None
        # and model_fields_set contains the field
        if self.settled_date is None and "settled_date" in self.model_fields_set:
            _dict['settled_date'] = None

        # set to None if creditor_id (nullable) is None
        # and model_fields_set contains the field
        if self.creditor_id is None and "creditor_id" in self.model_fields_set:
            _dict['creditor_id'] = None

        # set to None if face_value (nullable) is None
        # and model_fields_set contains the field
        if self.face_value is None and "face_value" in self.model_fields_set:
            _dict['face_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountPayable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoice_id": obj.get("invoice_id"),
            "due_date": obj.get("due_date"),
            "settled_date": obj.get("settled_date"),
            "creditor_id": obj.get("creditor_id"),
            "face_value": obj.get("face_value")
        })
        return _obj


