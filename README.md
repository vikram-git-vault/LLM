# LLM — review-insights

A hands-on project for learning how to work with large language models
through the OpenAI API and LangChain.

Everything is built around one realistic task: **turning messy customer
product reviews into structured, useful output** — sentiment, a list of
concrete problems, a priority, and a drafted support reply.

The project is deliberately split into five small programs. Each one
adds exactly one new idea on top of the last, so you can see why each
piece of complexity exists instead of meeting it all at once.

---

## Status: this is a scaffold

The folder structure, prompts, test data, configuration and this README
are **complete and working**.

The application logic is **intentionally left unwritten**. Every file
contains numbered `TODO` comments with hints that describe the shape of
the answer without giving you the code. This is a learning exercise, not
a finished product.

If you are reading this repo to learn from it, start at
`app1_single_call.py` and work down.

---

## Quick start

```bash
git clone https://github.com/vikram-git-vault/LLM.git
cd LLM

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# open .env and paste in your real OpenAI API key
```

Then run the steps in order:

```bash
python app1_single_call.py
python app2_file_prompts.py
python app3_prompt_eval.py
python app4_structured_json.py
python app5_pipeline.py
```

You need an OpenAI API key with credit on it. Each script costs a
fraction of a cent to run.

---

## The five steps, and why they exist

| # | File | The one new idea |
|---|---|---|
| 1 | `app1_single_call.py` | Make a single API call. Prompt is hardcoded. See exactly what the API returns and what it costs in tokens. |
| 2 | `app2_file_prompts.py` | Move prompts out of code and into text files. Now you can edit a prompt without touching Python. |
| 3 | `app3_prompt_eval.py` | Stop guessing which prompt is better. Run 10 test cases through two competing prompts, score every output, write a CSV. |
| 4 | `app4_structured_json.py` | Force the model to return a fixed shape. Get a typed Python object back instead of prose you have to eyeball. |
| 5 | `app5_pipeline.py` | Chain calls together, so step 2 reads step 1's output rather than the original input. |

---

## What every file does

### Top level

| File | Purpose |
|---|---|
| `README.md` | This file. |
| `requirements.txt` | The Python packages the project needs, with a comment explaining what each is for. Install with `pip install -r requirements.txt`. |
| `.env.example` | A template showing which environment variables are needed. Safe to commit — it contains no real key. Copy it to `.env` and fill in your own. |
| `.env` | **Not in this repo, and never should be.** Holds your real API key. Listed in `.gitignore`. |
| `.gitignore` | Tells git what never to commit: `.env`, the virtual environment, `__pycache__`, `.DS_Store`, and generated evaluation reports. |
| `config.py` | Shared setup used by every other file. Explained in detail below. |

### `config.py` — the shared foundation

Every other file imports from here. It handles four things:

- **Paths.** `BASE_DIR` is the folder `config.py` itself sits in, and
  `PROMPT_DIR`, `DATA_DIR` and `EVAL_DIR` are built from it. This means
  the scripts work no matter which directory you run them from.
- **Environment.** Loads `.env` and reads `OPENAI_MODEL`, defaulting to
  `gpt-4.1-mini`.
- **Client.** `get_client()` returns a ready OpenAI client, and exits
  with a clear message if the API key is missing.
- **File helpers.** `load_prompt()` reads a template and fills in its
  `{placeholders}`. `read_prompt()` reads a template and leaves the
  braces alone, because LangChain needs them intact. `load_text()`
  reads an input file from `data/`.

### The five applications

| File | What it does |
|---|---|
| `app1_single_call.py` | Sends one hardcoded review to the model and prints the reply plus the token count. Everything is inline on purpose — no helper functions, no external files. The point is to see the raw mechanics of an API call. |
| `app2_file_prompts.py` | Loads the review from `data/sample_review.txt` and runs three prompts against it — sentiment, issue extraction, and a one-line verdict — each loaded from `prompts/`. The API call is wrapped in a reusable `call_llm()` function instead of being copy-pasted three times. |
| `app3_prompt_eval.py` | The evaluation harness. Reads 10 test cases from `evaluation/reply_test_cases.csv`, runs each one through both `reply_zero_shot.txt` and `reply_few_shot.txt`, scores every output against four fixed checks, and writes `evaluation/reply_evaluation_report.csv`. The output is a number per prompt, so you can say which prompt is better rather than feel it. |
| `app4_structured_json.py` | Asks for a `ReviewAnalysis` object rather than free text, using the chain in `services/json_service.py`. If the model returns something that does not fit the schema, you get a validation error instead of silently bad data. |
| `app5_pipeline.py` | Runs the three-stage chain in `services/review_pipeline.py` and prints the result. |

