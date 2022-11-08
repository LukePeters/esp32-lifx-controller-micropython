import network
import urequests
from time import sleep
from boot import display, graphics, BUILTIN_LED

def connect_to_wifi():
    write_centered('Connecting...')

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect('YOUR_SSID', 'YOUR_SSID_PASSWORD')

    while not station.isconnected():
        blink_led(BUILTIN_LED, 0.2, 0.2)
    
    if station.isconnected():
        write_centered('Connected!')
        blink_led(BUILTIN_LED, 1)
    
    return station

def blink_led(led, duration, delay=0):
    led.on()
    sleep(duration)
    led.off()
    sleep(delay)

def get_lifx_headers():
    return {'Authorization': 'Bearer YOUR_LIFX_APP_TOKEN'}

def get_lifx_scenes():
    write_centered('Loading...')

    scenes = []
    resp = urequests.request('GET', 'https://api.lifx.com/v1/scenes', headers=get_lifx_headers())

    for scene in resp.json():
        scenes.append({ 'id': scene['uuid'], 'name': scene['name'] })
    
    resp.close()
    return scenes

def set_lifx_scene(scene):
    write_centered('Activating...')
    resp = urequests.request('PUT', f'https://api.lifx.com/v1/scenes/scene_id:{scene["id"]}/activate', headers=get_lifx_headers())
    resp.close()
    write_centered(f'{scene["name"]}', True)

def toggle_lifx_power():
    write_centered('Toggling...')
    resp = urequests.request('POST', f'https://api.lifx.com/v1/lights/all/toggle', headers=get_lifx_headers())

    # Response
    data = resp.json()
    power_state = 'On' if data['results'][0]['power'] == 'on' else 'Off'

    resp.close()
    write_centered(f'Powered {power_state}!', True)

def write_centered(text, border=False):
    char_width = 8
    max_chars = 16
    text_length = len(text)
    lpadding = 0

    if text_length < max_chars:
        lpadding = int((max_chars - text_length) / 2) * char_width
    
    display.fill(0)
    display.text(text, lpadding, 27)

    if border:
        graphics.rect(0, 0, 128, 64, 1)
    
    display.show()

def write_multiline(lines):
    display.fill(0)
    y = 0

    for line in lines:
        display.text(line, 0, y)
        y += 10
    
    display.show()