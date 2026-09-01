"""
A three-step chain where each step feeds the next.

    review text
        -> step 1: extract issues
        -> step 2: assign a priority based on those issues
        -> step 3: draft a support reply using issues + priority

This is the difference between "three separate prompts" (app2) and
"a pipeline" (this file). Step 2 never sees the raw review, only the
output of step 1.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from config import MODEL, get_api_key, read_prompt


# ------------------------------------------------------------------
# Model
# ------------------------------------------------------------------
# TODO 1: create the ChatOpenAI model, same as in json_service.py.
llm = None


# ------------------------------------------------------------------
# Step 1: extract issues from the raw review
# ------------------------------------------------------------------
# TODO 2: build a PromptTemplate from "extract_issues.txt"
#         with input_variables=["review"], then pipe it into the llm.
# HINT: issues_chain = issues_prompt | llm
issues_prompt = None
issues_chain = None


# ------------------------------------------------------------------
# Step 2: assign a priority from the issue list
# ------------------------------------------------------------------
# TODO 3: same pattern, using "priority_v1.txt" with
#         input_variables=["issues"].
priority_prompt = None
priority_chain = None


# ------------------------------------------------------------------
# Step 3: draft the reply
# ------------------------------------------------------------------
# TODO 4: same pattern, using "reply_few_shot.txt" with
#         input_variables=["text"].
#
# Think about this one: reply_few_shot.txt only has a {text} slot.
# You will need to feed it something that combines the issues and the
# priority. Either build that string yourself, or add a new prompt file
# with {issues} and {priority} slots. The second option is cleaner.
reply_prompt = None
reply_chain = None


def run_review_pipeline(review: str) -> dict:
    """
    Run all three steps in order and return a dict with keys:
    "issues", "priority", "reply".
    """
    # TODO 5: invoke step 1.
    #   response = issues_chain.invoke({"review": review})
    #   issues = response.content.strip()

    # TODO 6: invoke step 2, passing in the issues from step 1.

    # TODO 7: invoke step 3, passing in issues (and priority).

    # TODO 8: return the dict.
    raise NotImplementedError("Finish run_review_pipeline()")
