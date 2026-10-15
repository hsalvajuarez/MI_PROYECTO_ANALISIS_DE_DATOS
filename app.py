import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Cargar los datos
df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)


# df
# Limpiar los nombres de las columnas
df.columns = [c.lower().replace(' ', '_') for c in df.columns]

# Mostrar datos estadisticos
st.dataframe(df.describe()) 

# Desplegar una imagen en streamlit
fig, ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.pyplot(fig)