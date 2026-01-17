"""
pixelcore.exceptions
====================

Canonical exception hierarchy for the pixelcore library.

This module defines all public, stable exceptions that may be raised by
pixelcore. All exceptions raised by pixelcore MUST inherit from
`PixelcoreError`.

Design principles:
- Flat and minimal hierarchy
- Domain-oriented (not implementation-oriented)
- No helpers, no logic, no imports
- Safe to import everywhere (core, ops, io, pipelines)
- Considered part of the public API contract
"""


class PixelcoreError(Exception):
    """
    Base class for all pixelcore errors.

    Users may safely catch this exception to handle any error originating
    from the pixelcore library.
    """

    pass


# ---------------------------------------------------------------------
# Validation / Input Errors
# ---------------------------------------------------------------------


class ValidationError(PixelcoreError):
    """
    Base class for errors caused by invalid or inconsistent user input.

    These errors indicate that an object or argument violates required
    constraints (shape, type, range, compatibility).
    """

    pass


class InvalidImageError(ValidationError):
    """
    Raised when an Image object is invalid, malformed, or incompatible.

    Examples:
    - Invalid shape or dtype
    - Mismatched dimensions
    - Image does not meet required invariants
    """

    pass


class InvalidColorError(ValidationError):
    """
    Raised when a Color object is invalid or incompatible.

    Examples:
    - Wrong number of channels
    - Values outside expected range
    - Color space mismatch
    """

    pass


class InvalidMaskError(ValidationError):
    """
    Raised when a Mask object is invalid or incompatible.

    Examples:
    - Shape mismatch with image
    - Invalid mask type (binary vs weighted)
    - Values outside expected range
    """

    pass


# ---------------------------------------------------------------------
# Capability / Support Errors
# ---------------------------------------------------------------------


class UnsupportedOperationError(PixelcoreError):
    """
    Base class for operations that are valid in theory but not supported
    by the current implementation.
    """

    pass


class UnsupportedColorSpaceError(UnsupportedOperationError):
    """
    Raised when a color space conversion or operation is not supported.
    """

    pass


class UnsupportedInterpolationError(UnsupportedOperationError):
    """
    Raised when an interpolation or resampling method is not supported.
    """

    pass
