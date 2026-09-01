"""
STEP 4 - Make the model return a fixed shape, not prose.

Everything up to now returned free text you had to eyeball. This
returns a Python object with typed fields you can use in code.

Run:  python app4_structured_json.py
"""

from config import load_text
from services.json_service import analyse_review


def main():
    review = load_text("sample_review.txt")

    try:
        result = analyse_review(review)
    except Exception as e:
        print("Error:", e)
        print("\nIf this is a validation error, the model returned something")
        print("that did not fit ReviewAnalysis. That is the parser doing its")
        print("job - tighten the prompt or the field descriptions.")
        return

    # TODO 1: print the whole object.
    # TODO 2: print result.sentiment and result.star_rating on their own.
    # TODO 3: loop over result.issues and print each one with a dash.
    # TODO 4: print result.model_dump_json(indent=2) to see the raw JSON.

    raise NotImplementedError("Finish main()")


if __name__ == "__main__":
    main()
