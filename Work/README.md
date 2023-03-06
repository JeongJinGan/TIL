## 작성하기전 가상머신 네트워크 설정 꼭하기!!

### ❗❗파일 이동 cd /usr/local/src❗❗

# db4-devel 은 설치가 안됨

yum -y install wget cmake ncurses-devel libtool-ltdl expat-devel pcre-devel openssl-devel gcc gcc-c++


yum install wget


yum install bzip2

# apr-1.6.5
wget http://mirror.apache-kr.org/apr/apr-1.6.5.tar.bz2

# apr-util-1.6.3 (1.6.1은 다운이 안됨)
wget http://mirror.apache-kr.org/apr/apr-util-1.6.3.tar.bz2

# httpd-2.4.55 (최신버전)
wget http://mirror.apache-kr.org/httpd/httpd-2.4.55.tar.gz

# pcre-8.45
wget http://downloads.sourceforge.net/project/pcre/pcre/8.45/pcre-8.45.tar.bz2 

# 다운받은 압축파일 압축풀기

tar xvf apr-1.6.5.tar.bz2
tar xvf apr-util-1.6.3.tar.bz2
tar xvf httpd-2.4.55.tar.gz
tar xvf pcre-8.45.tar.bz2

ls로 압축 풀렸나 확인해보기


# apr 설치
> - ./configure시 에러 : cp -arp libtool libtoolT
- a : archive 기록/예방 r : 디렉토리 하위까지 복사 p : 원본 파일 정보 보존하여 복사
cd /usr/local/src/apr-1.6.5/

./configure --prefix=/usr/local/apr
make
make install

# apr-util 설치
cd /usr/local/src/apr-util-1.6.3/

./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr

make

make install

# pcre 설치
cd /usr/local/src/pcre-8.45/

./configure --prefix=/usr/local/pcre

make

make install

# apache 설치 (httpd-2.4.55)
cd /usr/local/src/httpd-2.4.55/

./configure --prefix=/usr/local/apache --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util --with-pcre=/usr/local/pcre --enable-mods-shared=all --enable-so --enable-rewrite --enable-auth-digest

> 위 과정에서 error: Did not find pcre-config script at ~~ 에러 났을 시

>--with-pcre=/usr/local/pcre/ 이 경로를
>--with-pcre=/usr/local/pcre/bin/pcre-config 로 변경

make

make install

# 서버 url 설정해주기
cd /
해서 초기 디렉토리로 이동 후

vi usr/local/apache/conf/httpd.conf
들어가서 ? or / 입력 후 ServerName 검색후 주석 지워준 뒤 i 를 눌러


ServerName localhost:80
으로 변경

ESC키 누르고 저장

```bash
변경 후
ServerTokens와 ServerSignature 설정 아무데나 추가해주기

ServerTokens Prod

ServerSignature Off

그리고 디렉토리 리스팅을 방지하기 위해
?The Options directive
를 검색해 나오는
Options Indexes FollowSymLinks를
Options으로 저장
```

:wq
로 저장하고 나가기(잘못 고쳤으면 :q 입력후 저장하지 않고 나가기)

/usr/local/apache/bin/httpd -k start
로 아파치를 시작하고

ps -ef | grep httpd
로 아파치가 켜져있나 프로세스 확인

curl localhost
를 입력해서 결과값이

<html><body><h1>It works!</h1></body></html>
가 나오면 설치 완료.

/usr/local/apache/bin/httpd -k stop

curl localhost
로 서버가 꺼졌나 확인.





### mysql설치
필수유틸 설치
yum -y install ncurses-devel gcc gcc-c++ zlib curl libtermcap-devel lib-client-devel bzip2-devel cmake bison perl perl-devel
 root

- 위에꺼 lib-client-devel 설치 안됨

압축파일 다운 및 해제
 cd /usr/local/src

[다운받기전 아래 에러 참조(버전 변경 필요)/ ,mysql-5.6.14버전으로 진행] 

 wget http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.14.tar.gz
  tar xvf mysql-5.6.14.tar.gz

> wget http://~~ -> wget: unable to resolve host address 'dev.mysql.com' 
> 에러 났을시 
> -> vi /etc/resolv.conf 
> nameserver 8.8.8.8 ----->추가

파일 이동 cd /usr/local/src/mysql-5.6.14



```bash
mysql-5.6.14 아래와 같은 에러로
mysql-5.6.51 버전으로 다운


gmake[2]: *** [storage/innobase/CMakeFIles/innobase_embedded.dir/build.make:1322: storage/innobase/CMakeFiles/innobase_embedded.dir/srv/srv0mon.cc.o] Error 1

gmake[1] : *** [CMakeFiles/Makefile2:1800: storage/innobase/CMakeFiles/innobase_embedded.dir/all] Error 2
```







#### Mysql 컴파일 설치
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/datag

> cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/data 
>
> 맨 뒤 datag, data 뭐가 맞는지 잘 모르겠다.. 가이드북에는 datag라고 적혀있기는 함.
> 일단, data로 진행.

gmake

gmake install

> cmake -DCMAKE ~~ 에러
> yum -y install openssl-devel 추가



#### Mysql 유저생성 및 그룹 계정권한주기
groupadd mydba

useradd mysql

chown -R mysql:mydba /usr/local/mysql

chown -R mysql /usr/local/mysql/data


- groupadd : 새로은 그룹을 생성하는 명령어
- useradd : 새로운 사용자를 생성하는 명령어
* 옵션 -M : 사용자 home디렉토리를 생성하지 않는다.
* 옵션 -c : 사용자의 설명문
* 옵션 -d : home디렉토리 지정 :home디렉토리를 생성후 지정하려면 -m으로 사용
* 옵션 -g : 소속될 그룹을 지정한다.
* 옵션 -s : 사용할 쉘을 지정한다.

