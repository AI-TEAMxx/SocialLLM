from openai import OpenAI
import httpx
client = OpenAI(base_url="https://svip.xty.app/v1", api_key="ASSIGNED KEY",            
        http_client=httpx.Client(
        base_url="https://svip.xty.app/v1",
        follow_redirects=True,
    ))
response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Please introduce yourself in twenty words."}
    ]
)
print(response)
print(response.choices[0].message.content)