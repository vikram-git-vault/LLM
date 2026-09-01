"""
STEP 2 - Prompts live in files, not in code.

Same idea as app1, but the review comes from data/ and the three
prompts come from prompts/. You can now edit a prompt without
touching any Python.

Run:  python app2_file_prompts.py
"""

import sys

from openai import AuthenticationError, APIConnectionError

from config import MODEL, get_client, load_prompt, load_text


client = get_client()


def call_llm(prompt: str, system: str = "You are a helpful assistant.") -> str:
    """
    Send one prompt and return just the reply text.

    Wrapping the API call in a function is the point of this step:
    app1 repeated the whole block three times, this does not.
    """
    try:
        # TODO 1: make the API call and return the message content.
        # HINT: same shape as app1, but use the `prompt` and `system`
        #       arguments instead of hardcoded strings.
        #       Return response.choices[0].message.content.strip()
        raise NotImplementedError("Finish call_llm()")

    except AuthenticationError:
        print("Authentication error: check OPENAI_API_KEY.")
        sys.exit(1)
    except APIConnectionError:
        print("Connection error.")
        sys.exit(1)


def main():
    review = load_text("sample_review.txt")
    print(f"Loaded review: {len(review)} characters\n")

    # TODO 2: sentiment
    #   prompt = load_prompt("sentiment_v1.txt", review=review)
    #   print the prompt, then print call_llm(prompt)

    # TODO 3: issues
    #   same, using "extract_issues.txt"

    # TODO 4: verdict
    #   same, using "verdict.txt"

    # TODO 5 (once it works): swap sentiment_v1.txt for sentiment_v2.txt
    #   and see whether the stricter wording changes the answer.

    raise NotImplementedError("Finish main()")


if __name__ == "__main__":
    main()
