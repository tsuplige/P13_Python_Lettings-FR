Instructions d'Installation
=======================================

Avant de commencer l'installation, assurez-vous d'avoir Python et pip installés sur votre système. Clonez ensuite le repository GitHub du projet Orange County Lettings depuis l'URL fournie par le directeur technique, Dominique.

``git clone https://github.com/tsuplige/P13_Python_Lettings-FR``


**Installation des Dépendances**

Accédez au répertoire du projet et créez un environnement virtuel.

``cd OrangeCountyLettings
python -m venv venv``

Activez l'environnement virtuel.

- Sur Windows :

``venv\Scripts\activate
``

- Sur macOS/Linux :

``source venv/bin/activate
``

Installez les dépendances requises à l'aide de pip.

``pip install -r requirements.txt
``

 **Configuration de l'Environnement**

Créez un fichier `.env` à la racine du projet et configurez les variables d'environnement nécessaires, telles que les clés secrètes, les paramètres de base de données, etc.

``dotenv
 *Exemple de configuration .env*
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url``

 **Lancement du Serveur de Développement**

Appliquez les migrations pour créer la structure de la base de données.

``python manage.py migrate
``

Démarrez le serveur de développement.

``python manage.py runserver
``

Accédez à l'adresse `http://localhost:8000` dans votre navigateur pour accéder au site Orange County Lettings en mode local.

Ces instructions devraient vous permettre de mettre en place et de faire fonctionner le site en local sur votre ordinateur, comme demandé par Dominique.