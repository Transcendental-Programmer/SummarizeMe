import streamlit as st
from text_summarization import (
    sumy_summarizer,
    nltk_summarizer,
    spacy_summarizer,
    t5_summarizer,
    readingTime,
    get_text
)

def main():
    st.title("Text Summarization App")
    st.markdown("""
        <style>
            .summarizer-section {
                background-color: #808080;
                border-radius: 10px;
                margin-bottom: 20px;
                padding: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("Summarize your text with different summarization techniques")

    activities = ["Summarize Text", "Summarize URL"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Summarize Text":
        st.subheader("Summarize Your Text")
        raw_text = st.text_area("Enter Text Here", "Type Here")

        if st.button("Summarize"):
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>Original Text</h5>", unsafe_allow_html=True)
            st.write(raw_text)

            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)
            st.markdown("<h5>SpaCy Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with SpaCy..."):
                summary_spacy = spacy_summarizer(raw_text)
            st.markdown(f"<p>{summary_spacy}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)
            
            st.markdown("<h5>Sumy Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with Sumy..."):
                summary_sumy = sumy_summarizer(raw_text)
            st.markdown(f"<p>{summary_sumy}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>NLTK Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with NLTK..."):
                summary_nltk = nltk_summarizer(raw_text)
            st.markdown(f"<p>{summary_nltk}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>T5 Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with T5..."):
                summary_t5 = t5_summarizer(raw_text)
            st.markdown(f"<p>{summary_t5}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

    elif choice == "Summarize URL":
        st.subheader("Summarize URL")
        url = st.text_input("Enter URL", "Type Here")

        if st.button("Summarize"):
            raw_text = get_text(url)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>Original Text from URL</h5>", unsafe_allow_html=True)
            st.write(raw_text)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>SpaCy Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with SpaCy..."):
                summary_spacy = spacy_summarizer(raw_text)
            st.markdown(f"<p>{summary_spacy}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>Sumy Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with Sumy..."):
                summary_sumy = sumy_summarizer(raw_text)
            st.markdown(f"<p>{summary_sumy}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>NLTK Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with NLTK..."):
                summary_nltk = nltk_summarizer(raw_text)
            st.markdown(f"<p>{summary_nltk}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

            st.markdown("<h5>T5 Summarizer</h5>", unsafe_allow_html=True)
            with st.spinner("Summarizing with T5..."):
                summary_t5 = t5_summarizer(raw_text)
            st.markdown(f"<p>{summary_t5}</p>", unsafe_allow_html=True)
            st.markdown("<div class='summarizer-section'>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
