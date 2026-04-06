"""
text-expander - Expand abbreviations and contractions

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import TextExpander, expand, process, main

__all__ = ["TextExpander", "expand", "process", "main"]
