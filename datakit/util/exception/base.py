#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Datakit Exception
-----------------
Base exception class for the Datakit library, ensuring structured error handling
across all data structures and utilities.

Author: Koushik Dutta | koushikdutta2024@outlook.com
Created: 13-Jan-2025 | Updated: 10-Mar-2025
Version: 1.1 | License: MIT

Usage:
    from exceptions.base_exception import DataKitException

    raise DataKitException("Custom error message")

Requirements:
    Python 3.x

Changelog:
    - 13-Jan-2025: Initial implementation
    - 10-Mar-2025: Improved exception structure
"""


class DataKitException(Exception):
    """Base exception class for the datakit module."""

    def __init__(self, message: str):
        super().__init__(f"[DataKit Error] {message}")
