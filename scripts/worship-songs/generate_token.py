"""
One-time script to generate OAuth token.json for YouTube API access.

Run this locally:
    python scripts/worship-songs/generate_token.py

It will open a browser for you to authorize, then save token.json.
Copy the contents of token.json into the YOUTUBE_OAUTH_TOKEN_JSON GitHub secret.
"""

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
]


def main():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)

    with open("token.json", "w") as f:
        f.write(creds.to_json())

    print("Token saved to token.json")
    print("Add its contents as the YOUTUBE_OAUTH_TOKEN_JSON GitHub secret.")


if __name__ == "__main__":
    main()
