.. _protectpythoncode:

保护 Python 代码
======================

现有解决方案
----------------------

知乎网友 `Prodesire <https://www.zhihu.com/people/prodesire/activities>`_ 发表了两篇文章介绍了他的 Python源代码加密解决方案，值得参考：

1. `如何保护你的 Python 代码 （一）—— 现有加密方案 <https://zhuanlan.zhihu.com/p/54296517>`_

2. `如何保护你的 Python 代码 （二）—— 定制 Python 解释器 <https://zhuanlan.zhihu.com/p/54297880>`_


全新解决方案
----------------------

Python wiki 里面有一个关于 `How do you protect Python source code? <https://wiki.python.org/moin/Asking%20for%20Help/How%20do%20you%20protect%20Python%20source%20code%3F>`_ 的回答，里面提到唯一安全的代码是驻留在远程机器上的代码，同时也提到对于 Java 、C 来说，保护代码也会是徒劳的，而和你的用户建立一个更好的互助关系也是一个不错的选择。但无论如何，在法律还不成熟的中国，保护 Python 代码还是需要做的。针对当前的解决方案都不是特别优雅，我在 Github 上新开了一个项目叫做 `goldenmask <https://github.com/youngquan/goldenmask>`_，希望可以提供一个方便易用的 Python 代码加密工具，让 Python 开发人员能够更加关注在开发这件事上。期待你的加入！

.. 编译为 pyc
.. ------------------------


.. 编译为 so
.. -------------------------

.. 代码混淆
.. --------------------------

.. 修改 Python 解释器
.. ----------------------------