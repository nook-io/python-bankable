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

from bankable.models.account_payable import AccountPayable

class TestAccountPayable(unittest.TestCase):
    """AccountPayable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountPayable:
        """Test AccountPayable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountPayable`
        """
        model = AccountPayable()
        if include_optional:
            return AccountPayable(
                invoice_id = invoice_90025,
                due_date = 2022-12-01,
                settled_date = 2022-12-01,
                creditor_id = 196af880-ab2b-4418-af40-95bb7ed78977,
                face_value = 900.25
            )
        else:
            return AccountPayable(
                invoice_id = invoice_90025,
                due_date = 2022-12-01,
                settled_date = 2022-12-01,
                creditor_id = 196af880-ab2b-4418-af40-95bb7ed78977,
                face_value = 900.25,
        )
        """

    def testAccountPayable(self):
        """Test AccountPayable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
