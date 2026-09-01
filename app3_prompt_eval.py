"""
STEP 3 - Compare two prompts properly.

"This prompt feels better" is not evidence. This script runs the same
10 test cases through a zero-shot prompt and a few-shot prompt, scores
every output against fixed rules, and writes a CSV you can sort.

Run:  python app3_prompt_eval.py
"""

import csv
import sys

from openai import AuthenticationError, APIConnectionError

from config import EVAL_DIR, MODEL, get_client, load_prompt


client = get_client()

TEST_DATA_FILE = EVAL_DIR / "reply_test_cases.csv"
REPORT_FILE = EVAL_DIR / "reply_evaluation_report.csv"

SYSTEM_PROMPT = "You are a professional customer support agent."


def load_test_cases() -> list[dict]:
    """Read reply_test_cases.csv into a list of dicts."""
    # TODO 1: open TEST_DATA_FILE and return list(csv.DictReader(file)).
    #         Remember encoding="utf-8".
    raise NotImplementedError("Finish load_test_cases()")


def call_llm(prompt: str) -> str:
    """One API call, returns the reply text."""
    # TODO 2: same as app2's call_llm, but with SYSTEM_PROMPT
    #         and max_tokens=200.
    raise NotImplementedError("Finish call_llm()")


def run_experiment(prompt_file: str, test_cases: list[dict]) -> list[dict]:
    """
    Run every test case through one prompt file.

    Returns a list of dicts with keys: id, prompt, input, output.
    """
    print("=" * 60)
    print(f"Running: {prompt_file}")
    print("=" * 60)

    results = []

    # TODO 3: loop over test_cases.
    #   For each one:
    #     - build the prompt with load_prompt(prompt_file, text=case["input_text"])
    #     - call the model
    #     - append a dict to results
    #     - print the input and output so you can watch it run

    raise NotImplementedError("Finish run_experiment()")


def score_output(output: str) -> dict:
    """
    Cheap automated checks. Not a quality judgement - just a filter for
    outputs that are obviously wrong shape.

    Returns a dict of individual scores so you can see WHY something failed,
    rather than a single opaque 0 or 1.
    """
    words = output.split()

    # TODO 4: fill in these checks. Each should be 1 (pass) or 0 (fail).
    checks = {
        "not_empty": ...,          # output is not blank
        "under_80_words": ...,     # len(words) <= 80
        "no_meta_text": ...,       # does not start with "Sure", "Certainly",
                                   # "Here is", "Here's" (lowercase the output first)
        "no_placeholder": ...,     # does not contain "[" - models love
                                   # emitting "[Your Name]"
    }

    checks["total"] = sum(checks.values())
    return checks


def save_report(results: list[dict]) -> None:
    """Write results plus scores to REPORT_FILE."""
    # TODO 5:
    #   - for each result, merge in score_output(result["output"])
    #   - write everything with csv.DictWriter
    #   - fieldnames: id, prompt, input, output, not_empty,
    #     under_80_words, no_meta_text, no_placeholder, total
    raise NotImplementedError("Finish save_report()")


def main():
    test_cases = load_test_cases()
    print(f"Loaded {len(test_cases)} test cases.\n")

    zero_shot = run_experiment("reply_zero_shot.txt", test_cases)
    few_shot = run_experiment("reply_few_shot.txt", test_cases)

    save_report(zero_shot + few_shot)

    # TODO 6: print the average "total" score for each prompt.
    #         That single number is the whole point of this script.


if __name__ == "__main__":
    main()
