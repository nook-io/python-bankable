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

from bankable.models.get_invoice200_response import GetInvoice200Response

class TestGetInvoice200Response(unittest.TestCase):
    """GetInvoice200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetInvoice200Response:
        """Test GetInvoice200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetInvoice200Response`
        """
        model = GetInvoice200Response()
        if include_optional:
            return GetInvoice200Response(
                invoice_id = cbbd0a65-a149-436a-99bd-06e819a44da9,
                invoice_number = 100,
                invoice_reference = 101,
                payment_status = WRITTEN_OFF,
                financing_status = FINANCED,
                issuer_name = Bankable - Issuer,
                issuer_registration_number = 12345678,
                issuer_country_code = FI,
                issuer_grade = AAA,
                debtor_name = Bankable - Debtor,
                debtor_registration_number = 12345678,
                debtor_country_code = FI,
                debtor_grade = B,
                currency = EUR,
                issue_date = 2021-10-27T00:00:00Z,
                due_date = 2021-11-10T00:00:00Z,
                face_value = 3702.09,
                settlement_date = 2021-10-27T00:00:00Z,
                rejected_date = 2021-10-27T00:00:00Z,
                rejected_reason = INVOICE_B_RATED,
                payment_terms = 30,
                financed_percentage = 1,
                financed_value = 3702.09,
                financing_duration = 14,
                fees_percentage = 0.0106,
                fees_amount = 39.35,
                overdue_deposit_days = 60,
                overdue_deposit_percentage = 0.0201,
                overdue_deposit_amount = 74.4,
                overdue_deposit_daily_amount = 1.24,
                proceeds_amount = 3588.34,
                financed_date = 2021-10-28T00:00:00Z
            )
        else:
            return GetInvoice200Response(
        )
        """

    def testGetInvoice200Response(self):
        """Test GetInvoice200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()