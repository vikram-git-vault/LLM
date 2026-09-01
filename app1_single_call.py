"""
STEP 1 - One raw API call.

Goal: prove your key works and see what the API actually returns.
Everything is hardcoded here on purpose. Later steps move things out.

Run:  python app1_single_call.py
"""

from openai import AuthenticationError, APIConnectionError

from config import MODEL, get_client


client = get_client()

REVIEW = (
    "The sound quality is great but the left earbud disconnects every "
    "twenty minutes and the Android app crashes on launch. Support has "
    "not replied in two weeks."
)


def main():
    print("Sending prompt...")

    try:
        # TODO 1: call the chat completions API.
        # HINT:
        #   response = client.chat.completions.create(
        #       model=MODEL,
        #       messages=[
        #           {"role": "system", "content": "You are a helpful assistant."},
        #           {"role": "user", "content": f"Summarise this review: {REVIEW}"},
        #       ],
        #       temperature=0.1,
        #       max_tokens=150,
        #   )
        response = None

        # TODO 2: print the reply text.
        # HINT: response.choices[0].message.content

        # TODO 3: print the token count.
        # HINT: response.usage.total_tokens
        #       Get in the habit of watching this - it is what you pay for.

        raise NotImplementedError("Finish main()")

    except AuthenticationError:
        print("Authentication error: check OPENAI_API_KEY in your .env file.")
    except APIConnectionError:
        print("Connection error: check your internet connection.")


if __name__ == "__main__":
    main()
