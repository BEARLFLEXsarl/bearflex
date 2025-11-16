# WSGI config for PythonAnywhere

import os
import sys

# Ajouter le répertoire de votre projet au chemin Python
path = '/home/yourusername/bearflex'  # À remplacer par votre nom d'utilisateur
if path not in sys.path:
    sys.path.append(path)

# Configuration de l'environnement Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'daouda.settings'

# Import de l'application WSGI
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())