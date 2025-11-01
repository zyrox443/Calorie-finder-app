import streamlit as st
import requests

# 🔑 Groq API key
GROQ_API_KEY = "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"

# 🧠 Function to get LLM response
def get_calories_from_llm(food):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a calorie expert AI that always responds in one single short line like: 'Apple has 120 calories.'"},
            {"role": "user", "content": f"How many calories are in {food}?"}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# 🎨 Streamlit UI
st.set_page_config(page_title="Zain's Calorie Bot 🍎", page_icon="🍎", layout="centered")

st.title("🍎 ZainGPT Calorie Teller")
st.write("Ask me the calories of any food — ")

food = st.text_input("Enter a food item (e.g., apple, pizza, burger):")

if st.button("Tell Calories"):
    if not food.strip():
        st.warning("Please enter a food item.")
    else:
        with st.spinner("Thinking..."):
            result = get_calories_from_llm(food)
            st.success(result)
