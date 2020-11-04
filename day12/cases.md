上篇, 我们介绍了使用RequestsLibrary库进行接口测试时断言的简单使用

本文将带你了解dpath库的强大之处:

- 如何断言可变内容, 如响应中的日期时间, 随机数等
- 如何断言内嵌对象的内容
- 如何断言对象

**注：** 本文中从reponse获取key的value都是通过[dpath](https://pypi.org/project/dpath/) 库解决

# 先看看最终的reponse
```python
response = {
    "id": 732,
    "date_created": "2020-10-26",
    "date_modify": get_current_day(),
    "weight": -1,
    "dimensions": {
        "length": "",
        "width": "",
        "height": ""
    },
    "attributes": [
        {
            "id": 6,
            "name": "Color",
            "option": "Black"
        }
    ],
    "_links": {
        "self": [
            {
                "href": "https://example.com/wp-json/wc/v3/products/22/variations/732"
            }
        ],
        "collection": [
            {
                "href": "https://example.com/wp-json/wc/v3/products/22/variations"
            }
        ],
        "up": [
            {
                "href": "https://example.com/wp-json/wc/v3/products/22"
            }
        ]
    }
}
```

## 断言1: 断言固定日期
- Mission: 判断response中的date_created是否等于2020 - 10 - 26

yaml用例如下, 注意日期一定要用**双引号**(大家可以试下不使用双引号)
```yaml
-
  keyword: assert_equal_by_dpath
  name: assert time by given constant string time.
  args:
    - ${resp.json()}
    - date_created
    # - 2020-10-26 will failure to assert
    - "2020-10-26"  # if set 2020-10-26, it will be date obj. Must to set "2020-10-26"
```

## 断言2: 断言可变内容
- Mission: 判断response中的date_modify的日期是否为今天
- 分解1: 将get_current_day的返回值写入到变量: ${expected_date}中
- 分解2: 断言resp.json中的date_modify和${expected_date}是否相等

```
# get_current_day


@keyword
def get_current_day(_format="%Y-%m-%d"):
  """
  get current date, return _format is %Y-%m-%d
  """
  import datetime
  return datetime.datetime.now().strftime(_format)


# yaml例子
-
  keyword: assert_equal_by_dpath
  name: assert time by variable.
  args:
    - ${resp.json()}
    - date_modify
    - ${expected_date}
  run_func:
    -
      keyword: get_current_day
      args:
        - "%Y-%m-%d"
      saved_var_names:
        -
          name: ${expected_date}
      # type: set_global_variable, set_suite_variable, set_test_variable
      type: set_test_variable
```


## 断言3: 模糊路径匹配VS精确路径匹配
- 模糊路径: \*\*/href
- 精确路径: _links/up/0/href
  
**注:** \*\*/href, dpath会找出所有的key, 然后get_value_by_path返回第一个匹配的值(**第一个**, 可能不是你想象的第一个)


```yaml
- 
  keyword: assert_equal_by_dpath
  name: assert href by fuzzy dpath. 
  args: 
    - ${resp.json()}
    # - "**/name"
    # - Color
    - "**/href"
    - https://example.com/wp-json/wc/v3/products/22
- 
  keyword: assert_equal_by_dpath
  name: assert href by specify dpath. 
  args: 
    - ${resp.json()}
    - _links/up/0/href
    - https://example.com/wp-json/wc/v3/products/22
```
```python
# get_value_by_path获取匹配到的第一个值
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
    return result
```

## 断言4: 断言对象
- Mission: 判断response中的_links/collection是否是字典列表
- 分解1: 将get_collection的返回值写入到变量: ${collection}中
- 分解2: 断言resp.json中的_links/collection和${collection}是否相等

```python
@keyword
def get_collection():
    return [{'href': 'https://example.com/wp-json/wc/v3/products/22/variations'}]
```

```yaml
- 
  keyword: assert_equal_by_dpath
  name: assert a python object. 
  args: 
    - ${resp.json()}
    - _links/collection
    - ${collection}
  run_func:
    - 
      keyword: get_collection
      saved_var_names: 
        - 
          name: ${collection}
      # type: set_global_variable, set_suite_variable, set_test_variable
      type: set_test_variable
```

# 我是总结
本文主要介绍了使用[dpath](https://pypi.org/project/dpath/)获取reponse的key-value并进行断言
