"""
pixelcore.core.enums
====================

Canonical enumerations used across pixelcore.

This module defines all zero-ambiguity constants that are part of the
pixelcore public API. Enums defined here are used to enforce explicit,
type-safe semantics and prevent silent behavior changes.

Design rules:
- Enums only (no constants, no helpers)
- No aliases
- No implicit conversions
- Safe to import from anywhere
- Changes are deliberate and breaking
"""

from enum import Enum


class ColorSpace(Enum):
    """
    Supported color spaces.

    Color space must always be explicit. Silent or implicit color space
    assumptions are forbidden throughout the library.
    """

    RGB = "RGB"
    LAB = "LAB"
    HSV = "HSV"
    GRAY = "GRAY"


class MaskType(Enum):
    """
    Supported mask types.

    BINARY:
        Mask values are strictly 0 or 1.

    WEIGHTED:
        Mask values are continuous (typically in range [0, 1]).
    """

    BINARY = "BINARY"
    WEIGHTED = "WEIGHTED"
