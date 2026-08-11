import os
import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# Local development path
local_credentials = os.path.join(
    "credentials",
    "dhruv-portfolio-505117-6d928fda43c8.json"
)

# Render Secret File path
render_credentials = "/etc/secrets/dhruv-portfolio-505117-6d928fda43c8.json"


# Use Render credentials when deployed,
# otherwise use the local credentials file
if os.path.exists(render_credentials):
    credentials_path = render_credentials
else:
    credentials_path = local_credentials


credentials = Credentials.from_service_account_file(
    credentials_path,
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