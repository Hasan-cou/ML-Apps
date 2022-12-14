"""
Purpose:connect manager for page to page link
"""

import streamlit as st


class MP:

    # @st.cache()
    def __init__(self) -> None:
        self.forms = []

    def connect(self, title, func) -> None:
        self.forms.append(
            {
                "title": title,
                "function": func
            }
        )

    def start(self):

        st.sidebar.image('Logo.png')
        page = st.sidebar.selectbox(
            '💎 System Navigation here⤵️::💎',
            self.forms,
            format_func=lambda form: form['title']
        )
        page['function']()
