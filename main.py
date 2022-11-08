from machine import Pin
from time import sleep
import urequests
from menu import Menu
from button import Button
from boot import display
import tools

BUTTON_UP = Button(4)
BUTTON_DOWN = Button(5)
BUTTON_ACTION = Button(18)
SCENES_MENU = Menu('Scenes Menu')

render_required = True
display_enabled = True

# CONNECT TO WIFI
station = tools.connect_to_wifi()

# THE MAIN PROGRAM LOOP
# While connected, handle all device functionality. Reconnects automatically.
while station.isconnected():

    # GET LIFX SCENES
    if not SCENES_MENU.items:
        items = tools.get_lifx_scenes()
        items.insert(0, { 'id': 'toggle_power', 'name': 'Power On/Off' })
        SCENES_MENU.set_items(items)

    # UP BUTTON
    if BUTTON_UP.pressed():
        SCENES_MENU.scroll('up')
        render_required = True

    # DOWN BUTTON
    if BUTTON_DOWN.pressed():
        SCENES_MENU.scroll('down')
        render_required = True
    
    # ACTION BUTTON
    action_btn_pressed = BUTTON_ACTION.pressed()
    
    # Activate the selected scene
    if action_btn_pressed == 1:
        menu_item = SCENES_MENU.items[SCENES_MENU.selected_item]

        if menu_item['id'] == 'toggle_power':
            tools.toggle_lifx_power()
        else:
            tools.set_lifx_scene(menu_item)

        sleep(2)
        render_required = True
    
    # Toggle the display on/off
    elif action_btn_pressed == 2:
        if display_enabled:
            display.poweroff()
            display_enabled = False
        else:
            display.init_display()
            display_enabled = True
            render_required = True
    
    # RENDER THE SCENES MENU
    if render_required:
        SCENES_MENU.render()
        render_required = False
    