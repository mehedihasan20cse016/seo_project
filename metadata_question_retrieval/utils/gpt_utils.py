import openai

openai.api_key = "your-openai-api-key"

def generate_answer(question):
    prompt = f"Provide a detailed and accurate answer to the following question:\n\n{question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating answer: {e}"
