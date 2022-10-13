import streamlit as st
import pandas as pd
import os
import os

import pandas as pd
import streamlit as st


def main():
    st.markdown("<h5 style='text-align: center; color: black;'>🔅Make Change in Your Data🔅</h5>",
                unsafe_allow_html=True)
    st.write("\n")
    # Load the uploaded data
    if 'iris.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        data = pd.read_csv('data/iris.csv')
        st.dataframe(data)
        # Read the column meta data for this dataset 
        col_metadata = pd.read_csv('data/metadata/ctd.csv')
        st.markdown("<h5 style='text-align: center; color: black;'>*️⃣ Update Data Field Section *️⃣ </h5>",
                    unsafe_allow_html=True)

    # Use two column technique
    col1, col2 = st.columns(2)
    global name, type

    # Design column 1
    name = col1.selectbox(f"""
   🔵Select Field for Update Datatype:""",
                          data.columns)
    # Design column two
    current_type = col_metadata[col_metadata['column_name'] == name]['type'].values[0]
    column_options = ('numerical', 'categorical', 'object')
    current_index = column_options.index(current_type)
    type = col2.selectbox("🔵Select Data Type:", options=column_options, index=current_index)
    with st.expander("For instruction expand, please:"):
        st.write("""
            In order to update data type of existing filed, please follow the Click me to Update->. 
        """)
    if st.button("▶️Click me to Update->"):
        # Set the value in the metadata and resave the file
        col_metadata = pd.read_csv('data/metadata/ctd.csv')
        st.dataframe(col_metadata[col_metadata['column_name'] == name])
        col_metadata.loc[col_metadata['column_name'] == name, 'type'] = type
        col_metadata.to_csv('data/metadata/column_type_desc.csv', index=False)
        st.write("☑️Your Field Datatype Changed Successfully as Follows!")
        st.dataframe(col_metadata[col_metadata['column_name'] == name])
