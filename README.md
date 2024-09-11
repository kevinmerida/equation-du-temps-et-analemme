# Equation du temps et analemme

## Description

La mesure du temps est effectuée de nos jours par des **horloges atomiques** avec une **extrême précision**. Une autre référence de temps est donnée par **la vitesse de rotation de la Terre sur elle-même** , qui est relativement stable.

Cette vitesse n’est cependant pas rigoureusement constante, car il faut parfois insérer une seconde au temps UTC (celui de nos montres) pour que la durée du **jour solaire moyen** reste égale à … 24h ! La diminution **très lente** de cette vitesse en est notamment la cause.

Mais considérons-là constante pour définir le **temps solaire moyen**. Il correspond à un "Soleil moyen" qui aurait une **orbite circulaire** à vitesse constante, de même période que l’orbite elliptique du "Soleil vrai" autour de la Terre, mais cette fois dans le plan équatorial.

Il s’agit juste d’avoir une référence de temps avec des jours qui durent tous 24h. Mais la Terre a une **orbite elliptique** et son axe de rotation est incliné par rapport au plan de l’écliptique. Ce qu’on appelle alors **le temps solaire vrai** sera alors un peu différent …

On se propose d'évaluer ici **l'équation du temps** qui est la différence entre le **temps solaire moyen** et le **temps solaire vrai**. Il sera ensuite possible de représenter la position du "Soleil vrai" dans le ciel, donc **l'analemme** au midi solaire moyen.

Différentes configurations sont testées :
* orbite vraie
* orbite circulaire et inclinaison non nulle
* orbite elliptique et inclinaison nulle

## Calculs

On se place dans le [référentiel géocentrique](https://media4.obspm.fr/public/ressources_lu/pages_reperes/referentiel-apprendre.html), avec un repère $OXYZ$ ($OX$ axe dirigé vers le [point vernal](https://acces.ens-lyon.fr/acces/thematiques/paleo/variations/tp-milankovitch/point_vernal), $OXY$ plan équatorial, $OZ$ axe de rotation de la Terre).

Dans ce repère $OXYZ$, on considère un autre repère $OXyz$, où $OXy$ est [l'écliptique](https://fr.wikipedia.org/wiki/%C3%89cliptique), incliné d'un angle $\epsilon$. Dans le plan de l'équateur $OXY$ et l'écliptique $OXy$, la référence commune pour les angles sera donc l'axe $OX$.

Dans le plan $OXy$, le "Soleil vrai" a une longitude écliptique

$$\lambda_V=W+V$$

où $W$ est la longitude écliptique du Soleil au périhélie et $V$ est [l'anomalie vraie](https://fr.wikipedia.org/wiki/Anomalie_vraie).

Dans le plan $OXY$, le "Soleil moyen" a une "longitude équatoriale" (le terme plus approprié serait plutôt ascension droite)

$$\lambda_M=W+M$$

où $M$ est cette fois [l'anomalie moyenne](https://fr.wikipedia.org/wiki/Anomalie_moyenne), proportionnelle au temps.

L'anomalie moyenne $M$ permet d'obtenir l'anomalie vraie $V$ grâce à la résolution de [l'équation de Képler](https://www.youtube.com/watch?v=QbxsBTaJXW0).

Dans le repère $OXyz$, le vecteur unitaire qui pointe vers le "Soleil vrai" est

$$\vec d_V=[\cos(\lambda_V),\sin(\lambda_V),0]$$

Dans le repère $OXYZ$, le vecteur unitaire qui pointe vers le "Soleil moyen" est

$$\vec d_M=[\cos(\lambda_M),\sin(\lambda_M),0]$$

Exprimons les coordonnées du vecteur $\vec d_V$ dans le repère $OXYZ$. On obtient

$$\vec d_V=[\cos(\lambda_V),\cos(\epsilon)\sin(\lambda_V),\sin(\epsilon)\sin(\lambda_V)]$$

Si on veut les coordonnées angulaires classiques de ce vecteur, avec une ascension droite $\lambda_V^\prime$ et une déclinaison $\delta$, il faut considérer son autre expression

$$\vec d_V=[\cos(\delta)\cos(\lambda_V^\prime),\cos(\delta)\sin(\lambda_V^\prime),\sin(\delta)]$$

On en déduit que $\sin(\delta)=\sin(\epsilon)\sin(\lambda_V)$, ce qui nous permet d'accéder à la valeur de $\delta$.

Ce qui nous intéresse maintenant est l'écart d'angle $\Delta\lambda$ entre les ascensions droites du "Soleil moyen" et du "Soleil vrai". Il faut donc se placer dans le plan $OXY$ et donc considérer un vecteur $\vec d_V^\prime$ qui sera la projection du vecteur $\vec d_V$ sur ce plan.

$$\vec d_M=[\cos(\lambda_M),\sin(\lambda_M),0]$$

$$\vec d_V^\prime=[\cos(\lambda_V),\cos(\epsilon)\sin(\lambda_V),0]$$

Une astuce pour éviter les calculs d'arctangente consiste à calculer le produit vectoriel
$$\vec d_M \wedge \vec d_V^\prime=[0,0,\cos(\lambda_M)\sin(\lambda_V)\cos(\epsilon)-\sin(\lambda_M)\cos(\lambda_V)]=[0,0,\lVert \vec d_M \lVert.\lVert \vec d_V^\prime \lVert.\sin(\Delta\lambda)]$$

avec $\lVert \vec d_M \lVert=1$ et $\lVert \vec d_V^\prime \lVert=\cos(\delta)$.

Au final, on obtient **l'équation du temps** $\Delta\lambda$ en angle :

$$\delta=\arcsin\left(\sin(\epsilon)\sin(\lambda_V)\right)$$

$$\Delta\lambda=\arcsin\left(\frac{\cos(\lambda_M)\sin(\lambda_V)\cos(\epsilon)-\sin(\lambda_M)\cos(\lambda_V)}{\cos(\delta)}\right)$$

Pour obtenir l'équation du temps $\Delta T$ en minutes, il suffit de diviser $\Delta\lambda$ par la vitesse de rotation de la Terre sur elle-même qui est de 15 degrés par heure soit $\dfrac{1}{4}$ de degré par minute :

$$\Delta T=4\Delta\lambda$$

## Programmes et résultats

Le programme [**eqt_ana.py**](Code/eqt_ana.pt) contient les fonctions permettant la génération des figures ci-dessous.
Le notebook [**equation_du_temps_et_analemme.ipynb**] donne des exemples d'appels à ces fonctions.

### Equation du temps

![](Data/Figure_1.png)

### Analemme

![](Data/Figure_2.png)




