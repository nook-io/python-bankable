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

class GetClient200Response(BaseModel):
    """
    GetClient200Response
    """ # noqa: E501
    id: Optional[Any] = Field(default=None, description="Credit Client ID provided by Bankable.")
    company_name: Optional[Any] = Field(default=None, description="Full company name.")
    state: Optional[Any] = Field(default=None, description="The onboarding state.")
    product_id: Optional[Any] = Field(default=None, description="Product identifier. The current options are **ETR** and **ETC**.")
    country_code: Optional[Any] = Field(default=None, description="ISO Country code (two letter country code from ISO 3166).")
    registration_number: Optional[Any] = Field(default=None, description="Company registration number.")
    iban: Optional[Any] = Field(default=None, description="Standard International Bank Account Number.")
    bic: Optional[Any] = Field(default=None, description="The Bank Identifier Code or SWIFT Code, made up of 8 or 11 characters.")
    sort_code: Optional[Any] = Field(default=None, description="The 6 digit sort code that identifies the Client bank.")
    account_number: Optional[Any] = Field(default=None, description="Client bank account number.")
    created_at: Optional[Any] = Field(default=None, description="Date at which the client was created.")
    updated_at: Optional[Any] = Field(default=None, description="Date at which the client was last updated.")
    __properties: ClassVar[List[str]] = ["id", "company_name", "state", "product_id", "country_code", "registration_number", "iban", "bic", "sort_code", "account_number", "created_at", "updated_at"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NEW_LEAD', 'LEAD_VERIFIED', 'LEAD_REJECTED', 'CONTRACT_SIGNED', 'COMPANY_CREATED', 'COMPANY_REQUESTED', 'CONTRACT_SENT', 'CONTRACT_GENERATED', 'LEAD_INVALID_SIGNERS'):
            raise ValueError("must be one of enum values ('NEW_LEAD', 'LEAD_VERIFIED', 'LEAD_REJECTED', 'CONTRACT_SIGNED', 'COMPANY_CREATED', 'COMPANY_REQUESTED', 'CONTRACT_SENT', 'CONTRACT_GENERATED', 'LEAD_INVALID_SIGNERS')")
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
        """Create an instance of GetClient200Response from a JSON string"""
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

        # set to None if company_name (nullable) is None
        # and model_fields_set contains the field
        if self.company_name is None and "company_name" in self.model_fields_set:
            _dict['company_name'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if product_id (nullable) is None
        # and model_fields_set contains the field
        if self.product_id is None and "product_id" in self.model_fields_set:
            _dict['product_id'] = None

        # set to None if country_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_code is None and "country_code" in self.model_fields_set:
            _dict['country_code'] = None

        # set to None if registration_number (nullable) is None
        # and model_fields_set contains the field
        if self.registration_number is None and "registration_number" in self.model_fields_set:
            _dict['registration_number'] = None

        # set to None if iban (nullable) is None
        # and model_fields_set contains the field
        if self.iban is None and "iban" in self.model_fields_set:
            _dict['iban'] = None

        # set to None if bic (nullable) is None
        # and model_fields_set contains the field
        if self.bic is None and "bic" in self.model_fields_set:
            _dict['bic'] = None

        # set to None if sort_code (nullable) is None
        # and model_fields_set contains the field
        if self.sort_code is None and "sort_code" in self.model_fields_set:
            _dict['sort_code'] = None

        # set to None if account_number (nullable) is None
        # and model_fields_set contains the field
        if self.account_number is None and "account_number" in self.model_fields_set:
            _dict['account_number'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetClient200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "company_name": obj.get("company_name"),
            "state": obj.get("state"),
            "product_id": obj.get("product_id"),
            "country_code": obj.get("country_code"),
            "registration_number": obj.get("registration_number"),
            "iban": obj.get("iban"),
            "bic": obj.get("bic"),
            "sort_code": obj.get("sort_code"),
            "account_number": obj.get("account_number"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


