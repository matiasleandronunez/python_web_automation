import os
import json

settings = None


class Settings(object):
    """Simple singleton class for managing and accessing settings"""
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsettings.json')) as f:
            settings = json.load(f)
            self.url = settings['url']
            self.api_uri = settings['api_uri']
            self.grid_uri = settings['grid_uri']
            self.default_browser = settings['default_browser']
            self.driver_timeout = int(settings['driver_timeout'])
            self.execute_in_grid = settings['execute_in_grid']


settings = Settings()
