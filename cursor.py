import pyautogui


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x_value(self):
        return self.x

    def get_y_value(self):
        return self.y

    def set_value(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Cursor:
    def __init__(self, scale):
        # Always use a scale that is higher than the target resolution.
        self.x_size_translation_key = scale / pyautogui.size().width
        self.y_size_translation_key = scale / pyautogui.size().height

    # Uses an x location and a y location
    def move_to(self, move_location_x, move_location_y):
        pyautogui.moveTo(
            move_location_x / self.x_size_translation_key,
            move_location_y / self.y_size_translation_key
        )
        _pos = Vector2(
            move_location_x / self.x_size_translation_key,
            move_location_y / self.y_size_translation_key
        )
        return _pos

    # Takes a Vector2 instead of separate x and y locations
    def move_to(self, cursor_pos):
        pyautogui.moveTo(
            cursor_pos.get_x_value() / self.x_size_translation_key,
            cursor_pos.get_y_value() / self.y_size_translation_key
        )
        _pos = Vector2(
            cursor_pos.get_x_value() / self.x_size_translation_key,
            cursor_pos.get_y_value() / self.y_size_translation_key
        )
        return _pos

    def get_translation_keys(self):
        return Vector2(self.x_size_translation_key, self.y_size_translation_key)
