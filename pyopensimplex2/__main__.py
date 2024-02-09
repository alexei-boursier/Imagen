# -*- coding: utf-8 -*-
"""OS2F Test"""
from __future__ import annotations

import ctypes

from . import OpenSimplex2F, OpenSimplex2F_context, OpenSimplex2F_noise2

SEED: ctypes.c_int64 = ctypes.c_int64(666)

ctx: ctypes._Pointer[OpenSimplex2F_context] = ctypes.pointer(OpenSimplex2F_context())
OpenSimplex2F(SEED, ctypes.pointer(ctx))

result: ctypes.c_double = OpenSimplex2F_noise2(ctx, 10.2, 10.2)
print(result)
