
import os
import yaml


class Config(object):

    def __init__(self, config):
        self._config = config

    def __repr__(self):
        return repr(self._config)

    def __getattr__(self, key):
        if key in self._config:
            return self._config[key]

    def get(self, *args, **kwargs):
        return self._config.get(*args, **kwargs)


_config = None


def load():
    global _config
    if _config is not None:
        return _config
    data = None
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yml')
    with open(config_path) as f:
        data = yaml.load(f)
    config = data.get('common', {})
    flavor = os.environ.get('SETTINGS_FLAVOR', 'dev')
    config.update(data.get(flavor, {}))
    config['flavor'] = flavor
    _config = Config(config)
    return _config
