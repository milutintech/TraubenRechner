import time
import csv
import sys
import glob
import os
#import Streamlit
import streamlit as st




#color constants
Grey100 = "#F5F5F5"
Grey200 = "#EEEEEE"
Grey300 = "#E0E0E0"
Grey400 = "#BDBDBD"
Grey500 = "#9E9E9E"
Grey600 = "#757575"
Grey700 = "#616161"
Grey800 = "#424242"
Grey900 = "#212121"

BGrey   = "#373b3e"
BAnthrazit =  "#46525a"
Red100  = "#be0000"

#variables

masse=int(1)

# --- Functions ---


# --- Main ---
st.set_page_config(page_title="TraubenRechenr", page_icon=":grapes:", layout="wide")

# --- Title ---
with st.container():
    image_column, text_column = st.columns((1, 3))
    with image_column:
        st.image(image="Obrecht-Logo-Bildwortmarke-schwarz.png", width=300)
    with text_column:
        st.header("")

    st.write("---")

# ---- Menu ----
# --- Home ---
st.title('Trauben-Rechner')
st.write("---")

st.text("")
#st.text("Ganztrauben KG")
masse = st.number_input("Gewicht eingeben (KG):",
                        placeholder="Type a number...",
                        value=None,
                        step=1)




#st.header("Resultat in: " + str(ResultatLrounded) + "L")
    
if st.button("Berechnen", type="primary"):
    # st.write("Instrument Error Status: ", st.session_state.instr1.query("*TST?"))
    
    AblaufsaftL = float((masse * 100) / 1800)
    CuveeL = float((masse * 900) / 1800)
    PresssaftL = float((masse * 300) / 1800)

    AblaufsaftLround = round(AblaufsaftL,1)
    CuveeLround = round(CuveeL,1)
    PresssaftLround = round(PresssaftL,1)

    st.header(str("PetNat - Ablaufsaft: ") + str(int(AblaufsaftLround)) + "L")
    st.header(str("BRUT - Cuvéé: ") + str(int(CuveeLround)) + "L")
    st.header(str("PetNat - Presssaft: ") + str(int(PresssaftLround)) + "L")
    
