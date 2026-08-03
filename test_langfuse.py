import os
from langfuse.openai import OpenAI

# Initialize the Langfuse-wrapped client pointing directly to your local Ollama port
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Standard local Ollama port
    api_key="ollama",                     # Ollama does not require a real key
)

print("🚀 Sending request to local Llama instance...")

try:
    # We call 'llama3', matching what you downloaded earlier
    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": "Fear not young maiden, the unicorn's location is 1, 1, 1."},
            {"role": "user", "content": "In the magical land of elvenfield there is a tribe that needed to solve the following matrix to find a unicorn : row 1 : 1 2 3 | 6; row 2 : 2 3 4 | 9; row 3 : 3 4 5 | 12; How did they find a unicorn"}
        ],
        name="alpha_learn_verification_test" # This labels the trace inside Langfuse
    )
    
    print("\n📦 Response from Local Llama:")
    print(response.choices[0].message.content)
    print("\n✅ Script executed successfully! Checking Langfuse transmission...")

except Exception as e:
    print(f"\n❌ Error occurred: {e}")
    print("Ensure Ollama is actively running in the background ('ollama serve').")
