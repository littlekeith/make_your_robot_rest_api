# RequestsLibrary之get请求
上篇, 介绍了使用yaml配置用例, 并通过robot api执行并生成结果的方法.  
  
本文将带你了解:  

- requestslibrary如何发送get请求
- yaml配置接口测试用例的结构
- 使用robot断言库进行简单断言

## 我是如何设计yaml结构的
秉承配置简单的原则, 即  

- 抽离公共属性, 比如接口地址和请求方法只需配置一次
- 用例对应不同的请求数据和断言
- 可配置前提条件/后置处理
- 可配置的关键字库

### 先看下yaml的例子
这里, 我们使用get请求本地项目的/user/logout接口.   
断言是判断请求响应的状态码, 因为本地设置了权限, 所以直接请求会返回401状态码 
```yaml
config:
  name: Activate Variable
  uri: /user/logout
  method: get
  librarys:
    - RequestsLibrary
    - keywords/dynamic_save.py
    - keywords/asserts.py
  setup:
    keyword: create_session
    args:
      - localenv
      - http://127.0.0.1:5000/v2

testcases:
-
  name: simple send get request
  tags: smoke
  payloads: null
  session: localenv
  assign: 
    - ${resp}

  assertions:
    - 
      keyword: log
      args: 
        - ${resp.json()}
    - 
      keyword: assert_equal
      args: 
        - ${resp.status_code}
        - 401

```

**下面**, 我们来解剖下yaml  

## Config节点之Setup
setup节点用来配置suite的setup  

- **keyword**: create_session关键字, 创建httpsession
- **args**: create_session参数, 这里只用到alias和url参数, 具体参数及含义可参见**RequestsLibrary**源代码
    + **localenv**: session 别名, 后期可通过这个别名发起get/post等请求
    + http://127.0.0.1:5000/v2: 服务器地址

## 接口信息
- uri: /user/logout -> 接口地址
- method: get -> 请求方法, 对应get_requests函数
- payloads: 请求数据, 没有就填null
- session: localenv -> session的别名, 对应setup中create_session中的alias参数
- assign: - ${resp} -> 保存响应数据, assertions中可直接使用该变量
  
**下面是核心代码**

## 断言
这里简单通过响应的状态码来判断  

- **keyword**: assert_equal -> 直接使用robot自带断言库进行断言
- args: 参数
    + ${resp.status_code} -> 注意这种写法, 可以直接获取对象的属性
  

看到这里, 是不是觉得robot api简单实用呢.  

# 我是预告
在本文中, 在断言中我们直接了解到获取对象属性的写法, 接下来：  
介绍**如何对reponse json进行断言**  
  
大家可以先想想怎么做, 有哪些方法, 哪种简单  
答案将在本系列文章的下一篇介绍

