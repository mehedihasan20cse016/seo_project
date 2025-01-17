import pandas as pd
import random

# Sample topics
topics = ["Technology", "Programming", "Mathematics", "Science", "Biology", "Cooking", "General Knowledge", "Technology", "Programming", "Mathematics", "Science", "Biology", "Cooking", "General Knowledge"]

# Sample questions and answers
questions_answers = [
    ("What is AI?", "AI is the simulation of human intelligence in machines."),
    ("How to bake a cake?", "To bake a cake, preheat the oven, mix ingredients, and bake for 30-40 minutes."),
    ("What is the speed of light?", "The speed of light is approximately 299,792 kilometers per second."),
    ("How does the internet work?", "The internet is a global network of interconnected computers."),
    ("What is the tallest mountain?", "Mount Everest is the tallest mountain in the world."),
    ("What is machine learning?","Machine learning is a subset of artificial intelligence where systems learn from data to improve their performance without being explicitly programmed."),
    ("How to install Python on Windows?","To install Python, download it from the official Python website and follow the installation instructions."),
    ("What is the capital of France?",  "The capital of France is Paris."),
    ("How does blockchain work?", "Blockchain is a decentralized and distributed digital ledger that records transactions across many computers."),
    ("What is the Pythagorean theorem?", "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides."),
    ("How to cook pasta?", "To cook pasta, boil water, add salt, put the pasta in, and cook for 8-12 minutes depending on the type."),
    ("What is the boiling point of water?", "The boiling point of water is 100 degrees Celsius or 212 degrees Fahrenheit at sea level."),
    ("How to set up a web server?", "To set up a web server, install server software like Apache or Nginx and configure it to serve your web pages."),
    ("What is photosynthesis?", "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water."),
    ("What is quantum computing?", "Quantum computing is a type of computation that utilizes quantum-mechanical phenomena such as superposition and entanglement.")
]

# Generate large dataset
data = []
for _ in range(14):  # Generate 1000 rows
    question, answer = random.choice(questions_answers)
    topic = random.choice(topics)
    data.append({"question": question, "answer": answer, "topic": topic})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/kaggle_dataset.csv", index=False)
print("Large dataset saved to data/kaggle_dataset.csv")


