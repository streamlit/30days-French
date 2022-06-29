# st.button

`st.button` permet l'affichage d'un bouton.

## Que construisons nous ?

Une application simple qui imprime des messages différents selon que le bouton ait été pressé ou non.

Déroulement de l'application :

1. Par défaut, l'application imprime "Goodbye"
2. En cliquant sur le bouton, l'application affiche le message alternatif "Why Hello?"

## Application de démonstration

L'application Streamlit déployée devrait ressembler à celle illustrée dans le lien ci-dessous :

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Code

Voici le code pour implémenter l'application mentionnée ci-dessus :

```python
import streamlit as st

st.header('st.button')

if st.button('say hello'):
     st.write('why hello?')
autre:
     st.write('goodbye')
```

## Explication ligne par ligne

La première chose à faire lors de la création d'une application Streamlit est d'importer la bibliothèque `streamlit` via `st`, comme ceci :

```python
import streamlit as st
```

Continuons avec la création d'un titre pour l'application :

```python
st.header('st.button')
```

Ensuite, nous utiliserons les instructions conditionnelles `if` et `else` pour afficher différent messages:

```python
if st.button('say hello'):
     st.write('why hello?')
autre:
     st.write('goodbye')
```

Comme nous pouvons le voir dans le code ci-dessus, la commande `st.button()` accepte l'argument d'entrée `say hello`, qui est le texte affiché par le bouton.

La commande `st.write` est utilisée pour imprimer des messages texte de type `why hello?` ou `goodbye` selon que le bouton ait été cliqué ou non, implémenté via :


```python
st.write('why hello there')
```

et

```python
st.write('goodbye')
```

Il est important de noter que les instructions `st.write` ci-dessus sont placées sous les conditions `if` et `else` afin d'effectuer le processus mentionné ci-dessus d'affichage alternatif des messages.

## Prochaines étapes

Maintenant que vous avez créé l'application Streamlit localement, il est temps de la déployer sur [Streamlit Cloud](https://streamlit.io/cloud) comme cela sera expliqué dans un prochain défi.

Comme il s'agit de la première semaine de votre défi, nous fournissons le code complet (comme indiqué dans la zone de code ci-dessus) et la solution (l'application de démonstration) directement sur cette page Web.

Pour avancer dans les prochains défis, il est recommandé d'essayer d'abord d'implémenter l'application Streamlit vous-même.

Ne vous inquiétez pas si vous êtes bloqué, vous pouvez toujours jeter un coup d'œil à la solution !

## Références

Vous souhaitez en savoir plus? Vous pouvez consulter la documentation de [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) dans la documentation de l'API Streamlit.