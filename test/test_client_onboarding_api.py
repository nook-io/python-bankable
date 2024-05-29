# coding: utf-8

"""
    Credit

    # Introduction Description of Bankable Credit RESTful API. Current limitations: - The Credit service does not support [cross origin headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) for security reasons. It is not possible to use Swagger UI and make API calls directly from the browser. - Modification API requests (`POST`, `DELETE`) require additional security scopes granted under the service agreement. - Consider the Bankable limitations for API calls that depend on the contract agreement.

    The version of the OpenAPI document: b6bf82e
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bankable.api.client_onboarding_api import ClientOnboardingApi


class TestClientOnboardingApi(unittest.TestCase):
    """ClientOnboardingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ClientOnboardingApi()

    def tearDown(self) -> None:
        pass

    def test_create_client(self) -> None:
        """Test case for create_client

        Create Client
        """
        pass

    def test_find_client(self) -> None:
        """Test case for find_client

        List Clients
        """
        pass

    def test_get_client(self) -> None:
        """Test case for get_client

        Get Client Details
        """
        pass

    def test_get_contract_signers(self) -> None:
        """Test case for get_contract_signers

        Get Contract Signers
        """
        pass

    def test_request_contract(self) -> None:
        """Test case for request_contract

        Request Contract
        """
        pass

    def test_submit_bank_data(self) -> None:
        """Test case for submit_bank_data

        Submit Bank Data
        """
        pass

    def test_submit_kyb(self) -> None:
        """Test case for submit_kyb

        Submit KYB Form
        """
        pass

    def test_upload_proof_of_address(self) -> None:
        """Test case for upload_proof_of_address

        Upload Proof of Address
        """
        pass


if __name__ == '__main__':
    unittest.main()
