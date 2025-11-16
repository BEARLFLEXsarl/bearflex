# Guide de Déploiement - MIROC sur PythonAnywhere avec domaine mirocbf.com

## 📋 LISTE DES FICHIERS CRÉÉS/MODIFIÉS

✅ `.env` - Variables d'environnement
✅ `daouda/settings.py` - Configuration mise à jour
✅ `daouda/settings_production.py` - Configuration production
✅ `daouda/wsgi_pythonanywhere.py` - Configuration WSGI
✅ `requirements_pythonanywhere.txt` - Dépendances pour PA

## 🔑 INFORMATIONS IMPORTANTES À RETENIR

- **Nom du projet**: bearflex
- **Application**: app (formulaire de contact MIROC)
- **Domaine**: mirocbf.com
- **Framework**: Django 5.1.2
- **Type de site**: Vitrine d'équipements industriels

## ⚠️ POINTS D'ATTENTION SÉCURITE

1. Changer la SECRET_KEY en production
2. Configurer les vraies variables d'environnement
3. Sécuriser les credentials email
4. Vérifier les ALLOWED_HOSTS