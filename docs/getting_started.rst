===============
Getting Started
===============

.. code-block:: python

    # High Level API, This API is based on "binaryapi.api" for easy usage
    from binaryapi.stable_api import Binary

    # Low Level API
    from binaryapi.api import BinaryAPI

------------
Requirements
------------

Requires **Python 3.7.0** or later.

------------
Installation
------------

.. code-block:: none

    pip install -U git+https://github.com/mdn522/binaryapi.git


-----------
Basic Usage
-----------

""""""
Import
""""""

.. code-block:: python

    from binaryapi.stable_api import Binary


"""""""""""""""""""
Enabling Debug Logs
"""""""""""""""""""

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


"""""""""""""""
Authorize/Login
"""""""""""""""

.. code-block:: python

    binary = Binary(token="YOUR-API-TOKEN-GOES-HERE")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Authorize/Login with a message handler/callback function
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: python

    def message_handler(msg):
        msg_type = msg.get('msg_type')

        print(msg_type, "=>", msg)

    binary = Binary(token="YOUR-API-TOKEN-GOES-HERE", message_callback=message_handler)


----
Misc
----

.. note::

   * In any code example: ``binary`` is instance of ``binaryapi.stable_api.Binary``
   * ``binary.api`` is instance of ``binaryapi.api.BinaryAPI``
   * All low level API functions are under ``binaryapi.api.BinaryAPI``
   * So you can call it like ``binary.api.buy``, ``binary.api.ticks_history``, etc. (considering you named the instance ``binary``)