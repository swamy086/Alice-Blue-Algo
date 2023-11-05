from alice_blue import *
import os
from datetime import date

def generate_token():
    date_open = open(os.path.join(current_path, 'date.txt'))
    date_in_file = date_open.read()
    print(date_in_file)
    if date.today() != date_in_file:
        # Create a new token for today
        new_token = AliceBlue.login_and_get_access_token(
            username='193734', password='DEC@micro123', twoFA='1',
            api_secret='XELKQq1kg8PYxY4fSJ8j2S3NtVh1AZSXAms1RV91XhGcQiloAvBFblsex3n41jV6',
            redirect_url='https://ant.aliceblueonline.com/plugin/callback',
            app_id='SePv1JYhfu')
        token_file = open('token.txt', 'w')
        token_file.write(new_token)
        token_file.close()

        open_date = open(os.path.join(current_path, 'date.txt'), 'w')
        open_date.write(str(date.today()))
        
        
today = date.today()
print(today)
current_path = os.getcwd()
token_file_path = os.path.join(current_path, 'token.txt')
#print(token_path)
open_token = open(token_file_path)
token_info = open_token.read()

#print(token_info)
#file = open('token.txt', 'w')
#ile.write("jlrjslfjs;'")
#file.close()
#print(f)
#access_token = AliceBlue.login_and_get_access_token(username='193734', password='AUG@micro123', twoFA='a',  api_secret='XELKQq1kg8PYxY4fSJ8j2S3NtVh1AZSXAms1RV91XhGcQiloAvBFblsex3n41jV6', redirect_url='https://ant.aliceblueonline.com/plugin/callback', app_id='SePv1JYhfu')
#print(access_token)
generate_token()