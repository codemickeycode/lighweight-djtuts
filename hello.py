import sys

from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

from django.conf.urls import url
from django.http import HttpResponse

from django.db import models

#### SETTINGS
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisasecretkeysampleonly',
    ROOT_URLCONF=__name__, # __name__ refers to this file
    ALLOWED_HOSTS=('localhost',),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'hellodb',
        }
    }
)
#django built in var used to identify that your web app is WSGI compliant
application = get_wsgi_application()
#### END SETTINGS

# views.py
#### VIEWS
def index(request):
    return HttpResponse('Hello World!')
#### END VIEWS


# urls.py
#### URLS
urlpatterns = (
    url(r'^$', index), #r - raw text which will be used for regex
)
#### END URLS

#### MODELS
class ListsItems(models.Model):
    item = models.Charfield()

#### END MODELS



#boilerplate
if __name__ == '__main__':
    execute_from_command_line(sys.argv) # or [runserver]