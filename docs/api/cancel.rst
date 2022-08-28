
Cancel a Contract (cancel)
===========================================================

Cancel contract with contract id

Auth Scope(s): :code:`trade`


.. py:method:: cancel(cancel: int, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param cancel: Value should be the `contract_id` which received from the `portfolio` call.
   :type cancel: int
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.cancel

  binary.api.cancel(
      11542203588
  )

.. seealso::
   * `Binary API Docs for cancel <https://developers.binary.com/api/#cancel>`_
    