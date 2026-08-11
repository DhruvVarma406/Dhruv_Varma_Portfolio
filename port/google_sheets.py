import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


credentials = Credentials.from_service_account_file(
    "credentials/dhruv-portfolio-505117-6d928fda43c8.json",
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