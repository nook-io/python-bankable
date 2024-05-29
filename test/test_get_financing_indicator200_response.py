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

from bankable.models.get_financing_indicator200_response import GetFinancingIndicator200Response

class TestGetFinancingIndicator200Response(unittest.TestCase):
    """GetFinancingIndicator200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFinancingIndicator200Response:
        """Test GetFinancingIndicator200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFinancingIndicator200Response`
        """
        model = GetFinancingIndicator200Response()
        if include_optional:
            return GetFinancingIndicator200Response(
                eligibility_status = pre-approved,
                financing_indicator = bankable.models.get_financing_indicator_200_response_financing_indicator.getFinancingIndicator_200_response_financing_indicator(
                    amount = 1000, 
                    updated_at = 2021-10-27T00:00:00Z, )
            )
        else:
            return GetFinancingIndicator200Response(
        )
        """

    def testGetFinancingIndicator200Response(self):
        """Test GetFinancingIndicator200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
