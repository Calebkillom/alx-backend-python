#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Teus Sep 10 22:52:17 2024

@Author: Caleb Kilonzi
"""
import unittest
from unittest.mock import patch, Mock
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
