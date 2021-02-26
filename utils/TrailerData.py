"""
"""
from configparser import ConfigParser

class TrailerData:
    def load_config(self):
        try:
            config = ConfigParser()
            config.read('tf.cfg')
            common = config['common']
            self._unit = common['unit']

            trailer = config['trailer']
            self._width = int(trailer['width'])
            self._height = int(trailer['height'])
            self._depth = int(trailer['depth'])
        except:
            pass

    def __init__(self):
        self._unit = 'meter'
        self._width = 1
        self._height = 1
        self._depth = 1

        self.load_config()

    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def depth(self):
        return self._depth
    @property
    def unit(self):
        return self._unit
