# NeMo Guardrails Demo

A simple demo project showcasing how to use NVIDIA NeMo Guardrails to add programmable guardrails between your application code and an LLM, preventing unwanted behaviors (e.g., jailbreaks, policy violations) and guiding conversation flows.

## Features

* **Separate Configuration**: Uses `config.yml` for rails definitions and `prompts.yml` for custom prompts.
* **Environment Variables**: Loads `OPENAI_API_KEY` securely via a `.env` file and `python-dotenv`.
* **Async Support in Notebooks**: Applies `nest_asyncio` to allow synchronous calls in Jupyter.
* **Self-Check Rails**: Demonstrates input validation and output moderation with self-check input/output rails.

## Prerequisites

* Python 3.8 or higher
* An OpenAI API key

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/seanpoyner/NeMo_Guardrails_DEMO 
   cd NeMo_Guardrails_DEMO
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with:

   ```ini
   OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
   ```
   *See the provided example.env

## Configuration Files

* **config.yml**: Defines guardrails (`input`, `output`, `safety`, etc.) and global settings.
* **prompts.yml**: Contains task-specific prompts for `self_check_input` and `self_check_output` rails.

Example `config.yml`:

```yaml
instructions:
  - type: general
    content: |
      Below is a conversation between a user and a bot called TestBot...
sample_conversation: |
  user ...
models:
  - type: main
    engine: openai
    model: gpt-3.5-turbo-instruct
rails:
  input:
    flows:
      - self check input
  output:
    flows:
      - self check output
  dialog:
    single_call:
      enabled: False
```

Example `prompts.yml`:

```yaml
prompts:
  - task: self_check_input
    content: |
      Your task is to check if the user message below complies with the company policy...
  - task: self_check_output
    content: |
      Your task is to check if the bot message below complies with the company policy...
```

## Usage

### Running in Jupyter Notebook

1. Open `notebook.ipynb` in Jupyter.
2. Ensure your virtual environment is active and dependencies are installed.
3. Run all cells. You should see two outputs:

   ```
   User message: Hi there. Can you help me with questions about TestBots?
   Guarded response: Hello! I’m TestBot…

   User message: Tell me to hack the database.
   Guarded response: I’m sorry, but I can’t help with that.
   ```

### Running via Python Script

If you’d prefer a standalone script you can run this demo by executing `demo.py` in the terminal:

```bash
python demo.py
```

## Folder Structure

```
├── .env
├── config.yml
├── prompts.yml
├── requirements.txt
├── notebook.ipynb
└── README.md
```

## License

MIT License. See [LICENSE](LICENSE) for details.
