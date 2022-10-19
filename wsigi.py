#from wsgiref.util import application_uri
from wsgiref.util import application_uri
from whitenoise import DjangoWhiteNoise

application = DjangoWhiteNoise(application_uri)