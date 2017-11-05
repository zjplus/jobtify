# jobtify

## 简介

jobtify 是job notify的简称,作为自己平时工作的小工具，主要功能使用Python调用linux命令行或者执行脚本，运行结束的时候给自己发一个通知。


## 技术学习点

* subprocess
* 装饰器
* argparse
* celery
* 打包成命令行工具

## 使用方法

1、下载 `git clone https://github.com/zjplus/jobtify.git`

2、安装依赖 在 jobtify目录执行 `pip install -r requirements.txt`

3、配置`config.py` redis 依赖

4、打包安装

5、启动 celery 服务

5、执行工具

```
' arg cmd is needed '
usage: jobtify.py [-h] [-cmd CMD] [-dir DIR]

optional arguments:
  -h, --help  show this help message and exit
  -cmd CMD    shell command
  -dir DIR    work dir
```

参数
* cmd 执行的shell 命令，必须
* dir 工作目录 缺省

例子

```jobtify -cmd "python hello.py"```

执行完之后，会调用notify.py 里的 on_success_notify 和 on_failed_notify 函数
可自定义修改这个两个函数达到通知的效果。

## todo

* 添加普通邮件告警
* 添加定期清理redis的key 或者命令行
* 添加程序配置的redis prefix