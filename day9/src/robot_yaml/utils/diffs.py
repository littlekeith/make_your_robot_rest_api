#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_similary_keys(expected_key, keys):
    '''
    get similar key
    ratio: returns a float in [0, 1], measuring the "similarity" of the
    sequences.  As a rule of thumb, a ratio value over 0.6 means the
    sequences are close matches.
    You can change compare ratio

    '''
    import difflib
    result = []
    for key in keys:

        _ratio = difflib.SequenceMatcher(None, key, expected_key).ratio()
        if _ratio >= 0.6:
            result.append(key)
    return result or keys
