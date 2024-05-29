# coding: utf-8

"""
    Credit

    # Introduction Description of Bankable Credit RESTful API. Current limitations: - The Credit service does not support [cross origin headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) for security reasons. It is not possible to use Swagger UI and make API calls directly from the browser. - Modification API requests (`POST`, `DELETE`) require additional security scopes granted under the service agreement. - Consider the Bankable limitations for API calls that depend on the contract agreement.

    The version of the OpenAPI document: b6bf82e
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bankable.api.invoice_finance_api import InvoiceFinanceApi


class TestInvoiceFinanceApi(unittest.TestCase):
    """InvoiceFinanceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvoiceFinanceApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_invoice(self) -> None:
        """Test case for cancel_invoice

        Cancel Invoice Finance
        """
        pass

    def test_create_invoice(self) -> None:
        """Test case for create_invoice

        Submit Invoice
        """
        pass

    def test_find_invoices(self) -> None:
        """Test case for find_invoices

        List Invoices
        """
        pass

    def test_get_invoice(self) -> None:
        """Test case for get_invoice

        Get Invoice Details
        """
        pass

    def test_get_price_breakdown(self) -> None:
        """Test case for get_price_breakdown

        Get Invoice Finance Price Breakdown
        """
        pass


if __name__ == '__main__':
    unittest.main()