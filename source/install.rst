.. _install:

Python 安装
=======================

Anaconda 发行版本
----------------------------

Anaconda 是一个包含了大量内置数据科学包的 Python 发行版本，有开源的免费版本，也有收费的企业版本。因为 Anaconda 内置了大量的 Python 包，包括 Jupyter、Spyder、Numpy、Scipy、pandas 等常用的 Python 包，其安装包较大，大概有 500 多M。**正因为内置了大量的 Python 包，在离线环境下选择使用 Anaconda 安装 Python 会是一个明智的选择。** Anaconda 不仅提供了能够在多个平台上（Windows、macOS、Linux）一键安装的可执行二进制文件，还能够避免无法联网安装常见 Python 包的问题，并提供了相应的环境变量配置，能够让系统默认的 python 解释器和 python 命令变成最新安装的 Python 版本。Anaconda 的下载包，可以去 Anaconda 的官网下载。

Python 官方支持
---------------------------

Python 的官网提供了不同 Python 版本的官方安装包，包括了 Python 源码、macOS 安装二进制文件、Windows 安装二进制文件等，也提供了一些不常用平台的安装方法。如果你想要获取最新版本的 Python，便可以去 Python 官网上下载相应的安装包进行安装。

针对 Linux，Python 官方提供的是源码安装方式，**但源码安装 Python 需要有一定的 Linux 操作系统基础，因为源码安装 Python 的时候，需要安装一些额外的系统库和头文件，这样才能完整安装 Python，否则安装的 Python 是不完整的，一些扩展库是无法使用的，比如 zlib、sqlite、readline 等。** 此外，Linux 操作系统大多有自己的软件包管理器，比如 Centos 的 yum、Ubuntu 的 apt，因此我们也可以下载指定 Python 版本相应的 rpm 包及其依赖或者 deb 包及其依赖完成Python 的安装。这里就不详细介绍源码安装 Python 和下载 rpm 包以及 deb 包的方法，具体的操作可以查看我在 Github 上开源的文档仓库：python-guide-offline。