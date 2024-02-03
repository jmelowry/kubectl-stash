#!/usr/bin/env python3

import os
import json

class ConfigManager:
    def __init__(self):
        self.config_file_path = self._find_config_file_path()

    def _find_config_file_path(self):
        """Determines the correct path for the .kubectl-stash configuration file."""
        local_config_path = os.path.join(os.getcwd(), '.kubectl-stash')
        home_config_path = os.path.join(os.path.expanduser('~'), '.kubectl-stash')
        
        # Use the local config file if it exists, otherwise use the one in the home directory
        return local_config_path if os.path.isfile(local_config_path) else home_config_path

    def load_config(self):
        """Loads the configuration from the .kubectl-stash file, if it exists."""
        try:
            with open(self.config_file_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            return {}  # Return an empty dict if the config file doesn't exist

    def save_config(self, config):
        """Saves the given configuration to the .kubectl-stash file."""
        with open(self.config_file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4, sort_keys=True)

    def update_config(self, **kwargs):
        """Updates the configuration file with provided key-value pairs."""
        config = self.load_config()
        config.update(kwargs)
        self.save_config(config)
