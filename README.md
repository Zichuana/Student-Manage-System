# student-manage-system
Django-SQLServer
python=3.9
Django=2.1.15
SQLServer2019

### pip安装django链接sqlserver需要的库
```pip install django-crontab django-mssql django-pyodbc django-pyodbc-azure django-pytds django-sqlserver```
### 数据库链接更改（setting.py）
```
DATABASES = {
  'default': {
    'ENGINE': 'sql_server.pyodbc',			        # 使用odbc连接报错，尝试直接用sqlserver就成功了  # django.db.backends
    'NAME': 'XS',				            # 自定义数据库连接名
    'USER': 'sa',					                # 数据库连接账户
    'PASSWORD': '123456',				        # 数据库连接密码
    'HOST': 'DESKTOP-I36E1HE',				            # 数据库服务地址 主机名
    'PORT': '1433',					                # 数据库连接端口
    'OPTIONS': {
        'driver': 'SQL Server Native Client 11.0',	# ODBC连接应用驱动（需查看安装）
        'MARS_Connection': True,
    }
  }
}
```
### 数据库创建
```
# 终端下执行
python manage.py makemigrations
python manage.py migrate
```
### 创建admin用户
```
# 终端下执行
python manage.py createsuperuser
```
### 终端运行代码
```
python manage.py runserver
```
