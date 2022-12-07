import streamlit as st
import pickle
import pandas as pd
import numpy as np



st.title("Client Recommendatation system")
crescendo_data=pickle.load(open("recomend_suitable_clients.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
list_of_all_clients=np.array(crescendo_data["foreign_company_name"])

a1,a2,a3,a4,a5 = st.columns(5)

a1.metric("Total Companies from Database","1580")
a2.metric("Total Casting companies","50")
a3.metric("Total Forging companies","50")
a4.metric("Intrested to have Joint venture for Vaccum Toilet System","50")
a5.metric("Intrested to have Joint venture for Smart Energy Meters ","60")
option = st.selectbox(
"Select your Dream client ",
(list_of_all_clients))


def movie_recommend(foreign_company_name):
     index = crescendo_data[crescendo_data['foreign_company_name'] == foreign_company_name].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:50]:
          l.append("{}".format(crescendo_data.iloc[i[0]].foreign_company_name,crescendo_data.iloc[i[0]].type_of_co_operation))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)

def products_recommend(foreign_company_name):
     index = crescendo_data[crescendo_data['foreign_company_name'] == foreign_company_name].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:50]:
          l.append("{}".format(crescendo_data.iloc[i[0]].product_name))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)
 
def type_of_co_operation_recommend(foreign_company_name):
     index = crescendo_data[crescendo_data['foreign_company_name'] == foreign_company_name].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:50]:
          l.append("{}".format(crescendo_data.iloc[i[0]].type_of_co_operation))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)

if st.button('Recommend Me'):
     st.write('Clients Recomended for you are:')
     # st.write(movie_recommend(option),show_url(option))
     df = pd.DataFrame({
          'Client_Recommended': movie_recommend(option),
          'Type_of_Co-operation' :type_of_co_operation_recommend(option),
          'Products_of Clients' :products_recommend(option)       
     })

     st.table(df)