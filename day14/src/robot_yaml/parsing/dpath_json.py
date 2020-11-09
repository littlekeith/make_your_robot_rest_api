#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_all_dpaths(dict_obj):
    '''
    get all response dpath
    response = {
        "a": {
            "b":1
        },
        "c":2
    }
    return ["a", "a/b", "c"]
    '''
    import dpath.util

    result = []
    for (path, value) in dpath.util.search(dict_obj, ['**'], yielded=True, separator="/"):
        result.append(path)

    return result


def get_value_by_path(src, path):
    '''
    get all response dpath, response can be list or dict
    response = [
        1,
        2,
        {
            'a': "test"
        }
    ]
    if path = "0", then return 1
    if path = "2/a", then return test
    '''

    import dpath.util
    from robot.api import logger
    from robot_yaml.utils.diffs import get_similary_keys

    # if not isinstance(src, list) or not isinstance(src, dict):
    #     raise Exception(
    #         "get_value_by_path src parameter should be list or dict")
    result = None
    b_found = False

    for (item_path, value) in dpath.util.search(src, path, yielded=True, separator="/"):
        # print(item_path, value)
        b_found = True
        result = value

    if b_found:
        return result

    all_path = get_all_dpaths(src)
    similar_keys = get_similary_keys(path, all_path)
    msg = "Could not find the path: {} in the object: \n{}\nsimilar keys: \n{}".format(
        path, src, similar_keys)
    logger.error(msg)
    raise Exception(msg)

def test_get_value_by_path(src, path):

    import dpath.util

    for (item_path, value) in dpath.util.search(src, path, yielded=True, separator="/"):
        print(item_path, value)


# response = {
#     "id": 732,
#     "date_created": "2020-10-26",
#     "date_modify": "get_current_day()",
#     "weight": -1,
#     "dimensions": {
#         "length": "",
#         "width": "",
#         "height": ""
#     },
#     "attributes": [
#         {
#             "id": 6,
#             "name": "Color",
#             "option": "Black"
#         }
#     ],
#     "_links": {
#         "self": [
#             {
#                 "href": "https://example.com/wp-json/wc/v3/products/22/variations/732"
#             }
#         ],
#         "collection": [
#             {
#                 "href": "https://example.com/wp-json/wc/v3/products/22/variations"
#             }
#         ],
#         "up": [
#             {
#                 "href": "https://example.com/wp-json/wc/v3/products/22"
#             }
#         ]
#     }
# }

# print(test_get_value_by_path(response, "**/name"))
# print(test_get_value_by_path(response, "**/href"))