### `prompts/` — the prompt templates

Plain text files with `{placeholder}` slots. Edit these to change model
behaviour; you should rarely need to touch the Python.

| File | Used by | Purpose |
|---|---|---|
| `sentiment_v1.txt` | app2 | Basic sentiment classification. Loose wording, on purpose. |
| `sentiment_v2.txt` | app2 | The same task with explicit rules and a defined "mixed" case. Compare the two outputs — this is your first lesson in prompt specificity. |
| `extract_issues.txt` | app2, pipeline step 1 | Pulls the concrete problems out of a raw review. |
| `extract_issues_v2.txt` | reference | The same task run against a *summary* rather than the raw review, with a hard cap on the number of items. |
| `verdict.txt` | app2 | Produces a one-line, 15-word verdict covering the best and worst point. |
| `priority_v1.txt` | pipeline step 2 | Triages a list of problems into high / medium / low, with explicit definitions for each level. |
| `reply_zero_shot.txt` | app3 | Drafts a support reply using instructions only. |
| `reply_few_shot.txt` | app3, pipeline step 3 | The same task with three worked examples. This is the "few-shot" half of the A/B test in app3. |
| `structured_review.txt` | app4 | Asks for the full structured analysis. LangChain appends the format instructions automatically. |

### `models/` — the output contract

| File | Purpose |
|---|---|
| `models/review.py` | Defines `ReviewAnalysis`, a Pydantic model with four fields: `sentiment` (one of three fixed values), `summary` (a string with a minimum length), `issues` (a list of 1–6 strings) and `star_rating` (an integer from 1 to 5). This class *is* the contract — it is what makes the model's output checkable. |
| `models/__init__.py` | Empty. Marks the folder as an importable Python package. |

### `services/` — the LangChain logic

| File | Purpose |
|---|---|
| `services/json_service.py` | Builds the structured-output chain: prompt → model → `PydanticOutputParser` → `ReviewAnalysis`. Exposes one function, `analyse_review(text)`. |
| `services/review_pipeline.py` | Builds the three-stage pipeline. Step 1 extracts issues from the review. Step 2 assigns a priority based only on those issues. Step 3 drafts a reply using both. Exposes one function, `run_review_pipeline(review)`. |
| `services/__init__.py` | Empty. Marks the folder as an importable Python package. |

### `data/` and `evaluation/`

| File | Purpose |
|---|---|
| `data/sample_review.txt` | A realistic ~200-word product review with a deliberate mix of praise and complaints, so "mixed" sentiment is the correct answer and there are several distinct issues to extract. |
| `evaluation/reply_test_cases.csv` | 10 short customer messages with `id` and `input_text` columns. Deliberately varied: some are angry, one is purely positive, one is a question rather than a complaint. Good prompts handle all of them; weak prompts fall over on the edge cases. |
| `evaluation/reply_evaluation_report.csv` | Generated by app3, not committed to the repo. Contains every output plus its four check scores and a total. |

---

## Concepts this project covers

- **Zero-shot vs few-shot prompting** — instructions alone versus
  instructions plus worked examples (`reply_zero_shot.txt` vs
  `reply_few_shot.txt`).
- **Prompt versioning** — keeping `v1` and `v2` side by side so you can
  compare instead of overwrite.
- **Prompt evaluation** — scoring outputs against fixed checks to get a
  number, not an impression.
- **Structured output** — using Pydantic to force and validate a schema.
- **Chaining** — composing several calls where each step consumes the
  previous step's output.
- **Separation of concerns** — configuration, prompts, schemas, business
  logic and entry points each live in their own place.

---

## Notes on cost and safety

- Every script prints or can print token usage. Get in the habit of
  watching it. `app5_pipeline.py` makes three calls where each prompt
  contains the previous step's output, so chains get expensive quickly.
- `temperature` is set to `0.1` everywhere. Low temperature means more
  repeatable output, which is what you want while you are comparing
  prompts.
- **Never commit `.env`.** It is already in `.gitignore`. If a key ever
  does reach GitHub, treat it as compromised and rotate it immediately
  at platform.openai.com — deleting the commit is not enough.
