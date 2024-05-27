
import streamlit as st
import os
import tempfile
from main import *

# Predefined list of keywords
keywords = director_words  # Replace with your actual keywords

# Streamlit app
st.title('Directorate Checker App')

# File uploader allows user to upload multiple files of any format
uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)

# # Button to delete all files
# if st.button('Delete All Files'):
#     # Clear the file uploader cache
#     st.experimental_rerun()

documents_with_keywords = []      
if uploaded_files:
    with tempfile.TemporaryDirectory() as temp_dir:
        for index, uploaded_file in enumerate(uploaded_files, start=1):
            # Save the uploaded file locally in a temporary directory
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Check for keywords in the document
            message, found_keywords = check_keywords_in_document(file_path, keywords)
            
            if found_keywords:
                # Add the file name to the list of documents with keywords
                documents_with_keywords.append(uploaded_file.name)
                # Use markdown to display file name with numbering in bright color
                st.markdown(f"<span style='color: #FF5733'>{index}. FILE NAME:</span> {uploaded_file.name}", unsafe_allow_html=True)
                # Display keywords found in bright color
                st.markdown(f"<span style='color: #33FF57'>Keyword Found:</span>  {', '.join(found_keywords)}", unsafe_allow_html=True)
                st.markdown(f"<span style='color: #33FF57'> ----------------------------------------</span>  ", unsafe_allow_html=True)

# Display the list of documents with keywords in the sidebar
if documents_with_keywords:
    st.sidebar.title("Documents with Keywords")
    for index, doc in enumerate(documents_with_keywords, start=1):
        st.sidebar.text(f"{index}. {doc}")


