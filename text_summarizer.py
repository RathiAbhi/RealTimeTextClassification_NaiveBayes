"""
Uses openAI for 1000-token summaries
"""

import openai
from config import OPENAI_API_KEY

class TextSummarizer:
    def __init__(self,api_key):
        openai.api_key = api_key

    def summarize(self,text,max_tokens=1000):
        if not text:
            return ""

        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [{"role":"system","content":"Summarize in 1000 tokens"},
                        {"role":"user","content":text}],
            max_tokens = max_tokens
        )

        return response["choices"][0]["message"]["content"]