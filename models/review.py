"""
The "contract" for structured output.

Pydantic checks the model's answer against these rules. If the model
returns something that does not fit, you get an error instead of
silently bad data.
"""

from typing import Literal

from pydantic import BaseModel, Field


class ReviewAnalysis(BaseModel):

    # TODO 1: sentiment
    # Should be one of exactly three values: "positive", "negative", "mixed".
    # HINT: Literal["positive", "negative", "mixed"] does this for you.
    #       Add a Field(description=...) so the model knows what you want.
    sentiment: ...

    # TODO 2: summary
    # A short summary string. Give it a minimum length so the model
    # cannot get away with a one-word answer.
    # HINT: str = Field(min_length=20, description="...")
    summary: ...

    # TODO 3: issues
    # A list of the problems reported. Between 1 and 6 items.
    # HINT: list[str] = Field(min_length=1, max_length=6, description="...")
    issues: ...

    # TODO 4: star_rating
    # An integer from 1 to 5.
    # HINT: int = Field(ge=1, le=5, description="...")
    star_rating: ...
