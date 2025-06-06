# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.15
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdns_auth_client.api.zonemetadata_api import ZonemetadataApi


class TestZonemetadataApi(unittest.TestCase):
    """ZonemetadataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ZonemetadataApi()

    def tearDown(self) -> None:
        pass

    def test_create_metadata(self) -> None:
        """Test case for create_metadata

        Creates a set of metadata entries
        """
        pass

    def test_delete_metadata(self) -> None:
        """Test case for delete_metadata

        Delete all items of a single kind of domain metadata.
        """
        pass

    def test_get_metadata(self) -> None:
        """Test case for get_metadata

        Get the content of a single kind of domain metadata as a Metadata object.
        """
        pass

    def test_list_metadata(self) -> None:
        """Test case for list_metadata

        Get all the Metadata associated with the zone.
        """
        pass

    def test_modify_metadata(self) -> None:
        """Test case for modify_metadata

        Replace the content of a single kind of domain metadata.
        """
        pass


if __name__ == '__main__':
    unittest.main()
