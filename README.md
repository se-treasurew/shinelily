# 闪光利利（shinelily）
>  用python编写的基于酷q、cqhttp和nonebot的QQ机器人

## 废除

由于酷Q已经无法使用，该项目废除。

## 功能（2.0）

> 2020-8-2

- 重构项目结构
- 添加早午晚安功能
- 添加复读功能

### 天气预报

接入“和风天气”api

#### 使用方法

`天气 地名`例如`天气 杭州`

### teach 

#### 使用方法

- 添加键值对：`teach question answer`例如`teach 你叫什么 闪光利利`，便会把相应键值对存入文件
  -`你叫什么`
  -`闪光利利`
- `delete question`删除键值对，例如`delete 你叫什么`,便会删除相应键值对

### rainbow

接入沙雕app的api，提供彩虹屁功能

#### 使用方法

`rainbow`即可回复一句rainbow

### repeater

在群中有重复的消息，bot会复读一句

### greet

早午晚安功能

## 功能（1.0）

> 2020-7-20

- 可以设置是否at触发机器人功能
- `config.py`文件为`nonebot`配置文件
- `my_config.py`文件为我的配置文件（目前用于`myDict.py`的`data_url`）

### 天气预报

接入“和风天气”api

#### 使用方法

`天气 地名`例如`天气 杭州`

### teach 

#### 使用方法

- 添加键值对：`teach question answer`例如`teach 你叫什么 闪光利利`，便会把相应键值对存入文件
  -`你叫什么`
  -`闪光利利`
- `delete question`删除键值对，例如`delete 你叫什么`,便会删除相应键值对

### rainbow

接入沙雕app的api，提供彩虹屁功能

#### 使用方法

`rainbow`即可回复一句rainbow