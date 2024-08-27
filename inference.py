import json
import httpx
from openai import OpenAI

def load_data(file_path):
    """ Load and parse JSONL file """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def create_evaluation_prompt(data_entry):
    """ Create evaluation prompts based on the provided data entry """
    context = "\n".join([f"{turn['speaker']}: {turn['utterance']}" for turn in data_entry['dialogue']])
    character_response = data_entry['response_messages']['response']
    return f"""
### 角色设定
{data_entry['character_profile']}

### 对话
{context}

### 角色回复
{character_response}
"""

def main():
    client = OpenAI(base_url="https://svip.xty.app/v1", api_key="ASSIGNED KEY", http_client=httpx.Client(base_url="https://svip.xty.app/v1", follow_redirects=True))

    # Load data
    data = load_data("emotion_self_awareness_benchmark_data_sample.json")

    for entry in data:
        prompt = create_evaluation_prompt(entry)
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ]
        )
        print(response)
        print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
