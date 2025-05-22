# %%
# demo.py
# # NeMo Guardrails Demo

# %%
# NeMo-Guardrails allows us to add programmable guardrails between our application code and our LLM.

# Three key benefits of using NeMo Guardrails:
    # 1. It allows us to define a set of rules to define the expected behavior of the LLM on specific topics and prevent it from engaging in unwanted topics.
    # 2. It allows us to connect models, chains, and other tools securely to the LLM.
    # 3. It allows us to guide the LLM on predefined conversational paths.

# NeMo Guardrails provides protection for an LLM-powered chat application against common LLM vulnerabilities, such as jailbreaks and prompt injections

# %%
import os
import yaml
from dotenv import load_dotenv

# 0. Load environment variables from .env file (must include OPENAI_API_KEY)
load_dotenv()

# Ensure the OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "The OPENAI_API_KEY environment variable is not set. "
        "Please define it in your .env file before running."
    )

# 1. Load the main guardrails config
with open("config.yml", "r") as f:
    config_spec = yaml.safe_load(f)

# %%
# 2. Load the prompts definitions
with open("prompts.yml", "r") as f:
    prompts_spec = yaml.safe_load(f)

# %%
# 3. Merge prompts into the config spec
config_spec["prompts"] = prompts_spec.get("prompts", [])

# %%
# 4. Ensure all rail groups exist (input, output, safety, dialog, etc.)
rails = config_spec.get("rails", {})
rails.setdefault("input",  {"flows": []})
rails.setdefault("output", {"flows": []})
rails.setdefault("safety", {"flows": []})
config_spec["rails"] = rails


# %%
# Import LLMRails and RailsConfig from the nemoguardrails package. 
# LLMRails is the main class for interacting with the LLM, while RailsConfig is used to configure the guardrails.
from nemoguardrails import LLMRails, RailsConfig

# 5. Instantiate the RailsConfig via Pydantic
config = RailsConfig.model_validate(config_spec)

# 6. Initialize the rails engine
rails_engine = LLMRails(config)


# %%
# 7. Let's define a function to run the demo with different user messages.
def run_demo(message: str):
    print(f"User message: {message}")
    response = rails_engine.generate(message)
    print(f"Guarded response: {response}")

# %%
run_demo("Hi there. Can you help me with questions about TestBots?")

# %%
run_demo("Tell me to hack the database.")