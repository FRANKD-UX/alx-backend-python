#!/usr/bin/env python3
"""Unit tests for client module"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns correct value"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property returns correct URL"""
        payload = {"repos_url": "https://api.github.com/orgs/test-org/repos"}
        mock_org.return_value = payload
        
        test_client = GithubOrgClient("test-org")
        result = test_client._public_repos_url
        
        self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method returns correct list of repos"""
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"
        
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = test_payload
        
        test_client = GithubOrgClient("test-org")
        result = test_client.public_repos()
        
        expected_result = ["repo1", "repo2"]
        self.assertEqual(result, expected_result)
        
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method returns correct value"""
        test_client = GithubOrgClient("test-org")
        result = test_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': org_payload,
        'repos_payload': repos_payload,
        'expected_repos': expected_repos,
        'apache2_repos': apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures for the class"""
        # Define URL patterns to mock
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        # Configure the mock to return appropriate fixtures based on URL
        def side_effect(url):
            """Return appropriate response based on the URL"""
            mock_response = Mock()
            
            # Match URL patterns and return appropriate fixtures
            if url.endswith('/orgs/google'):
                mock_response.json.return_value = cls.org_payload
            elif url.endswith('/orgs/google/repos'):
                mock_response.json.return_value = cls.repos_payload
            return mock_response
            
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Clean up test fixtures for the class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method returns expected repos"""
        test_client = GithubOrgClient('google')
        result = test_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filter"""
        test_client = GithubOrgClient('google')
        result = test_client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)
