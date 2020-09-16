#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ruamel.yaml import YAML
from ruamel.yaml.constructor import SafeConstructor


class YamlReader(object):
    """docstring for YamlReader"""

    def __init__(self):
        super(YamlReader, self).__init__()
        # self.yaml = YAML(typ='safe')
        self.yaml = YAML()
        self.yaml.allow_duplicate_keys = True

    def yaml_to_dict(self, yaml_file):
        import codecs

        with codecs.open(yaml_file, 'rb', 'utf-8') as f:
            return self.yaml.load(f)
