import yaml


class Utils:
    """A class with a set of functions for surface work."""
    @staticmethod
    def yaml_reader(yaml_path: str):
        with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
            return yaml.safe_load(yaml_file)
