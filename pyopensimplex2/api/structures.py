# -*- coding: utf-8 -*-
"""Structures"""
from __future__ import annotations

import ctypes
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    Fields: TypeAlias = list[
        tuple[str, type[ctypes._CData]]  # pylint: disable=protected-access
    ]


class Struct(ctypes.Structure):
    """A C struct"""

    _fields_: Fields
    """Structure fields"""


class Grad2(Struct):
    """
    OS2F Grad2

    Fields:
        dx (ctypes.c_double): dx
        dy (ctypes.c_double): dy
    """

    _fields_ = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
    ]


class Grad3(Struct):
    """
    OS2F Grad3

    Fields:
        dx (ctypes.c_double): dx
        dy (ctypes.c_double): dy
        dz (ctypes.c_double): dz
    """

    _fields_ = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
        ("dz", ctypes.c_double),
    ]


class Grad4(Struct):
    """
    OS2F Grad4

    Fields:
        dx (ctypes.c_double): dx
        dy (ctypes.c_double): dy
        dz (ctypes.c_double): dz
        dw (ctypes.c_double): dw
    """

    _fields_ = [
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
        ("dz", ctypes.c_double),
        ("dw", ctypes.c_double),
    ]


class LatticePoint2D(Struct):
    """
    OS2F LatticePoint2D

    Fields:
        xsv (ctypes.c_int): xsv
        ysv (ctypes.c_int): ysv
        dx (ctypes.c_double): dx
        dy (ctypes.c_double): dy
    """

    _fields_ = [
        ("xsv", ctypes.c_int),
        ("ysv", ctypes.c_int),
        ("dx", ctypes.c_double),
        ("dy", ctypes.c_double),
    ]


class LatticePoint3D(Struct):
    """
    OS2F LatticePoint3D

    Fields:
        dxr (ctypes.c_double): dxr
        dyr (ctypes.c_double): dyr
        dzr (ctypes.c_double): dzr
        xrv (ctypes.c_int): xsv
        yrv (ctypes.c_int): ysv
        zrv (ctypes.c_int): zrv
        nextOnFailure (cpoint._Pointer[LatticePoint3D]]): nextOnFailure
    """


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


class LatticePoint4D(Struct):
    """
    OS2F LatticePoint4D

    Fields:
        xsv (ctypes.c_int): xsv
        ysv (ctypes.c_int): ysv
        zsv (ctypes.c_int): zsv
        wsv (ctypes.c_int): wsv
        dx (ctypes.c_double): dx
        dy (ctypes.c_double): dy
        dz (ctypes.c_double): dz
        dw (ctypes.c_double): dw
        xsi (ctypes.c_double): xsi
        ysi (ctypes.c_double): ysi
        zsi (ctypes.c_double): zsi
        wsi (ctypes.c_double): wsi
        ssiDelta (ctypes.c_double): ssiDelta
    """

    _fields_ = [
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


class Context(Struct):
    """
    OS2F OpenSimplex2F_context

    Fields:
        perm (ctypes._Pointer[ctypes.c_int16]): perm
        permGrad2 (ctypes._Pointer[Grad2]): permGrad2
        permGrad3 (ctypes._Pointer[Grad3]): permGrad3
        permGrad4 (ctypes._Pointer[Grad4]): permGrad4
    """

    _fields_: Fields = [
        ("perm", ctypes.POINTER(ctypes.c_int16)),
        ("permGrad2", ctypes.POINTER(Grad2)),
        ("permGrad3", ctypes.POINTER(Grad3)),
        ("permGrad4", ctypes.POINTER(Grad4)),
    ]
