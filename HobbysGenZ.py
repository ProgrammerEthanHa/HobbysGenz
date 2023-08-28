import streamlit as st
import pandas as pd
import altair as alt

st.header("Was treibt die Jugend von Heute?")
st.subheader("Anteil der Befragten (Gen.Z), die folgende Hobbys haben")

source = pd.DataFrame({
        'Anteil(%)': [48, 39, 37, 36, 32, 32, 30, 26],
        'Aktivitäten': ['Soziale Kontakte pflegen', 'Sport & Fitness', 'Videospiele', 'Kochen & Backen', 'Außenaktivitäten', 'Lesen', 'Reisen', 'Technik & Computer']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Aktivitäten:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 3360 Befragte in Deutschland; Mehrfachbeantwortung möglich
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Statista Global Consumer survey")