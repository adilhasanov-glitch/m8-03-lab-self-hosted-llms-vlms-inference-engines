"""
Task 2 — Hit the local Ollama endpoint from Python.

Ollama exposes an OpenAI-compatible HTTP API on http://localhost:11434.
That means the SAME client code you used for a hosted API works here —
you only change the base URL (and the API key is a dummy value locally).

Run Ollama first (it starts a server automatically when you `ollama run`
or `ollama serve`), then:

    pip install -r requirements.txt
    python local_client.py
"""

from openai import OpenAI

# Point the OpenAI client at your LOCAL Ollama server instead of the cloud.
# This demonstrates that calling an LLM is simply sending an HTTP request
# to an inference server, regardless of where that server is running.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Required by the client but ignored by Ollama.
)

MODEL = "llama3.2:3b"


def main() -> None:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a concise assistant."},
            {
                "role": "user",
                "content": "In one sentence, what is an inference engine?"
            },
        ],
    )

    print("Model response:")
    print(response.choices[0].message.content)

    print(
        "\nReflection:\n"
        "This program uses the same request structure as a hosted LLM API. "
        "The client sends a JSON request containing the model name and chat "
        "messages, and receives a JSON response with the model's reply. "
        "The only difference is that the inference server is running on "
        "localhost instead of a cloud provider like Gemini or OpenAI."
    )


if __name__ == "__main__":
    main()
