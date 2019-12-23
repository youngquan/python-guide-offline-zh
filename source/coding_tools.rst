.. _coding_tools:

代码编写工具
=======================

Pycharm
-----------------

Pycharm 是 JetBrains 公司针对 Python 推出的专业开发工具。就像 IDEA 在 Java 工程师之间的流行，Pycharm 也无可争议的是目前最好用的 Python IDE。它提供了强大的智能提示功能，支持大量的 Web 框架和性能测试工具，**并具备远程运行、调试程序的功能。** 远程调试运行 Python 程序的功能有时是非常实用的，因为经常我们编写的 Python 代码是需要运行在 Linux 服务器上的，而不是运行在本地的 Windows 服务器上。

VSCode
-----------------

**虽然 Pycharm 功能强大，但有时会觉得 Pycharm 过于庞大和笨重，启动速度感人。因此，有时你还会需要 VScode 的帮助。** VSCode 是微软开源的一款现代化编辑器，支持各种语言，并以扩展的模式提供了强大的功能支持，Nodepad ++ 肯定因为 VSCode 减少了不少用户。最近微软在极力推广 Python，还推出了远程模式的VSCode，还官方支持了 NoteBook。不管怎样，当你需要打开单个 Python 文件，或者需要阅读某个项目的源码时，VsCode 都是一个不错的选择。

Jupyter
-----------------

Jupyter 项目主要提供交互式计算，帮助用户在数据探索和算法设计阶段，获知代码的中间结果，从而迭代地去编写并改进代码。**事实上，我们无法一次性就设计好代码逻辑，而需要在获知代码中间结果的基础上，持续编程。**

Jupyter 的名称来自，Julia、Python 和 R 三种编程语言的组合，以表明它对这三种编程语言的支持。然而事实上，目前 Jupyter 已经支持 40 种编程语言的交互式计算了。Jupyter 项目包含了多个子项目，包括 JupyterNotebook、JupyterLab和JupyterHub。

JupyterLab 是下一代的 JupyterNotebook，提供了一个基于 Web 的交互式开发环境，整合了 Notebook 的功能，并同时提供了多种数据的预览，相比 Notebook 有更好的 UI 设计和体验。同时，JupyterLab 还提供了可扩展的模块化支持，阿里的 PI 平台中关于拖拽神经网络的模块便是基于 JupyterLab 开发。

JupyterHub 则主要面向多用户，通过 JupyterHub 你可以方便地为多个的用户提供交互式开发服务，而不相互影响。