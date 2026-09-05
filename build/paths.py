# -*- coding: utf-8 -*-
"""Where this repository is. Every other script imports REPO from here, so the whole build
runs from wherever the repository has been cloned."""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
REPO = _os.path.dirname(_HERE)
