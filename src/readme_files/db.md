# markdown使用说明
https://blog.csdn.net/Kwoky/article/details/107604775
# 数据库说明
## mysql
### mysql安装和配置
https://blog.csdn.net/weixin_52097724/article/details/128576284
https://blog.csdn.net/ladymorgana/article/details/129286445
### nvicat安装和配置
https://mp.weixin.qq.com/s?__biz=Mzg3ODA5ODY3MQ==&mid=2247497982&idx=1&sn=d1c3b24441fa3b2bf9a40a8d2eba983b&chksm=cf1a597ef86dd0687b57a21194d66ac18ce8c61812ae69672a79137635bb9fdbf5cbe13d4a40&scene=27
### docker-compose
version: '3.1'

services:
  master-mysql:
    platform: linux/x86_64
    image: mysql:latest
    container_name: mysql
    ports:
      - 3306:3306
    restart: always
    environment:
      TZ: Asia/Shanghai
      MYSQL_ROOT_PASSWORD: 123456
    command:
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
      --default-authentication-plugin=mysql_native_password
    volumes:
      - ./conf.d:/etc/mysql/conf.d
      - ./data:/var/lib/mysql
#networks:
//  default:
//    external:
//      name: xph_network

## mysql连接池实现方式
https://blog.csdn.net/s1t16/article/details/128031369

## mongodb
https://blog.csdn.net/ladymorgana/article/details/129286602

## linux命令
根据端口获得进程号
lsof -i :8080 | grep -i LISTEN | awk '{print $2}'
组合获得该进程的执行命令
lsof -i :8080 | grep -i LISTEN | awk '{print $2}' | xargs -I {} ps -o command -p {} | tail -n +2
管道给kill掉该进程
lsof -i :8080 | grep -i LISTEN | awk '{print $2}' | xargs -I {} kill -15 {}
