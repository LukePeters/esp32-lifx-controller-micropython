# LIFX Controller

Powered by an ESP-WROOM-32 board.

## Dependency Information

- Using MicroPython and its builtin modules:
  - `time` for sleep delays
  - `machine` for controlling pins
  - `network` for connecting to WiFi
  - `urequests` for sending HTTP requests
- My own packages/modules should live in the `lib` directory, which lets me easily import them in `boot.py` and `main.py`