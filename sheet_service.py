import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def load_sheet(sheet_id):
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(sheet_id).sheet1
data = sheet.get_all_records()
return pd.DataFrame(data)
