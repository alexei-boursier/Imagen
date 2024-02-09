# -*- coding: utf-8 -*-
"""Functions"""
from __future__ import annotations

import ctypes
import os
from typing import TYPE_CHECKING

from .structures import Context

if TYPE_CHECKING:
    from typing import TypeAlias

    Pointer: TypeAlias = ctypes._Pointer  # pylint: disable=protected-access

_os2f: ctypes.CDLL = ctypes.CDLL(os.path.abspath("./lib/OpenSimplex2/OpenSimplex2F.so"))


def shutdown() -> None:
    """
    OS2F OpenSimplex2F_shutdown

    Free up all the LatticePoint stuff allocated in setup_lattice_points()

    Return:
        Nothing
    """
    function: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_shutdown
    function.argtypes = []
    function.restype = None
    return function()


def free(ctx: Pointer[Context]) -> None:
    """
    OS2F OpenSimplex2F_free

    Arguments:
        ctx: OpenSimplex2F_context

    Return:
        Nothing
    """
    function: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_free
    function.argtypes = [ctypes.POINTER(Context)]
    function.restype = None
    return function(ctx)


def open_simplex2f(seed: ctypes.c_int64, ctx: Pointer[Pointer[Context]]) -> None:
    """
    OS2F OpenSimplex2F

    Arguments:
        seed: seed
        ctx: OpenSimplex2F_context

    Return:
        Nothing
    """
    function: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F
    function.argtypes = [ctypes.c_int64, ctypes.POINTER(ctypes.POINTER(Context))]
    function.restype = None
    return function(seed, ctx)


def noise2(
    ctx: Pointer[Context], x: ctypes.c_double, y: ctypes.c_double
) -> ctypes.c_double:
    """
    OS2F OpenSimplex2F_noise2

    2D Simplex noise, standard lattice orientation.

    Arguments:
        ctx: OpenSimplex2F_context
        x: x
        y: y

    Returns:
        A value
    """
    function: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_noise2
    function.argtypes = [
        ctypes.POINTER(Context),
        ctypes.c_double,
        ctypes.c_double,
    ]
    function.restype = ctypes.c_double
    return function(ctx, x, y)


def noise2_xbeforey(ctx: Pointer[Context], x: ctypes.c_double, y: ctypes.c_double) -> ctypes.c_double:
    """
    OS2F OpenSimplex2F_noise2_XBeforeY

    2D Simplex noise, with Y pointing down the main diagonal.
    Might be better for a 2D sandbox style game, where Y is vertical.
    Probably slightly less optimal for heightmaps or continent maps.

    Arguments:
        ctx: OpenSimplex2F_context
        x: x
        y: y

    Returns:
        A value
    """
    function: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_noise2_XBeforeY
    function.argtypes = [
        ctypes.POINTER(Context),
        ctypes.c_double,
        ctypes.c_double,
    ]
    function.restype = ctypes.c_double
    return function(ctx, x, y)
