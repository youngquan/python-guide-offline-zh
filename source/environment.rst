.. _environment:

无网环境下的 Python 开发依然需要一个 Python 仓库。

本地 Python 仓库
--------------------------------

管理 Python 包最好的工具就是 pip，但因为无法联网，我们无法配置 pip 源，从而随心所欲地下载相应的 Python 包。还好 Python 社区提供了一些搭建本地 Python 仓库的工具，能够方便我们在联网环境中下载需要的 Python 包，拷贝到离线环境后，通过配置本地的 Python 仓库，使用 pip install 命令安装指定的 Python 包。Awesome Python 网站提供了4个用于搭建本地的 Python 仓库，包括 warehouse、bandersnatch、devpi、localshop。warehouse 是Python 官方的 Python 仓库，bandersnatch 是对整个 Python 库的镜像，容量过大。devpi 和 localshop 使用起来都需要更多的精力。**如果只是小型的团队，更加推荐先是使用 Pypiserver，它更加小型，也更加实用。**

虽然说 Python 代码也是跨平台的，但各个 Python 包仍然有不同操作系统和芯片指令集的区别。去查看 PyPi 网站提供的有关 tensorflow 的 Python 包列表，便可以看到不同 Python 版本、不同操作系统以及不同芯片指令集的区别：

因此当我们使用 `pip download` 命令下载 Python 包的时候，默认只是下载当前命令运行平台相关的 Python 包，包括当前的 Python 版本、操作系统以及芯片指令集。在离线环境下，由于导入资料的成本的高昂，我们有时希望一次导入所有版本的 Python 包和依赖；另一方面，又由于我们经常会命令从 Windows 操作系统上下载 Linux 系统上的 Python 包和依赖，我们也希望能够直接下载不同操作系统、不同芯片指令集甚至 Python 版本的 Python 库。**虽然 pip 提供了以下跨平台的操作指令和参数，但有时仍然会因为依赖的问题而导致下载失败。** 因此，如果你需要下载某个 Python 包，我这里会推荐我之前编写的一个 Python 库：pip-download，虽然目前还是我一个人使用，但还是很方便的可以试一下。

虚拟环境
---------------------------

开发的 Python 项目多了以后，便经常会遇到依赖冲突的问题。项目 1 用了 A 版本的 Python 库 package，项目 2 用了 B 版本的 Python 库 package，那么如果都用系统版本的 Python 环境，是无法同时安装同一 Python 库的两个版本。因而，virtualenv 和 Python 3 自带的 venv 模块便能发挥左右。你可以通过执行如下的命令建立虚拟环境，并进行激活，从而拥有一个干净的 Python 依赖：

.. code-block:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate

    $ pip install virtualenv
    $ virtualenv

此外，Anaconda 的 Python 版本也自带了虚拟环境管理工具 conda，Pyenv 则是一个能够建立不同 Python 版本虚拟环境的一个工具，而在 Python 包依赖及其管理上，还有很多知名的工具值得了解：propetry。Python 在包及其依赖上的管理实在过于宽泛，导致了诸多不方便和不一致。但我们还有未来不是吗？