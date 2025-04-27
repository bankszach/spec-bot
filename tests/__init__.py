"""Test configuration and shared fixtures."""

import pytest
import warnings

# Silence ripgrep missing warning during tests
warnings.filterwarnings("ignore", message=".*ripgrep.*") 