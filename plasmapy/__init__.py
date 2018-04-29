"""
PlasmaPy is a community-developed and community-driven open source core
Python package for plasma physics.
"""

# Check that PlasmaPy is being imported from a recent enough version of
# Python so that otherwise an appropriate ImportError with a useful
# error message will be raised.  This check should be done before
# anything else to avoid error messages that obfuscate the source of the
# problem.  This file must be Python 2 compliant enough to avoid raising
# any SyntaxError exceptions, and thus cannot have f-strings.

import sys

if sys.version_info < (3, 6):
    raise ImportError(
        "PlasmaPy requires Python version 3.6 or higher, but is being "
        "called from Python version {}.".format(sys.version.split()[0]))

# Place all imports that require Python 3.6+ **after** the Python
# version check.

# The dunder namespace should be reserved for the special objects that
# are specified in Python documentation (e.g., __name__, __doc__, and
# __version__).  All hidden objects that are specific to PlasmaPy
# should start with a single underscore (e.g., _githash).

__name__ = "plasmapy"

__doc__ = ("A community-developed and community-driven open source "
           "core Python package for plasma physics.")

# The file version.py is created by installing PlasmaPy with setup.py
# using functionality from astropy_helpers.  If this has not been run,
# then set the default values to None.

try:
    from .version import version as __version__
    from .version import githash as _githash
except (ImportError, ModuleNotFoundError):
    __version__ = None
    _githash = None

try:
    from . import atomic
    from . import classes
    from . import constants
    from . import diagnostics
    from . import mathematics
    from . import physics
    from . import utils
except (ImportError, ModuleNotFoundError) as exc:
    raise ImportError("Unable to load PlasmaPy subpackages.") from exc

# Clean up the top-level namespace.

del sys
