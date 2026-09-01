# review-insights

A practice project for learning prompt engineering with the OpenAI API
and LangChain, built around one task: turning messy customer product
reviews into structured, useful output.

Same five patterns as `practice_demo`, different domain, cleaner
structure.

## Setup

```bash
cd ~/Projects/review-insights

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# then open .env and paste in your real API key
```

## The five steps

Work through them in order. Each one adds exactly one new idea.

| File | New idea |
|---|---|
| `app1_single_call.py` | One raw API call. Prompt hardcoded. See what comes back and what it costs in tokens. |
| `app2_file_prompts.py` | Prompts move into `prompts/*.txt`, input moves into `data/`. The API call becomes a reusable function. |
| `app3_prompt_eval.py` | Run 10 test cases through two competing prompts, score every output, write a CSV. Stop guessing which prompt is better. |
| `app4_structured_json.py` | Force the model into a fixed schema with Pydantic. Get an object back, not prose. |
| `app5_pipeline.py` | Chain three calls so each step feeds the next. |

## Layout

```
config.py                 shared setup: paths, env, client, file loaders
data/                     input text
prompts/                  prompt templates (edit these, not the Python)
models/review.py          the Pydantic schema
services/json_service.py  structured-output chain
services/review_pipeline.py  three-step chain
evaluation/               test cases in, scored report out
```

## Two things done differently from practice_demo

**1. All paths come from `config.py`, built off `BASE_DIR`.**
`practice_demo` used bare relative paths like `Path("prompts")`, which
only work if you run the script from the project root. Here the scripts
work from anywhere.

**2. No API calls at import time.**
In `practice_demo`, `services/content_pipeline.py` created the LLM and
read prompt files the moment it was imported. That makes the module
impossible to import without a valid key, and impossible to test. Here
the setup is explicit.

## Status

Scaffold. Every `TODO` is yours to fill in. The hints tell you the
shape of the answer without writing it for you.
