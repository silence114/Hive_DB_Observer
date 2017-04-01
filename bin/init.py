# -*- coding:utf-8 -*-
from util.config_util import ConfigUtil


# 获取数据库信息
def get_database_list():
    conf = ConfigUtil()
    HIVE_BASE_DIR = conf.get_config('HIVE_HOME')




