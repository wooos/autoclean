import yaml


class CleanPath(object):
    def __init__(self, clean_config):
        self.clean_config = clean_config

    @property
    def directory(self):
        return self.clean_config.get('directory')

    @property
    def filename(self):
        return self.clean_config.get('filename')

    @property
    def expire(self):
        return self.clean_config.get('expire')

    @property
    def command(self):
        return self.clean_config.get('command')


class CleanConfig(object):
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config_data = yaml.safe_load(config_file.read())

    @property
    def paths(self):
        clean_paths = []
        for clean_path in self.config_data.get('autoclean').get('paths'):
            clean_paths.append(CleanPath(clean_path))
        return clean_paths
