# -*- coding:utf-8 -*-
import sys
import os
import ConfigParser
import collections
import logging
import logging.config


class ConfigUtil:
    def __init__(self):
        self.Configurations = collections.defaultdict()
        self.sys_conf_file_path = os.path.sep.join([sys.path[0], '..', 'conf', 'sys_config.ini'])  # 获取配置文件的路径
        log_conf_file_path = os.path.sep.join([sys.path[0], '..', 'conf', 'logging_config.ini'])   # 获取日志配置的路径

        logging.config.fileConfig(log_conf_file_path)
        self.logger = logging.getLogger("logging")

        if os.path.exists(self.sys_conf_file_path) and os.path.isfile(self.sys_conf_file_path):
            self.logger.info('loading logging config file:{log_file}'.format(log_file=log_conf_file_path))
            self.conf = ConfigParser.ConfigParser()
            self.conf.read(self.sys_conf_file_path)
        else:
            self.logger.error('can not find system config file:{log_file}'.format(log_file=self.sys_conf_file_path))
            exit(-1, 'can not find System config file:{log_file}'.format(log_file=self.sys_conf_file_path))

    def get_config(self, conf, section='default'):
        """
        从系统配置文件中获取配置信息
        :param conf: 配置项名称
        :param section: 配置项的段
        :return: 配置文件中的配置信息,如果不存在返回None
        """
        if self.conf.get(section, conf) is None:
            self.logger.error('can not find configuration {section}.{conf} in system config file'
                              .format(section=section, conf=conf))
            return None
        else:
            return self.conf.get(section, conf)

    def set_config(self, conf, vaule, section='default'):
        """
        修改配置文件中的配置项
        :param conf: 配置名称
        :param vaule: 修改后的配置值
        :param section: 配置section信息
        :return: None
        """
        self.conf.set(section, conf, vaule)
        self.conf.write(open(self.sys_conf_file_path, "w"))  # 配置项写回配置文件中

