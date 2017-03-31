# -*- coding:utf-8 -*-
from config_util import ConfigUtil


class HDFSUtil:
    def __init__(self):
        conf = ConfigUtil()
        self.HIVE_BASE_DIR = conf.get_config('HIVE_BASE_DIR')
        self.Databases = conf.get_config('DBName').split(',|，')

    def list_file(self,hdfs_path):
        pass
