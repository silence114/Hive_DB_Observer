drop database if exists db_observer;
create database if not exists db_observer;

drop user 'db_observer'@'localhost';
flush privileges;
create user 'db_observer'@'localhost' identified by 'db_observer';

grant usage on db_observer.* to 'db_observer'@'%' identified by 'db_observer' with
MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0
MAX_USER_CONNECTIONS 0;

grant all privileges on db_observer.* to 'db_observer'@'%';

flush privileges;

--数据库信息表
drop table if exists db_observer.db_info;
create table if not exists `db_observer`.`db_info`
(
     id             int unsigned  not null primary key auto_increment  comment '自增主键'
    ,db_name        varchar(32)   not null default 'default'           comment 'hive数据库名称'
    ,hdfs_path      varchar(128)  not null                             comment 'hive数据库的存储HDFS目录'
    ,table_num      int unsigned  not null default 0                   comment '数据库下的表的个数'
    ,par_table_num  int unsigned  not null default 0                   comment '数据库下的分区表的个数'
    ,db_size        bigint        not null default 0                   comment '数据库存储size，单位字节'
    ,db_admin       varchar(16)   not null default ''                  comment '数据库管理员'
    ,is_delete      tinyint       not null default 0                   comment '数据库是否删除，0：未删除，1：已删除'
    ,db_create_time varchar(32)   not null                             comment '数据库创建时间'
    ,gmt_create     datetime      not null default current_timestamp   comment '记录创建时间'
    ,gmt_modified   datetime      not null default current_timestamp on update current_timestamp comment '记录修改时间'
    ,unique key idx_db_info_dbname (db_name)
)AUTO_INCREMENT = 1000
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8
COMMENT = '数据库信息表';

--表元数据信息表
drop table if exists db_observer.table_info;
create table if not exists db_observer.table_info
(
    id             int unsigned  not null primary key auto_increment  comment '自增主键'
    ,db_id         int unsigned  not null
    ,db_name       varchar(32)   not null default 'default'           comment 'hive数据库名称'
    ,table_name    varchar(64)   not null                             comment 'hive表名'

)
