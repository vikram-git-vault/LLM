"""
Shared configuration for the whole project.

Every script imports from here instead of repeating the same
dotenv / client / path setup. This is the main structural
improvement over practice_demo.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
# BASE_DIR is the folder THIS file lives in.
# Building every path from BASE_DIR means the scripts work no matter
# which directory you run them from. (practice_demo used bare relative
# paths like "prompts/", which only work from the project root.)

BASE_DIR = Path(__file__).resolve().parent

PROMPT_DIR = BASE_DIR / "prompts"
DATA_DIR = BASE_DIR / "data"
EVAL_DIR = BASE_DIR / "evaluation"

# ------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------

load_dotenv(BASE_DIR / ".env")

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def get_api_key() -> str:
    """Return the API key, or exit with a clear message if missing."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Error: OPENAI_API_KEY not found.")
        print("Copy .env.example to .env and put your real key in it.")
        sys.exit(1)
    return key


def get_client() -> OpenAI:
    """Raw OpenAI SDK client. Used by app1 and app2/app3."""
    return OpenAI(api_key=get_api_key())


# ------------------------------------------------------------------
# File helpers
# ------------------------------------------------------------------

def load_prompt(name: str, **variables) -> str:
    """
    Read a prompt template from prompts/ and fill in its {placeholders}.

    Example:
        load_prompt("sentiment_v1.txt", review="...")
    """
    path = PROMPT_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8").format(**variables)


def read_prompt(name: str) -> str:
    """
    Read a prompt template WITHOUT filling placeholders.
    LangChain needs the raw template with {braces} intact.
    """
    path = PROMPT_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def load_text(filename: str) -> str:
    """Read a text file from data/."""
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    return path.read_text(encoding="utf-8").strip()
