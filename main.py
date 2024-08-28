import streamlit as st
import api

st.header("Informationen")

try:
    desired_pok = st.text_input("Über welches Pokemon möchtest du Informationen erhalten?")
    info = api.get_poke_info(desired_pok.lower())
    abilities = api.get_abilities(info)
    measures = api.get_measures(info)
    image = api.get_image(info)
    st.image(image, f'Name des Pokemons: {desired_pok}')
    st.subheader("Fähigkeiten:")
    count = 1
    for element in abilities:
        st.write(f'{count}: {element}')
        count += 1
    st.subheader("Eigenschaften:")
    st.write(f'Gewicht: {measures[0]}')
    st.write(f'Größe: {measures[1]}')
except:
    st.write("Bitte gültiges Pokemon eingeben!")