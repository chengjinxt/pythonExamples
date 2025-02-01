from openai import OpenAI
import os

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-max-2025-01-25",
    messages=[
      {'role': 'system', 'content': 'You are a helpful assistant.'},
      {'role': 'user', 'content': 'Which number is larger, 9.11 or 9.8?'}
    ]
)

print(completion.choices[0].message)