Stuff Discussed:
------------
startproject

MTV
model
view      -- controller
template

settings
view
url

-------------

class based view VS function-based view
class-based - all the classes that you need is already incorporated, introduced since django 1.3
function-based - for simple views
manage.py - wrapper for the command execute_from_command_line
runs a webserver

typical web app, runs through WSGI

| PYTHON   | PHP  |
|-----------|------|
| apache   |   |
| django| cake, laravel, codeigniter |
| gunicorn - wsgi server | uses the mod_wsgi in apache |

gunicorn - its like an enhanced version of a webserver, wsgi compliant

nginx is good for static contents
apache for dynamic contents

Django - can still be lightweight like flask but batteries included


Creating, Setting Directory and Deactivating Virtualenv
-------------
```
mkvirtualenv --python=/usr/bin/python3.3 --no-site-packages djtuts

(djtuts)micaela@codemickeycode:~/Projects$ mkdir djtuts
(djtuts)micaela@codemickeycode:~/Projects$ cd djtuts
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ setvirtualenvproject
Setting project for djtuts to /home/micaela/Projects/djtuts
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ deactivate

micaela@codemickeycode:~/Projects/djtuts$ workon djtuts
```

Install Django
-------------
```
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ pip install --upgrade django
```

Running the Built-in Server
-----------
```
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ python hello.py runserver
```

Install Gunicorn
----------
```
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ pip install gunicorn
```

Run Gunicorn
----------
```
gunicorn hello:application --log-file=-
OR
gunicorn hello --log-file=- --bind=:127.0.0.1:8000
```

Install htop (optional)
----------
```
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ sudo apt-get install htop
```

Create DB
---------
```
(djtuts)micaela@codemickeycode:~/Projects/djtuts$ python hello.py syncdb
```
