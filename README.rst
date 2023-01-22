Note
============

This is a fork of the library by Stone Hippo available `HERE <https://github.com/stonehippo/CircuitPython_Bela_Trill>`_.

I made this fork to simplify some of the code and optimize it for my usage. I only have the Bela Trill Square so I can only test with that but it should work with the others, but if you have trouble let me know and I may be able to help. The example below should also work with the square sensor, unlike the original example.

Introduction
============

A CircuitPython driver for the `Bela.io Trill touch sensors <https://bela.io/products/trill/>`_

Dependencies
============

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

Setting up a single Trill touch sensor is straightforward, when using the default I2C address's and scan settings.

.. code-block:: python

  import board
  import time
  import busio
  import bela_trill
  import touch

  i2c = busio.I2C(board.PERIPHERAL_SCL, board.PERIPHERAL_SDA)

  square = bela_trill.Square(i2c)
  trill = touch.Touches(square)

  while True:
    print("Total touches detected: " + str(trill.get_num()))
    if int(trill.get_num()) >= 1 :
    # only need to run this if a touch is detected
      print("Horizontal touches detected: " + str(trill.get_precise("h")))
      print("Vertical touches detected: " + str(trill.get_precise("v")))
      for i in range(trill.get_num()):
        # subtract 1 due to indexing begging at 0
        index = i - 1
        print("Touch " + str(i) + " detected at " + str(trill.get_touch(index)))
    time.sleep(0.5)
    # the time is pretty high here for readability purposes.
