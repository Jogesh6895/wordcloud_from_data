import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class Config:
    def __init__(self, config_path: str = "src/config/settings.yaml"):
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get(self, key_path: str, default: Any = None) -> Any:
        keys = key_path.split(".")
        value = self._config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    @property
    def data(self) -> Dict[str, Any]:
        return self._config.get("data", {})

    @property
    def text(self) -> Dict[str, Any]:
        return self._config.get("text", {})

    @property
    def wordcloud(self) -> Dict[str, Any]:
        return self._config.get("wordcloud", {})

    @property
    def masks(self) -> Dict[str, Any]:
        return self._config.get("masks", {})

    @property
    def output(self) -> Dict[str, Any]:
        return self._config.get("output", {})

    @property
    def variants(self) -> Dict[str, Any]:
        return self._config.get("variants", {})

    def reload(self) -> None:
        self._config = self._load_config()


_config_instance: Optional[Config] = None


def get_config() -> Config:
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance
