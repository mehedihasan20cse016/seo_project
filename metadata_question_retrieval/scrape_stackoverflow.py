import requests
import pandas as pd

def scrape_stackoverflow():
    # Simulate scraping questions
    data = [
        {"question": "What is AI?", "answer": "AI is the simulation of human intelligence in machines.", "topic": "Technology"},
        {"question": "How to bake a cake?", "answer": "Mix ingredients, bake for 30-40 minutes.", "topic": "Cooking"},
    ]
    df = pd.DataFrame(data)
    df.to_csv("data/stackoverflow_data.csv", index=False)
    print("Sample data scraped and saved to data/stackoverflow_data.csv")

if __name__ == "__main__":
    scrape_stackoverflow()
