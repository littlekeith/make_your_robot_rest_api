# 重构代码
代码结构
```s
├───src
│   └───robot_yaml
│       ├───config
│       │   └───setttings.py --基本配置(目前只有结果路径,结果名字)
│       ├───datas
│       │   └───yaml_fields.py --yaml文件中使用到的key
│       ├───keywords
│       │   ├───asserts.py --断言关键字
│       │   └───dynamic_save.py --执行函数关键字         
│       ├───model
│       │   ├───testcases.py --创建用例步骤
│       │   ├───teststeps.py --创建关键字
│       │   └───testsuites.py --创建suite步骤
│       ├───outputs --结果保存目录
│       ├───parsing
│       │   ├───arguments.py --解析命令行参数
│       │   ├───dpath_json.py --根据路径获取python对象的值
│       │   └───yamlreader.py --yaml转换成python对象
│       ├───reporting --暂时没用
│       ├───running
│       │   ├───case.py --解析yaml中testcases节点
│       │   └───suite.py --解析yaml中config节点并初始化suite
│       ├───utils
│       │   ├───commons.py --常用函数
│       │   └───diffs.py --获取python列表中相似的key
│       └───run.py --程序主入口
│       
├───tests --simple test
│    └───examples
└───cases.yaml   --用例文件
```

# how to run
- python run.py --help

##  run with no parameter
```

λ cd day9\src\robot_yaml
λ python run.py 
True
==============================================================================
Activate Variable
==============================================================================
Test return list                                                      | PASS |
------------------------------------------------------------------------------
Test return dict                                                      | PASS |
------------------------------------------------------------------------------
Test return string                                                    | PASS |
------------------------------------------------------------------------------
Test setup                                                            | PASS |
------------------------------------------------------------------------------
Activate Variable                                                     | PASS |
4 critical tests, 4 passed, 0 failed
4 tests total, 4 passed, 0 failed
==============================================================================
Output:  day9\src\robot_yaml\outputs\test-output.xml

```

## run with parameter
```
λ cd day9\src\robot_yaml
λ python run.py -o test.xml
True
==============================================================================
Activate Variable
==============================================================================
Test return list                                                      | PASS |
------------------------------------------------------------------------------
Test return dict                                                      | PASS |
------------------------------------------------------------------------------
Test return string                                                    | PASS |
------------------------------------------------------------------------------
Test setup                                                            | PASS |
------------------------------------------------------------------------------
Activate Variable                                                     | PASS |
4 critical tests, 4 passed, 0 failed
4 tests total, 4 passed, 0 failed
==============================================================================
Output:  day9\src\robot_yaml\outputs\test.xml
```
