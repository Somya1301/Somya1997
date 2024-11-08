import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Top Queries", page_icon="📈", layout="wide")  
st.subheader("PYTHON QUERY OPERATIONS | FETCH DATA FROM DATASET BY ADVANCED QUERY")

theme_plotly = None 

#sidebar
st.sidebar.image("data/logo1.webp")

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
# Load the Excel file into a DataFrame
file_path = 'python_query.xlsx'  
df = pd.read_excel(file_path)

with st.expander("🔷 **View Original Dataset | Excel file**"):
 st.dataframe(df,use_container_width=True)

# TASK 1: Display results using Streamlit metrics cards horizontally
# Query 1
with st.expander("**QUERY 1:** Select count **States** by Frequency"):
 state_count = df['State'].value_counts().reset_index()
 state_count.columns = ['State', 'Frequency']
 st.write("Count of States by Frequency:")
 st.dataframe(state_count,use_container_width=True)

# Bar graph for Query 2
with st.expander("**QUERY 2:** select count **State** by frequency and print in dataframe and show simple bar graph with grids and legend"):
 fig3 = px.bar(state_count, x='State', y='Frequency', labels={'x': 'State', 'y': 'Frequency'}, title='Frequency of States')
 fig3.update_layout(showlegend=True)
 fig3.update_xaxes(showgrid=True)
 fig3.update_yaxes(showgrid=True)
 st.plotly_chart(fig3,use_container_width=True)

# Query 3
with st.expander("**QUERY 3:** Select count **BusinessType** by frequency"):
 business_type_count = df['BusinessType'].value_counts().reset_index()
 business_type_count.columns = ['BusinessType', 'Frequency']
 st.write("Count of Business Types by Frequency:")
 st.dataframe(business_type_count,use_container_width=True)



# Query 4
with st.expander("**QUERY 4:** select minimal **Investment** and minimal **Rating** where **State** is Mwanza and date is range from 2-jan-21 to 16-jan-21"):
 query_5 = df[(df['State'] == 'Mwanza') & (df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16')][['Investment', 'Rating']].agg('min')
 st.success("Minimum **Investment** and **Rating** where **State** is **Mwanza** and date is in the specified range:")
 st.dataframe(query_5)


# Query 5
with st.expander("**QUERY 5:** select count **Location** where **Location** ='Dodoma'"):
 count_location = df[df['State'] == "Dodoma"]['Location'].count()
 st.info(f"## {count_location}")







# Query 6- Sum of investments in the date range at Dodoma
with st.expander("**QUERY 6:** select summation of **investment** where **Expiry** is a date range from 2-jan-21 to 16-jan-21 and region is Dodoma"):
 sum_investment_date_range_dodoma = df[(df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16') & (df['State'] == 'Dodoma')]['Investment'].sum()
 st.info(f"## {sum_investment_date_range_dodoma:,.3f}")






