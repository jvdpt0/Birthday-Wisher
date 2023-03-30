import smtplib
import datetime as dt
import pandas as pd
import random

birthdays = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays.to_dict(orient='records')

birthday_choice = input('Insert new birthday? (Y or N) ').upper()
if birthday_choice == 'Y':
    new_name = input('Insert name: ')
    new_email = input(f"Insert {new_name}'s email: ")
    new_birthday = input(f"Insert {new_name}'s birthday (MM/DD/YYYY): ")
    new_birthday_date = dt.datetime.strptime(new_birthday, '%m/%d/%Y').date()
    new_year = new_birthday_date.year
    new_month = new_birthday_date.month
    new_day = new_birthday_date.day
    new_birthday_dict = {
        'name' : new_name, 
        'email' : new_email,
        'year' : new_year,
        'month' : new_month,
        'day' : new_day
    }
    birthdays_dict.append(new_birthday_dict)
    birthday_df = pd.DataFrame.from_dict(birthdays_dict)
    birthday_df.to_csv('birthdays.csv', index=False)

birthdays = pd.read_csv('birthdays.csv')

now = dt.datetime.now()
year = now.year
month = now.month
today = now.day
my_email = 'INSERT YOUR EMAIL HERE'
my_password = 'INSERT YOUR PASSWORD HERE'

for index, row in birthdays.iterrows():
    if month == row['month'] and today == row['day']:
        birthday_person = row['name']
        birthdays_person_email = row['email']
        with open (f"letter_templates\letter_{random.randint(1,3)}.txt") as file:
            letter_content = file.read()
            letter_content = letter_content.replace('[NAME]', birthday_person)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=birthdays_person_email,
                msg= f'Subject: Happy Birthday! \n\nf{letter_content}'
                )
            print('Email sent')
    
