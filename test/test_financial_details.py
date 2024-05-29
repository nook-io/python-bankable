# coding: utf-8

"""
    Credit

    # Introduction Description of Bankable Credit RESTful API. Current limitations: - The Credit service does not support [cross origin headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) for security reasons. It is not possible to use Swagger UI and make API calls directly from the browser. - Modification API requests (`POST`, `DELETE`) require additional security scopes granted under the service agreement. - Consider the Bankable limitations for API calls that depend on the contract agreement.

    The version of the OpenAPI document: b6bf82e
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bankable.models.financial_details import FinancialDetails

class TestFinancialDetails(unittest.TestCase):
    """FinancialDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialDetails:
        """Test FinancialDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinancialDetails`
        """
        model = FinancialDetails()
        if include_optional:
            return FinancialDetails(
                period_month = 2022-01,
                revenue = 100.25,
                costs = 100.25,
                gross_profit = 100.25,
                expenses = 100.25,
                ebitda = 100.25,
                depreciation = 100.25,
                amortisation = 100.25,
                ebit = 100.25,
                taxes = 100.25,
                interests = 100.25,
                profit_loss = 100.25,
                assets = 100.25,
                current_assets = 100.25,
                liabilities = 100.25,
                current_liabilities = 100.25,
                shareholder_equity = 100.25
            )
        else:
            return FinancialDetails(
                period_month = 2022-01,
                revenue = 100.25,
                gross_profit = 100.25,
                expenses = 100.25,
                ebitda = 100.25,
                ebit = 100.25,
                taxes = 100.25,
                profit_loss = 100.25,
                assets = 100.25,
                current_assets = 100.25,
                liabilities = 100.25,
                current_liabilities = 100.25,
        )
        """

    def testFinancialDetails(self):
        """Test FinancialDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
