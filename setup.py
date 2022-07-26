#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("defergo/README.MD", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(name='defergo',  # 包名
      version='0.0.5',  # 包的版本号
      description='go defer in py',  # 包的介绍、概述
      author='aadog',  # 包的作者
      author_email='97077088@qq.com',  # 邮箱
      url='https://github.com/aadog/defer-py',  # 项目源代码地址 一般的填git地址
      packages=find_packages(),  # Python导入包的列表 可以find_packages() 来自动收集
      long_description=long_description,  # 项目的描述 读取README.md文件的信息
      long_description_content_type="text/markdown",  # 描述文档README的格式 一般md
      license="GPLv3",  # 开源协议
      # 这 需要去官网查，在下边提供了许可证连接 或者 你可以直接把我的粘贴走
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent"],

      # python_requires='>=3.0',  # Python的版本约束
      # 其他依赖的约束
      install_requires=[],
      )