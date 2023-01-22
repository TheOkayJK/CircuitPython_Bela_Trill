import bela_trill

class Touches(object):

    # inits.
    def __init__(self, trill):
        self.trill = trill

    # Returns the number vertical or horizontal touches. Pass 'v' for vertical and 'h' for horizontal
    def get_precise(self, direction):
        trill = self.trill
        if direction is "v":
            return trill.number_of_vertical_touches()
        elif direction is "h":
            return trill.number_of_horizontal_touches()
        else:
            return None

    # Returns the location of the given touch as a list.
    def get_touch(self, index):
        trill = self.trill
        touch = []
        if index < len(trill.vertical_touches):
            touch_v = trill.vertical_touches[index]
            touch.append(touch_v.location)
        if index < len(trill.horizontal_touches):
            touch_h = trill.horizontal_touches[index]
            touch.append(touch_h.location)
        return touch

    # Returns the max number of touches currently detected.
    # Useful for simplicity and to prevent unnecessary formatting.
    def get_num(self):
        trill = self.trill
        max_t = 0
        max_t = max(trill.number_of_vertical_touches(), trill.number_of_horizontal_touches())
        return max_t
