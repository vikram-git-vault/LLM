"""
Structured output using LangChain + Pydantic.

Flow:  prompt template  ->  LLM  ->  PydanticOutputParser  ->  ReviewAnalysis
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from config import MODEL, get_api_key, read_prompt
from models.review import ReviewAnalysis


# ------------------------------------------------------------------
# 1. The model
# ------------------------------------------------------------------
# TODO 1: create the LangChain chat model.
# HINT: ChatOpenAI(model=MODEL, temperature=0.1, api_key=get_api_key())
llm = None


# ------------------------------------------------------------------
# 2. The parser
# ------------------------------------------------------------------
# TODO 2: create a PydanticOutputParser pointed at ReviewAnalysis.
# This is what turns the model's raw text back into a Python object.
# HINT: PydanticOutputParser(pydantic_object=ReviewAnalysis)
parser = None


# ------------------------------------------------------------------
# 3. The prompt
# ------------------------------------------------------------------
# The parser can generate its own instructions telling the model
# exactly what JSON shape to produce. You append those to your prompt.

# TODO 3: build the PromptTemplate.
# HINT:
#   PromptTemplate(
#       template=read_prompt("structured_review.txt") + "\n\n{format_instructions}\n",
#       input_variables=["text"],
#       partial_variables={"format_instructions": parser.get_format_instructions()},
#   )
prompt = None


# ------------------------------------------------------------------
# 4. The chain
# ------------------------------------------------------------------
# TODO 4: wire them together with the pipe operator.
# HINT: chain = prompt | llm | parser
chain = None


def analyse_review(text: str) -> "ReviewAnalysis":
    """Run the chain and return a validated ReviewAnalysis object."""
    # TODO 5: invoke the chain with {"text": text} and return the result.
    raise NotImplementedError("Finish analyse_review()")
