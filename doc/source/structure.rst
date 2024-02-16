Structure de la Base de Données et Modèles de Données
=======================================

La base de données de Orange County Lettings est conçue avec les modèles suivants :

#### Modèles de Données Principaux

##### Address

Le modèle `Address` représente une adresse physique avec les attributs suivants :

- `number` (PositiveIntegerField) : Numéro de rue.
- `street` (CharField) : Nom de la rue.
- `city` (CharField) : Ville de l'adresse.
- `state` (CharField) : État ou province de l'adresse.
- `zip_code` (PositiveIntegerField) : Code postal.
- `country_iso_code` (CharField) : Code ISO du pays.

```rst
**Address:**

- ``number`` (PositiveIntegerField) : Numéro de rue.
- ``street`` (CharField) : Nom de la rue.
- ``city`` (CharField) : Ville de l'adresse.
- ``state`` (CharField) : État ou province de l'adresse.
- ``zip_code`` (PositiveIntegerField) : Code postal.
- ``country_iso_code`` (CharField) : Code ISO du pays.

    Méthodes :
        __str__() : Affiche une représentation textuelle de l'adresse.
```

##### Letting

Le modèle `Letting` représente une location avec les attributs suivants :

- `title` (CharField) : Titre de la location.
- `address` (OneToOneField) : Adresse associée à la location.

```rst
**Letting:**

- ``title`` (CharField) : Titre de la location.
- ``address`` (OneToOneField) : Adresse associée à la location.

    Méthodes :
        __str__() : Affiche une représentation textuelle de la location.
```

##### Profile

Le modèle `Profile` représente le profil d'un utilisateur avec les attributs suivants :

- `user` (OneToOneField) : Utilisateur associé au profil.
- `favorite_city` (CharField) : Ville préférée de l'utilisateur (optionnel).

```rst
**Profile:**

- ``user`` (OneToOneField) : Utilisateur associé au profil.
- ``favorite_city`` (CharField) : Ville préférée de l'utilisateur.

    Méthodes :
        __str__() : Affiche une représentation textuelle du profil.
```

Cette structure de base de données permet de stocker efficacement les informations relatives aux adresses, aux locations et aux profils d'utilisateurs dans Orange County Lettings.