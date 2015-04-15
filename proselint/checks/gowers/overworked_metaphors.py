# -*- coding: utf-8 -*-
"""MAU103: Overworked metaphors.

---
layout:     post
error_code: MAU103
source:     Sir Ernest Gowers
source_url: http://bit.ly/1CQPH61
title:      overworked metaphors
date:       2014-06-10 12:31:19
categories: writing
---

"""
from tools import memoize, existence_check


@memoize
def check_biggest_bottleneck(text):
    """Use the registered trademark symbol instead of (R)."""
    err = "gowers.mixed_metaphors"
    msg = "Mixed metaphor: bottles with big necks are easy to pass through."
    regex = "biggest bottleneck"

    return existence_check(text, [regex], err, msg, max_errors=1)
