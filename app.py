import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1ZOXyMPZ29xT_Ycb0mx8CJSiPLby6WutJZAGDD-iSJ-o/export?format=xlsx&id=1ZOXyMPZ29xT_Ycb0mx8CJSiPLby6WutJZAGDD-iSJ-o'

df=pd.read_excel(url, sheet_name='Original')


def main():

    st.title("Curso StremLit")
    st.dataframe(df)
    



if __name__ == '__main__':  #para q se ejecute la funcion solo si estoy en este archivo

    main()


