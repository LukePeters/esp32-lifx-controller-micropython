from boot import display, DISPLAY_LINE_HEIGHT, DISPLAY_MAX_LINES

class Menu:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items
        self.length = len(items)
        self.selected_item = 0
        self.scrolled_lines = 0
    
    def set_items(self, items):
        self.items = items
        self.length = len(items)
    
    def render(self):
        display.fill(0)
        y = 0

        for idx, val in enumerate(self.items):

            # Only show as many lines as will fit on the display
            if (idx + 1) > DISPLAY_MAX_LINES:
                break

            menu_item_index = self.scrolled_lines + idx
            prefix = '|' if idx == (self.selected_item - self.scrolled_lines) else ' '

            display.text(f'{prefix}{self.items[menu_item_index]["name"]}', 0, y)

            y += DISPLAY_LINE_HEIGHT
        
        display.show()
    
    def scroll(self, direction):

        # Change the selected menu item
        if direction == 'down':
            if self.selected_item < (self.length - 1):
                self.selected_item += 1
        else:
            if self.selected_item > 0:
                self.selected_item -= 1

        # Scroll the menu up/down
        scrollable_lines = (self.length - DISPLAY_MAX_LINES)
        
        if direction == 'down':
            # Moved below the last visible item
            if (self.selected_item + 1) > DISPLAY_MAX_LINES:
                if self.scrolled_lines < scrollable_lines:
                    self.scrolled_lines += 1
        
        elif direction == 'up':
            # Moved above the first visible item
            if (self.selected_item - self.scrolled_lines) < 0:
                self.scrolled_lines -= 1