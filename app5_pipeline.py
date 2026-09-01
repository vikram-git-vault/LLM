"""
STEP 5 - Chain the calls so each step builds on the last.

app2 ran three independent prompts against the same input.
This runs three prompts where step 2 reads step 1's output.

Run:  python app5_pipeline.py
"""

from config import load_text
from services.review_pipeline import run_review_pipeline


def main():
    review = load_text("sample_review.txt")

    result = run_review_pipeline(review)

    # TODO 1: print result["issues"], result["priority"] and result["reply"]
    #         under clear headings.

    # TODO 2 (worth doing): print the token usage for the whole pipeline.
    #         Three chained calls cost roughly three times one call, and
    #         step 3's prompt contains step 1 and 2's output. Chains get
    #         expensive fast. Measure it before you build a longer one.

    raise NotImplementedError("Finish main()")


if __name__ == "__main__":
    main()
