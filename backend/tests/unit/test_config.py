from config.loader import Config

def test_config_loading():
    config = Config()
    assert config.get("database") is not None
