import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from forms import utils
import seaborn as sns
import os


def main():
    if 'iris.csv' not in os.listdir('data'):
        st.markdown("Upload data")
    else:
        df_analysis = pd.read_csv('data/iris.csv')
        cols = pd.read_csv('data/metadata/ctd.csv')
        Categorical, Numerical, Object = utils.getColumnTypes(cols)
        corr = df_analysis.corr()

        fig2, ax2 = plt.subplots()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        cmap = sns.diverging_palette(240, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, linewidths=.5, cmap=cmap, center=0, ax=ax2)
        ax2.set_title("Correlation Co-efficient Matrix")
        st.pyplot(fig2)
