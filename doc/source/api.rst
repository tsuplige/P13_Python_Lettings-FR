Description des Interfaces de Programmation
=======================================


*Lettings*

*Vue `letting(request, letting_id)`*

La vue `letting` est utilisée pour afficher les détails d'une location spécifique en fonction de son ID.

```
**Vue `letting(request, letting_id)`**

Cette vue prend deux arguments :
- `request` : La requête HTTP.
- `letting_id` (int) : L'ID de la location à charger.

Elle retourne le template `lettings/letting.html` avec les données correspondant à l'objet `Letting`.

Elle utilise la méthode `get_object_or_404()` pour récupérer l'objet `Letting` en fonction de son ID, puis construit un contexte contenant le titre et l'adresse de la location avant de rendre le template.
```

 **Profiles**

*Vue `profile(request, username)`*

La vue `profile` est utilisée pour afficher les détails d'un profil utilisateur spécifique en fonction de son nom d'utilisateur.

```
**Vue `profile(request, username)`**

Cette vue prend deux arguments :
- `request` : La requête HTTP.
- `username` (str) : Le nom d'utilisateur du profil à charger.

Elle retourne le template `profiles/profile.html` avec les données correspondant à l'objet `Profile`.

Elle utilise la méthode `get_object_or_404()` pour récupérer l'objet `Profile` en fonction du nom d'utilisateur, puis construit un contexte contenant le profil avant de rendre le template.
```

#### Index

*Vue `index(request)`*

La vue `index` est utilisée pour accéder à la page d'index du site.

```
**Vue `index(request)`**

Cette vue prend un seul argument :
- `request` : La requête HTTP.

Elle retourne le template `index.html`.
```

#### Endpoints API

##### Endpoint `letting/<int:letting_id>/`

L'endpoint `letting/<int:letting_id>/` permet d'accéder aux détails d'une location spécifique via une requête HTTP GET. Il renvoie les données au format JSON.

##### Endpoint `profile/<str:username>/`

L'endpoint `profile/<str:username>/` permet d'accéder aux détails d'un profil utilisateur spécifique via une requête HTTP GET. Il renvoie les données au format JSON.
