import os
import streamlit as st
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.parse


@st.cache_resource
def load_models():
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    gpt_model_name = "gpt2"  # Use "distilgpt2" for a smaller version
    models_folder = "models/"

    if not os.path.exists(models_folder):
        os.makedirs(models_folder)

    embedding_model = SentenceTransformer(embedding_model_name)
    gpt_model = pipeline("text-generation", model=gpt_model_name, tokenizer=gpt_model_name)

    return embedding_model, gpt_model


@st.cache_data
def load_dataset():
    dataset_path = "data/combined_dataset.csv"
    if not os.path.exists(dataset_path):
        st.error(f"Dataset not found at {dataset_path}. Please check your dataset path.")
        return pd.DataFrame(columns=["question", "answer", "topic"])

    return pd.read_csv(dataset_path)


def scrape_web(query):
    """Scrapes web for a concise answer using DuckDuckGo search."""
    search_url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("a", class_="result__a")

            if results:
                # Extract text and URL of the first result
                first_result = results[0]
                title = first_result.text
                relative_link = first_result["href"]

                # Decode the actual target URL from DuckDuckGo link
                parsed_url = urllib.parse.urlparse(relative_link)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                actual_url = query_params.get("uddg", [None])[0]

                if actual_url:
                    # Fetch the content of the actual target URL
                    page_response = requests.get(actual_url, headers=headers, timeout=10)
                    if page_response.status_code == 200:
                        page_soup = BeautifulSoup(page_response.text, "html.parser")
                        paragraphs = page_soup.find_all("p")
                        if paragraphs:
                            # Combine text from the first few paragraphs for context
                            answer = " ".join(p.text for p in paragraphs[:2])
                            return f"{answer.strip()} (Source: {actual_url})"
                    return f"No detailed content found. (Source: {actual_url})"

        return "No relevant information found online."
    except Exception as e:
        return f"Error during web scraping: {e}"




def main():
    st.title("Community Question Answering System")
    st.subheader("Provide relevant answers to user queries.")

    embedding_model, gpt_model = load_models()
    df = load_dataset()

    user_query = st.text_input("Enter your question:")
    if user_query:
        # Generate embeddings for the user query
        query_embedding = embedding_model.encode(user_query, convert_to_tensor=True)

        # Direct answer generation using GPT
        st.write("### Answer to Your Question:")
        generated_answer = gpt_model(user_query, max_length=50, num_return_sequences=1)[0]["generated_text"]
        st.write(f"**Generated Answer**: {generated_answer}")

        # Find related questions from the dataset
        if not df.empty:
            dataset_embeddings = embedding_model.encode(df["question"].tolist(), convert_to_tensor=True)
            similarities = util.cos_sim(query_embedding, dataset_embeddings)[0]

            # Apply a similarity threshold for relevance
            threshold = 0.7
            relevant_indices = [i for i, score in enumerate(similarities) if score > threshold]
            if relevant_indices:
                st.write("### Related Questions and Answers:")
                for idx in relevant_indices:
                    st.write(f"**Question**: {df.iloc[idx]['question']}")
                    st.write(f"**Answer**: {df.iloc[idx]['answer'] or 'Answer not available'}")
                    st.write(f"**Topic**: {df.iloc[idx]['topic']}")
                    st.write("---")
            else:
                st.write("No highly relevant questions found in the dataset.")
        else:
            st.write("The dataset is empty. Unable to find related questions.")

        # Web scraping fallback for topic-related data
        st.write("### Web Scraped Information:")
        scraped_info = scrape_web(user_query)
        st.write(scraped_info)


if __name__ == "__main__":
    main()
