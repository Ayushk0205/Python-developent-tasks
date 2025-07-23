import google.generativeai as genai
from serpapi import GoogleSearch

genai.configure(api_key="AIzaSyAdhfXy-BBftBaRA236fjZG6QoqqEx2yak")

model = genai.GenerativeModel('gemini-2.0-flash')

serpapi_key = "8812bcd6f5895fc4d2ad612be8ea91a9405be6011d5c0d8568fc24c0a079df57"

def google_search(query):
    param = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": serpapi_key
    }

    search = GoogleSearch(param)
    results = search.get_dict()

    if "organic_results" in results:
        return "\n".join([res["snippet"] for res in results["organic_results"][:5]])
    return "No result found."

def chat_with_gemini(query):
    search_result = google_search(query)

    prompt = f""" I searched google for "{query}" and found the following information:
    {search_result}

    Based on this, please give me a concise and to the point answer."""

    response = model.generate_content(prompt)
    return response.text

user = input("Prompt: ")
print(chat_with_gemini(user))

