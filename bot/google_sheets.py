import gspread
from google.oauth2.service_account import Credentials
from bot.config import CREDENTIALS_FILE, GOOGLE_SHEET_ID, GOOGLE_SHEET_TAB

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(GOOGLE_SHEET_TAB)



def save_to_sheet(data: dict):
    values = [data.get(col, "") for col in sheet.row_values(1)]
    sheet.append_row(values)