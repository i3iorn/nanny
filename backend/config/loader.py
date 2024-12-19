import yaml
import os

class Config:
    def __init__(self, config_path=None):
        if config_path is None:
            # Default to config.yaml in the same directory
            config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, 'r') as f:
            self._config = yaml.safe_load(f)

    def get(self, key, default=None):
        return self._config.get(key, default)
