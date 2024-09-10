#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Teus Sep 10 21:57:00 2024

@Author: Caleb Kilonzi
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_response = {"org": org_name}
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)
        result = client.org

        expected_url = "https://api.github.com/orgs/" + org_name
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_response)

    def test_public_repos_url(self):
        mock_payload = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }

        with patch.object(self.client, 'org', return_value=mock_payload):
            result = self.client._public_repos_url
            expected_url = mock_payload['repos_url']
            self.assertEqual(result, expected_url)
