import pymysql 
from django.contrib import admin

pymysql.install_as_MySQLdb()
admin.site.site_header = 'Django-ERP'
admin.site.site_title = 'ERP'