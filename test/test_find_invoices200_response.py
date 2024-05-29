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

from bankable.models.find_invoices200_response import FindInvoices200Response

class TestFindInvoices200Response(unittest.TestCase):
    """FindInvoices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindInvoices200Response:
        """Test FindInvoices200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindInvoices200Response`
        """
        model = FindInvoices200Response()
        if include_optional:
            return FindInvoices200Response(
                results = None,
                pagination = bankable.models.find_invoices_200_response_pagination.findInvoices_200_response_pagination(
                    limit = 20, 
                    offset = 10, 
                    total_items = 2033, )
            )
        else:
            return FindInvoices200Response(
        )
        """

    def testFindInvoices200Response(self):
        """Test FindInvoices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
