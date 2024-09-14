import streamlit as st
from rag import Rag

# Show title and description.
st.title("📄 Hackcup Demo")

problem = st.text_input("Problem")
if not problem:
    st.info("Please add your problem to continue.", icon="❓")
else:
    # Let the user upload a file via `st.file_uploader`.
    uploaded_sample_input = st.file_uploader(
        "Upload Sample Input (.txt)", type=("txt")
    )

    uploaded_sample_output = st.file_uploader(
        "Upload Sample Output (.txt)", type=("txt")
    )

    if uploaded_sample_input and uploaded_sample_output:

        # Process the uploaded file and question.
        uploaded_sample_input_data = uploaded_sample_input.read().decode()
        uploaded_sample_output_data = uploaded_sample_output.read().decode()

        if st.button("Start", type="primary"):
            #st.write_stream("sample output")
            rag = Rag(problem, uploaded_sample_input_data, uploaded_sample_output_data)
            st.write(rag.run())

        # Stream the response to the app using `st.write_stream`.
        #st.write_stream("sample output")
