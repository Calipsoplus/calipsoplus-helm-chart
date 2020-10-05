from calipsoplus.settings import *
import os

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['calipsoplus.desy.de', 
                 'backend.calipsoplus.svc.cluster.local', 
                 'backend.calipsoplus.svc',
                 'backend.calipsoplus',
                 'backend',
                 'frontend.calipsoplus.svc.cluster.local',
                 'frontend.calipsoplus.svc',
                 'frontend.calipsoplus',
                 'frontend',
]

CORS_ORIGIN_WHITELIST = [
	 'calipsoplus.desy.de',
	 'frontend.calipsoplus.svc.cluster.local',
	 'backend.calipsoplus.svc.cluster.local',
	 'proxy.calipsoplus.svc.cluster.local',
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.desy\.de$",
]

CSRF_TRUSTED_ORIGINS = [ '.desy.de' ]

DJANGO_ENV = 'KUBERNETES'

os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'

# docker location
DOCKER_URL_DAEMON = os.environ["DOCKER_URL_DAEMON"]
REMOTE_MACHINE_IP = os.environ["REMOTE_MACHINE_IP"]

# Port of mocklogin
MOCKLOGIN_PORT = os.environ["MOCKLOGIN_PORT"]

# OIDC callback URL
OIDC_AUTHENTICATION_CALLBACK_URL = os.environ["OIDC_AUTHENTICATION_CALLBACK_URL"]

# logs
LOGGING['loggers']['django']['handlers'] = ['console']
LOGGING['loggers']['django_cron']['handlers'] = ['console']
LOGGING['loggers']['apprest']['handlers'] = ['console']

# backend
BACKEND_CALIPSO = "/services"

# frontend
FRONTEND_CALIPSO = "/"

# umbrella_logout
UMBRELLA_LOGOUT = BACKEND_CALIPSO + "/Shibboleth.sso/Logout?return=" + FRONTEND_CALIPSO

# umbrella_login
UMBRELLA_LOGIN = BACKEND_CALIPSO + "/Shibboleth.sso/Login?target=" + BACKEND_CALIPSO + "/calipsoplus-services/umbrella/frontend/"

# User Office backend API login
BACKEND_UO_LOGIN = f"http://mocklogin:{MOCKLOGIN_PORT}/login/"
BACKEND_UO_HASH = f"http://mocklogin:{MOCKLOGIN_PORT}/login/umbrella/"
BACKEND_UO_IS_AUTHORIZED = f"http://mocklogin:{MOCKLOGIN_PORT}/is_staff/"

# which indicates the REST endpoint to be connected against, if the DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL flag is set to 1.
# Note: endpoint should contain: login, number of items (pagination), offset (from and to), and keyword (optional)
DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL_ENDPOINT = f"http://mocklogin:{MOCKLOGIN_PORT}/experiments/$USERNAME/"

#database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'read_default_file': os.path.join('/secret', 'default.cnf'),
        }
    },
    'guacamole': {
        'ENGINE': 'django.db.backends.mysql',
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'read_default_file': os.path.join('/secret', 'guacamole.cnf'),
        },
    },
}

# List of additional group names and/or IDs that the container process will run as.
GROUPS_DOCKER_ADD = []
