import streamlit as st
import numpy as np
import pandas as pd
from forms import utils


# @st.cache
def main():
    with st.expander("Acknowledgement Note:"):
        st.write(f"""
            User-friendly interfaces have developed as part of the interviewing process for machine learning skills. 
            Prof. Hasan Jamil, Ph.D., a world-renowned expert in his field, advises me as I design these interfaces. 
            This prototype is just getting started. 
            We think that this technology will reach its full potential in a fairly short amount of time.
        """)

    # Upload the dataset and save as csv
    st.markdown("<h4 style='text-align: center; color: black;'>🗄 Data Source Upload Section:</h4>",
                unsafe_allow_html=True)
    st.write("\n")
    #st.markdown("At First Browse Your Dataset, Then Click Load Data:", unsafe_allow_html=True)
    # Code to read a single file
    up_file = st.file_uploader(f"🔵Choose a file ℹ️ Browse Your File, Then Click Load Data", type=['csv', 'xlsx'])
    global data
    if up_file is not None:
        try:
            data = pd.read_csv(up_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(up_file)
    if st.button("💾Load Data"):
        # Raw data
        st.dataframe(data)
        data.to_csv('data/iris.csv', index=False)
        numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = list(set(list(data.columns)) - set(numeric_cols))
        # Save the columns as a dataframe or dictionary
        columns = []
        # Iterate through the numerical and categorical columns and save in columns
        columns = utils.genMetaData(data)
        columns_df = pd.DataFrame(columns, columns=['column_name', 'type'])
        columns_df.to_csv('data/metadata/ctd.csv', index=False)
        # Display columns
        st.markdown(f"▶️Column Name◀️---▶️Type◀️")
        for i in range(columns_df.shape[0]):
            st.write(f"🔸{i + 1}. **{columns_df.iloc[i]['column_name']}** ➡️ {columns_df.iloc[i]['type']}")
        with st.expander("For instruction expand, please:"):
            st.write("""
                All field names with their data-types are shown here. Is there required to update data-type?
                To make any correction, please go to change metadata option.   
                . 
            """)
