
from .lib import (
    show,
    setup,
    teardown,
    register_plugins,
    register_host,
)


def is_setup():
    from . import lib
    return lib._has_been_setup


__all__ = [
    "show",
    "setup",
    "teardown",
    "register_plugins",
    "register_host",
]