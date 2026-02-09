import json
import os
from pathlib import Path

class ConfigManager:
    """Manages loading and saving configuration data for the portfolio website."""
    
    def __init__(self, config_path='config.json'):
        """
        Initialize the ConfigManager.
        
        Args:
            config_path: Path to the configuration JSON file
        """
        # Get the absolute path to the config file (in the project root)
        self.base_dir = Path(__file__).resolve().parent.parent
        self.config_path = self.base_dir / config_path
        self._config = None
        self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file."""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self._config = json.load(f)
                print(f"Configuration loaded from {self.config_path}")
            else:
                print(f"Warning: Config file not found at {self.config_path}")
                self._config = self._get_default_config()
        except json.JSONDecodeError as e:
            print(f"Error parsing config file: {e}")
            self._config = self._get_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self._config = self._get_default_config()
    
    def save_config(self, config_data=None):
        """
        Save configuration to JSON file.
        
        Args:
            config_data: Dictionary to save. If None, saves current config.
        """
        try:
            data_to_save = config_data if config_data is not None else self._config
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=2, ensure_ascii=False)
            print(f"Configuration saved to {self.config_path}")
            if config_data is not None:
                self._config = config_data
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def get(self, key=None, default=None):
        """
        Get configuration value by key.
        
        Args:
            key: Dot-notation key (e.g., 'personal.name' or 'site.title')
                 If None, returns entire config.
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        if key is None:
            return self._config
        
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def update(self, key, value):
        """
        Update a configuration value.
        
        Args:
            key: Dot-notation key (e.g., 'personal.name')
            value: New value
            
        Returns:
            True if successful, False otherwise
        """
        keys = key.split('.')
        config = self._config
        
        # Navigate to the parent of the target key
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # Set the value
        config[keys[-1]] = value
        return self.save_config()
    
    def _get_default_config(self):
        """Return default configuration if file doesn't exist."""
        return {
            "site": {
                "title": "Portfolio Website",
                "description": "My Portfolio",
                "logo": "/static/Content/Icons/wizardLogo.png"
            },
            "personal": {
                "name": "Your Name",
                "title": "Software Engineer",
                "bio": "Your bio here"
            },
            "navigation": [],
            "projects": [],
            "social": {}
        }

# Global instance
_config_manager = None

def get_config_manager():
    """Get or create the global ConfigManager instance."""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager
