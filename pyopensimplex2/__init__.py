# -*- coding: utf-8 -*-
"""Python OpenSimplex2 wrapper"""
from __future__ import annotations

'''
import ctypes
import os.path
from typing import TYPE_CHECKING, TypeAlias

__all__: list[str] = [
    "Grad2",
    "Grad3",
    "Grad4",
    "LatticePoint2D",
    "LatticePoint3D",
    "LatticePoint4D",
    "OpenSimplex2F_context",
    "OpenSimplex2F_shutdown",
    "OpenSimplex2F_free",
    "OpenSimplex2F",
    "OpenSimplex2F_noise2",
    "OpenSimplex2F_noise2_XBeforeY",
    "OpenSimplex2F_noise3_Classic",
    "OpenSimplex2F_noise3_XYBeforeZ",
    "OpenSimplex2F_noise3_XZBeforeY",
    "OpenSimplex2F_noise4_Classic",
    "OpenSimplex2F_noise4_XYBeforeZW",
    "OpenSimplex2F_noise4_XZBeforeYW",
    "OpenSimplex2F_noise4_XYZBeforeW",
]

if TYPE_CHECKING:
    Fields: TypeAlias = list[
        tuple[str, type[ctypes._CData]]  # pylint: disable=protected-access
    ]

_os2f: ctypes.CDLL = ctypes.CDLL(
    os.path.abspath("../lib/OpenSimplex2/OpenSimplex2F.so")
)


class Grad2(ctypes.Structure):
    """OS2F Grad2"""

    _fields_: Fields = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
    ]


class Grad3(ctypes.Structure):
    """OS2F Grad3"""

    _fields_: Fields = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
        ("dz", ctypes.c_double),
    ]


class Grad4(ctypes.Structure):
    """OS2F Grad4"""

    _fields_: Fields = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
        ("dz", ctypes.c_double),
        ("dw", ctypes.c_double),
    ]


class LatticePoint2D(ctypes.Structure):
    """OS2F LatticePoint2D"""

    _fields_: Fields = [
        ("xsv", ctypes.c_int),
        ("ysv", ctypes.c_int),
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
    ]


class LatticePoint3D(ctypes.Structure):
    """OS2F LatticePoint3D"""

    _fields_: Fields


LatticePoint3D._fields_ = [  # pylint: disable=protected-access
    ("dxr", ctypes.c_double),
    ("dyr", ctypes.c_double),
    ("dzr", ctypes.c_double),
    ("xrv", ctypes.c_int),
    ("yrv", ctypes.c_int),
    ("zrv", ctypes.c_int),
    ("nextOnFailure", ctypes.POINTER(LatticePoint3D)),
    ("nextOnSuccess", ctypes.POINTER(LatticePoint3D)),
]


class LatticePoint4D(ctypes.Structure):
    """OS2F LatticePoint4D"""

    _fields_: Fields = [
        ("xsv", ctypes.c_int),
        ("ysv", ctypes.c_int),
        ("zsv", ctypes.c_int),
        ("wsv", ctypes.c_int),
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
        ("dz", ctypes.c_double),
        ("dw", ctypes.c_double),
        ("xsi", ctypes.c_double),
        ("ysi", ctypes.c_double),
        ("zsi", ctypes.c_double),
        ("wsi", ctypes.c_double),
        ("ssiDelta", ctypes.c_double),
    ]


class OpenSimplex2F_context(ctypes.Structure):
    """OS2F OpenSimplex2F_context"""

    _fields_: Fields = [
        ("perm", ctypes.POINTER(ctypes.c_int16)),
        ("permGrad2", ctypes.POINTER(Grad2)),
        ("permGrad3", ctypes.POINTER(Grad3)),
        ("permGrad4", ctypes.POINTER(Grad4)),
    ]


OpenSimplex2F_shutdown: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_shutdown
"""OS2F OpenSimplex2F_shutdown"""
OpenSimplex2F_shutdown.argtypes = []
OpenSimplex2F_shutdown.restype = None

OpenSimplex2F_free: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_free
"""OS2F OpenSimplex2F_free"""
OpenSimplex2F_free.argtypes = [ctypes.POINTER(OpenSimplex2F_context)]
OpenSimplex2F_free.restype = None

OpenSimplex2F: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F
"""OS2F OpenSimplex2F"""
OpenSimplex2F.argtypes = [
    ctypes.c_int64,
    ctypes.POINTER(ctypes.POINTER(OpenSimplex2F_context)),
]
OpenSimplex2F.restype = ctypes.c_int

OpenSimplex2F_noise2: ctypes._NamedFuncPointer = _os2f.OpenSimplex2F_noise2
"""OS2F OpenSimplex2F_noise2"""
OpenSimplex2F_noise2.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise2.restype = ctypes.c_double

OpenSimplex2F_noise2_XBeforeY: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise2_XBeforeY
)
"""OS2F OpenSimplex2F_noise2_XBeforeY"""
OpenSimplex2F_noise2_XBeforeY.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise2_XBeforeY.restype = ctypes.c_double

OpenSimplex2F_noise3_Classic: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise3_Classic
)
"""OS2F OpenSimplex2F_noise3_Classic"""
OpenSimplex2F_noise3_Classic.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise3_Classic.restype = ctypes.c_double

OpenSimplex2F_noise3_XYBeforeZ: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise3_XYBeforeZ
)
"""OS2F OpenSimplex2F_noise3_XYBeforeZ"""
OpenSimplex2F_noise3_XYBeforeZ.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise3_XYBeforeZ.restype = ctypes.c_double

OpenSimplex2F_noise3_XZBeforeY: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise3_XZBeforeY
)
"""OS2F OpenSimplex2F_noise3_XZBeforeY"""
OpenSimplex2F_noise3_XZBeforeY.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise3_XZBeforeY.restype = ctypes.c_double

OpenSimplex2F_noise4_Classic: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise4_Classic
)
"""OS2F OpenSimplex2F_noise4_Classic"""
OpenSimplex2F_noise4_Classic.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise3_Classic.restype = ctypes.c_double

OpenSimplex2F_noise4_XYBeforeZW: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise4_XYBeforeZW
)
"""OS2F OpenSimplex2F_noise4_XYBeforeZW"""
OpenSimplex2F_noise4_XYBeforeZW.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise4_XYBeforeZW.restype = ctypes.c_double

OpenSimplex2F_noise4_XZBeforeYW: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise4_XZBeforeYW
)
"""OS2F OpenSimplex2F_noise4_XZBeforeYW"""
OpenSimplex2F_noise4_XZBeforeYW.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise4_XZBeforeYW.restype = ctypes.c_double

OpenSimplex2F_noise4_XYZBeforeW: ctypes._NamedFuncPointer = (
    _os2f.OpenSimplex2F_noise4_XYZBeforeW
)
"""OS2F OpenSimplex2F_noise4_XYZBeforeW"""
OpenSimplex2F_noise4_XYZBeforeW.argtypes = [
    ctypes.POINTER(OpenSimplex2F_context),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
OpenSimplex2F_noise4_XYZBeforeW.restype = ctypes.c_double
'''
