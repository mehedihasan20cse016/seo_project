Community Question Answering System
## Description
A system to provide relevant answers to user queries by combining data from Stack Overflow and Kaggle.
## Features
- Scrape latest questions from Stack Overflow.
- Combine multiple datasets.
- Provide top 10 most relevant answers using `sentence-transformers`.
## Setup
1. Clone the repository.
2. Install dependencies:
3. Run the scripts in order:
- `scrape_stackoverflow.py`
- `combine_datasets.py`
- `app.py`
4. Access the app at [http://localhost:8501](http://localhost:8501).


## Future Work
- Scrape real answers from Stack Overflow.
- Enhance the relevance model.
