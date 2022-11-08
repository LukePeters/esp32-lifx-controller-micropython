# LIFX Controller

Powered by an ESP-WROOM-32 board. The OLED display uses the SSD1306 driver.

## Dependency Information

- Using MicroPython and its builtin modules:
  - `time` for sleep delays
  - `machine` for controlling pins
  - `network` for connecting to WiFi
  - `urequests` for sending HTTP requests
- My own packages and manually downloaded modules should live in the `lib` directory, which lets me easily import them in `boot.py` and `main.py`

## Original Project by Luke Peters

![LIFX Controller](./images/enclosure.jpg)
![LIFX Controller](./images/components.jpg)
![LIFX Controller](./images/enclosure_back.jpg)
![LIFX Controller](./images/pcbs.jpg)