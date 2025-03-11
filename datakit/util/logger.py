#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Datakit Logger
--------------
Custom logging utility for the Datakit library, providing structured logging
with support for console and file handlers.

Author: Koushik Dutta | koushikdutta2024@outlook.com
Created: 13-Jan-2025 | Updated: 10-Mar-2025
Version: 1.1 | License: MIT

Usage:
    from logger import

Requirements:
    Python 3.x

Changelog:
    - 13-Jan-2025: Initial implementation
    - 10-Mar-2025: Change in exception
"""

import logging
import sys
from typing import Optional

class DataKitLogger:
    """
    Custom logger for Datakit with optional file logging.
    """

    def __init__(self, level=logging.INFO, log_file: Optional[str] = None):
        """
        Initializes the logger.

        :param level: Logging level (default: INFO).
        :param log_file: Optional log file name. If None, only console logging is used.
        """
        self.logger = logging.getLogger("Datakit")
        self.logger.setLevel(level)
        self.logger.propagate = False

        # Log format
        log_format = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
        )

        # Console Handler (Always enabled)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_format)
        self.logger.addHandler(console_handler)

        # Optional File Handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(log_format)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """
        Retrieves the configured logger instance.
        :return: A logger instance configured with console and optional file handlers.
        """
        return self.logger
