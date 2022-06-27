# st.progress

`st.progress` affiche une barre de progression qui se met à jour graphiquement au fur et à mesure que l'itération progresse.

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

##Code
Voici comment utiliser `st.progress` :

```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une application Streamlit est d'importer la bibliothèque `streamlit` as `st` et la bibliothèque `time` comme ceci :

```python
import streamlit as st
import time
```

Ensuite, nous créons un titre pour l'application :
```python
st.title('st.progress')
```

Une `About this app` box est créée à l'aide de `st.expander` et la description est affichée via `st.write` :

```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

Enfin, nous définissons une barre de progression et l'instancions avec une valeur de départ de "0".

Ensuite, une boucle `for` itérera de `0` jusqu'à ce que `100` soit atteint. À chaque itération, nous utilisons `time.sleep(0.05)` pour permettre à l'application d'attendre `0.05` secondes avant d'ajouter une valeur de `1` à la barre de progression `my_bar` et, ce faisant, l'affichage graphique de la barre augmente à chaque itération.

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Lectures complémentaires
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)