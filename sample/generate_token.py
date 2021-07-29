import os
from alice_blue import *
from datetime import date

def generate_token():
    date_open = open(os.path.join(CURRENT_PATH, 'date.txt'))
    date_in_file = date_open.read()
    print(date_in_file)
    
    if DATE_TODAY != date_in_file:
        print("----------------")
        print("generating new token")
        # Create a new token for today
        new_token = AliceBlue.login_and_get_access_token(
            username='193734', password='AUG@micro123', twoFA='a',
            api_secret='XELKQq1kg8PYxY4fSJ8j2S3NtVh1AZSXAms1RV91XhGcQiloAvBFblsex3n41jV6',
            redirect_url='https://ant.aliceblueonline.com/plugin/callback',
            app_id='SePv1JYhfu')
        token_file = open('token.txt', 'w')
        token_file.write(new_token)
        token_file.close()

        open_date = open(os.path.join(CURRENT_PATH, 'date.txt'), 'w')
        open_date.write(str(date.today()))
        open_date.close()
        return new_token
    else:
        print("gettting existing token value")
        open_token = open(TOKEN_FILE_PATH)
        token_info = open_token.read()
        open_token.close()
        return token_info

        
        
if __name__== '__main__':
    # variables
    DATE_TODAY = str(date.today())
    CURRENT_PATH = os.getcwd()
    TOKEN_FILE_PATH = os.path.join(CURRENT_PATH, 'token.txt')
    print(TOKEN_FILE_PATH)
    # calling generating token method
    token_value = generate_token()
    print("---------------TOKEN-------------------------")
    print(token_value)
    print("---------------------------------------------")


    alice_instance = AliceBlue(username='193734',
                               password='AUG@micro123',
                               access_token=token_value)
    
    print(alice_instance)
    print(alice_instance.get_balance())
   









   
