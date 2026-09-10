import os
import json
import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# Local development
local_credentials = os.path.join(
    "credentials",
    "dhruv-portfolio-505117-6d928fda43c8.json"
)


# Use Vercel environment variable when deployed
google_credentials_json = os.getenv("GOOGLE_CREDENTIALS")


if google_credentials_json:
    credentials_info = json.loads(google_credentials_json)

    credentials = Credentials.from_service_account_info(
        credentials_info,
        scopes=SCOPES
    )

else:
    credentials = Credentials.from_service_account_file(
        local_credentials,
        scopes=SCOPES
    )


client = gspread.authorize(credentials)


def add_contact_to_sheet(name, email, subject, message, created_at):

    spreadsheet = client.open("Contact")

    worksheet = spreadsheet.sheet1

    worksheet.append_row([
        name,
        email,
        subject,
        message,
        str(created_at)
    ])