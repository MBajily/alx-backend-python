#!/usr/bin/env python3
"""Unit test file for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Test org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url property"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/test/repos"
            }
            test_class = GithubOrgClient("test")
            self.assertEqual(
                test_class._public_repos_url,
                "https://api.github.com/orgs/test/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test public_repos method"""
        test_payload = [{"name": "test"}]
        mock_get_json.return_value = test_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "test_url"
            test_class = GithubOrgClient("test")
            result = test_class.public_repos()

            self.assertEqual(result, ["test"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: Dict,
            license_key: str,
            expected: bool
            ) -> None:
        """Test has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up class fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mock"""
            mock_response = Mock()
            if url.endswith('/orgs/google'):
                mock_response.json.return_value = cls.org_payload
            elif url.endswith('/orgs/google/repos'):
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class fixtures"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Integration test for public_repos method"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(self.mock_get.call_count, 2)

    def test_public_repos_with_license(self) -> None:
        """Integration test for public_repos method with license"""
        test_class = GithubOrgClient("google")
        self.assertEqual(
            test_class.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
        self.assertEqual(self.mock_get.call_count, 2)


if __name__ == '__main__':
    unittest.main()
