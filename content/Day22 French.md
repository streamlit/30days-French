# st.form

`st.form` crée un formulaire qui regroupe les éléments avec un bouton "Submit".

En règle générale, chaque fois qu'un utilisateur interagit avec un widget, l'application Streamlit est réexécutée Un formulaire est un conteneur qui regroupe d'autres éléments et widgets et un bouton "Submit". Un utilisateur peut donc interagir avec un ou plusieurs widgets autant de fois qu'il le souhaite sans provoquer de réexécution du code. Lorsque le bouton "Submit" du formulaire est pressé, toutes les valeurs de widget à l'intérieur du formulaire seront envoyées à Streamlit en une seule fois.

Les formulaires ont toutefois quelques contraintes :

- Chaque formulaire doit contenir un `st.form_submit_button`.
- `st.button` et `st.download_button` ne peuvent pas être ajoutés à un formulaire.
- Les formulaires peuvent apparaître n'importe où dans votre application (barre latérale, colonnes, etc.), mais ils ne peuvent pas être intégrés à d'autres formulaires.

Pour plus d'informations sur les formulaires, consultez notre [article](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Code
Voici comment utiliser `st.form` :

```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.write('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une application Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un titre pour l'application :
```python
st.title('st.form')
```

### Premier exemple
Dans le formulaire, nous commencerons par écrire une sous-en-tête (subheader) "Order your coffee", puis créerons plusieurs widgets de saisie (`st.selectbox`, `st.select_slider` et `st.checkbox`) pour collecter des informations sur la commande de café. Enfin, un bouton "Submit" est créé via la commande `st.form_submit_button`, qui, une fois cliqué, enverra toutes les données entrées par l'utilisateur a l'application.

```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

Une fois cliqué sur le bouton 'Submit', il est temps d'ajouter un peu de *logique*!

Par défaut, chaque fois que l'application Streamlit démarre, l'instruction `else` sera exécutée et nous verrons un message `☝️ Place your order!`. Alors qu'en cliquant sur le bouton d'envoi (`Submit`), toutes les entrées fournies par l'utilisateur via les différents widgets sont stockées dans plusieurs variables (par exemple, `coffee_bean_val`, `coffee_roast_val`, etc.) et imprimées via la commande `st.markdown` à l'aide d'un f-string, comme suit:

```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### Deuxième exemple
Passons maintenant au deuxième exemple sur l'utilisation de `st.form` comme notation d'objet. Ici, la commande `st.form` est assignée à la variable `form`. Par la suite, diverses commandes Streamlit telles que `slider` ou `form_submit_button` sont appliquées sur la variable `form`.


```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Lectures complémentaires
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Présentation du bouton Soumettre et des formulaires](https://blog.streamlit.io/introducing-submit-button-and-forms/)