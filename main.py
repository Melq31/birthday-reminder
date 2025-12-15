from datetime import datetime, date
from sheet_service import load_sheet
from email_service import send_email
from whatsapp_service import send_whatsapp
import os


SHEET_ID = os.environ['SHEET_ID']


df = load_sheet(SHEET_ID)


today = date.today()


for _, row in df.iterrows():
birth = datetime.strptime(row['nascimento'], '%Y-%m-%d').date()
next_birthday = birth.replace(year=today.year)
if next_birthday < today:
next_birthday = next_birthday.replace(year=today.year + 1)


days_diff = (next_birthday - today).days
days_before = [int(x) for x in str(row['dias_antes']).split(',')]


if days_diff in days_before:
msg = f"🎉 Lembrete: o aniversário de {row['nome']} é em {days_diff} dia(s)!"
send_email(row['email'], 'Lembrete de Aniversário', msg)
send_whatsapp(row['whatsapp'], msg)
