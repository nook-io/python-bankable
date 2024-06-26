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

class SubmitKYBRequest(BaseModel):
    """
    SubmitKYBRequest
    """ # noqa: E501
    annual_revenue: Optional[Any] = Field(description="Annual revenue of the company")
    incorporation_date: Optional[Any] = Field(description="The incorporation date of the company")
    financial_institution: Optional[Any] = Field(description="The company is a financial institution. False is obligatory to be able to onboard. We give out an error if true.")
    income_source: Optional[Any] = Field(description="Source of income.")
    trading_name: Optional[Any] = Field(default=None, description="The trading name of the company if different from the legal name.")
    industry: Optional[Any] = Field(default=None, description="Standard Industrial Classification code.")
    financing_frequency: Optional[Any] = Field(description="The financing frequency.")
    financing_needed: Optional[Any] = Field(default=None, description="Amount of financing needed.")
    comments: Optional[Any] = Field(default=None, description="Extra comment.")
    ultimate_beneficial_owners: Optional[Any] = Field(default=None, description="Array of objects where each object is an owner with at least 25% ownership. 0-4 people.")
    directors: Optional[Any] = Field(description="Array of objects where each object is a director of the company.")
    corporate_structure: Optional[Any] = Field(default=None, description="Array of objects where each object is a company with at least 25% ownership. Unlimited companies.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["annual_revenue", "incorporation_date", "financial_institution", "income_source", "trading_name", "industry", "financing_frequency", "financing_needed", "comments", "ultimate_beneficial_owners", "directors", "corporate_structure"]

    @field_validator('income_source')
    def income_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('business_activities', 'investment_activities', 'royalties'):
            raise ValueError("must be one of enum values ('business_activities', 'investment_activities', 'royalties')")
        return value

    @field_validator('financing_frequency')
    def financing_frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('regular', 'sporadic', 'season'):
            raise ValueError("must be one of enum values ('regular', 'sporadic', 'season')")
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
        """Create an instance of SubmitKYBRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if annual_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.annual_revenue is None and "annual_revenue" in self.model_fields_set:
            _dict['annual_revenue'] = None

        # set to None if incorporation_date (nullable) is None
        # and model_fields_set contains the field
        if self.incorporation_date is None and "incorporation_date" in self.model_fields_set:
            _dict['incorporation_date'] = None

        # set to None if financial_institution (nullable) is None
        # and model_fields_set contains the field
        if self.financial_institution is None and "financial_institution" in self.model_fields_set:
            _dict['financial_institution'] = None

        # set to None if income_source (nullable) is None
        # and model_fields_set contains the field
        if self.income_source is None and "income_source" in self.model_fields_set:
            _dict['income_source'] = None

        # set to None if trading_name (nullable) is None
        # and model_fields_set contains the field
        if self.trading_name is None and "trading_name" in self.model_fields_set:
            _dict['trading_name'] = None

        # set to None if industry (nullable) is None
        # and model_fields_set contains the field
        if self.industry is None and "industry" in self.model_fields_set:
            _dict['industry'] = None

        # set to None if financing_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.financing_frequency is None and "financing_frequency" in self.model_fields_set:
            _dict['financing_frequency'] = None

        # set to None if financing_needed (nullable) is None
        # and model_fields_set contains the field
        if self.financing_needed is None and "financing_needed" in self.model_fields_set:
            _dict['financing_needed'] = None

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['comments'] = None

        # set to None if ultimate_beneficial_owners (nullable) is None
        # and model_fields_set contains the field
        if self.ultimate_beneficial_owners is None and "ultimate_beneficial_owners" in self.model_fields_set:
            _dict['ultimate_beneficial_owners'] = None

        # set to None if directors (nullable) is None
        # and model_fields_set contains the field
        if self.directors is None and "directors" in self.model_fields_set:
            _dict['directors'] = None

        # set to None if corporate_structure (nullable) is None
        # and model_fields_set contains the field
        if self.corporate_structure is None and "corporate_structure" in self.model_fields_set:
            _dict['corporate_structure'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SubmitKYBRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annual_revenue": obj.get("annual_revenue"),
            "incorporation_date": obj.get("incorporation_date"),
            "financial_institution": obj.get("financial_institution"),
            "income_source": obj.get("income_source"),
            "trading_name": obj.get("trading_name"),
            "industry": obj.get("industry"),
            "financing_frequency": obj.get("financing_frequency"),
            "financing_needed": obj.get("financing_needed"),
            "comments": obj.get("comments"),
            "ultimate_beneficial_owners": obj.get("ultimate_beneficial_owners"),
            "directors": obj.get("directors"),
            "corporate_structure": obj.get("corporate_structure")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


