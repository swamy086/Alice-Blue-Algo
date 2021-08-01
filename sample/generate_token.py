import os
import time
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
                               access_token=token_value,
                               master_contracts_to_download=['NSE'])
    
    print(alice_instance)
    #print(alice_instance.get_profile())


    # get instrunment by symbol
    tata_motors_nse_eq = alice_instance.get_instrument_by_symbol('NSE', 'TATAMOTORS')


    socket_opened = False
    def event_handler_quote_update(message):
        stock_data = message
        print(stock_data['ltp'])
        
    def open_callback():
        global socket_opened
        socket_opened = True

    alice_instance.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)

    while(socket_opened==False):
        pass
    
    alice_instance.subscribe(
        alice_instance.get_instrument_by_symbol('NSE', 'TATAMOTORS'),
        LiveFeedType.MARKET_DATA)
    time.sleep(10)

    value = 10
    while(value < 100):
        print("wowwwwww")
        time.sleep(1)
        value = value +1