#### Mysql DB 생성
cd /usr/local/mysql

./scripts/mysql_install_db --user=mysql --datadir=/usr/local/mysql/data

> /usr/bin/perl: bad interpreter: No such file or directory 에러
> -> 해결 yum install perl 설치



#### Mysql 설정파일 및 데몬 복사 및 수정
cp support-files/my-default.cnf /etc/my.cnf
라는 명령어를 사용시 cp: overwrite '/etc/my.cnf'? 라는 문구 출력시 y입력

vi /etc/my.cnf
맨 아래부분에 추가해 준다.

innodb_buffer_pool_size = 16M

innodb_additional_mem_pool_size = 2M

innodb_log_file_size = 5M

innodb_log_buffer_size = 8M

innodb_flush_log_at_trx_commit = 1

innodb_lock_wait_timeout = 50

explicit_defaults_for_timestamp = TRUE


#### Mysql Path 등록 (주요기능을   간편히 사용하기 위한)
ln -s /usr/local/mysql/bin/mysql /usr/bin/mysql

ln -s /usr/local/mysql/bin/mysqldump /usr/sbin/mysqldump

ln -s /usr/local/mysql/bin/mysql_config /usr/sbin/mysql_config

ln -s /usr/local/mysql/bin/mysqladmin /usr/sbin/mysqladmin

ln -s /usr/local/mysql/support-files/mysql.server /etc/rc.d/init.d/mysql




#### Mysql 구동 설정하기
chkconfig --add mysql

chkconfig --level 24 mysql off

chmod -R 755 /usr/local/mysql/data


chkconfig / 서비스 관리 명령어, 자동실행등록)
chmod / 권한부여

Mysql 실행 방법1

service mysql start

> 실행할 때 에러남

Mysql 실행 방법2

cd /usr/local/mysql/support-files/

./mysql.server start


Mysql root 계정 비밀번호 변경
cd /usr/local/mysql/bin
./mysqladmin -u root password root[2023-03-06]
: 비밀번호 : root
초기 비밀번호 설정 이후 아래와 같은 명령어로 접근하면 된다.
mysql -u root -p해당명령어로 접근 하면 된다.
- 패스워드 노출 경고 
- using a password on the command line interface can be insecure. 
- 경고창이 떠서 그냥 mysql -u root -p 로 넘어감.


Mysql데이터베이스 및 테이블 생성
show databases;
: 데이터베이스 테이블 확인
 
mysql> create database gjj;

Query OK, 1 row affected (0.00 sec)

데이터베이스 확인

mysql> show databases;

데이터베이스 선택

mysql> use gjj;

Database changed

테이블생성

mysql> create table test(no int,name varchar(20));

Query OK, 0 rows affected (0.01 sec)

테이블확인

mysql> show tables;

1 row in set (0.00 sec)

테이블에 데이터입력

mysql> insert into test (no,name) values (1,'test');

Query OK, 1 row affected (0.00 sec)

테이블 데이터 확인

mysql> select * from test;

       	 no  	 name
         
       	 1    	 test
         
 
Mysql나가기

exit;
 
 
Mysql 시작 종료

/usr/local/mysql/bin

service mysql start

service mysql stop

#### postgresql
필수 유틸 설치

yum -ay install compat-readline43 readline-devel crypto-utils.* openssl* readline-devel pam-devel
> yum -a install compat-readline43 readline-devel crypto-utils.* openssl* readline-devel pam-devel
> 
> ay 오타같음. 
> 
> 이렇게 진행 시 unable to find a match compat-readline43 crypto-utils.* 에러 남.

그냥 진행해보도록 함.

#### Pgsql 소스파일 다운로드 및 업데이트
cd /usr/local/src

wget http://ftp.postgresql.org/pub/source/v9.3.2/postgresql-9.3.2.tar.gz

tar zvf postgresql-9.3.2.tar.gz 
> xvf를 잘못쓴거 같기는 한데 진행했더니 오류 나서 밑에걸로 진행

위에꺼 오류나면 // tar -xzvf postgresql-9.3.2.tar.gz
> -xzvf 명령어 뭔지 공부

cd postgresql-9.3.2

#### Pgsql 소스 컴파일 및 설치
./configure --prefix=/usr/local/pgsql --without-readline

gmake

gmake install

#### 유저 추가권한 부여
useradd postgres

chown -R postgres:postgres /usr/local/pgsql

#### DB 초기화 및 서l비스 등록
su - postgres
-> [root@localhost ~]# 에서 [postgres@localhost ~]$ 으로 변경 됨.

/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data

/usr/local/pgsql/bin/pg_ctl start -D /usr/local/pgsql/data

```
LOG: database system is ready to accept connections
LOG: autovacuum launcher started
라고 뜬다.
```

#### Postgre 데이터베이스 및 테이블 수정
cd /usr/local/pgsql/bin

./psql

1. 사용자 추가
postgres =# CREATE USER root WITH PASSWORD ‘root’;

CREATE ROLE

2. 사용자 조회
select * from pg_shadow;

3. 데이터베이스 생성

create database pggjj;

나가기

\q

4. 테이블생성

./psql -U root pggjj 
- ( ./psql –U (유저명) (데이터베이스명))

pggjj=> create table test(no integer, name varchar(20));

pggjj=>insert into test(no,name) values (3,'postgrestest');

pggjj=> select * from test;

       	no   	name
        
       	3     	test
        
       	(1 row)
        
pggjj=>\q







---이어서 작성 필요---
