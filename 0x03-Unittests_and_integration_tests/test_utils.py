#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Teus Sep 10 21:57:00 2024

@Author: Caleb Kilonzi
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various valid inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that a KeyError is raised for the respective inputs."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> None:
        """Test that get_json returns the expected result."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for memoize method
    """
    def test_memoize(self):
        """
        Test method for memoize
        """
        test_instance = TestClass()

        with patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
