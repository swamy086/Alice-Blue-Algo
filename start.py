import os
import time
from alice_blue import *
from datetime import date
import logging

logging.basicConfig(filename="logs.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running file")
logger = logging.getLogger()

def generate_token():
    """
    Generates new token for the day or returns existing token in token.txt file
    :return: generated token or existing token from token.txt file
    """
    date_open = open(os.path.join(CURRENT_PATH, 'date.txt'))
    date_in_file = date_open.read()
    print(date_in_file)

    # if date mentioned in the file is not matching generate new token
    if DATE_TODAY != date_in_file:
        print("----------------")
        print("generating new token")
        # Create a new token for today
        new_token = AliceBlue.login_and_get_access_token(
            username='193734', password='PKswamy@15697', twoFA='1',
            api_secret='XELKQq1kg8PYxY4fSJ8j2S3NtVh1AZSXAms1RV91XhGcQiloAvBFblsex3n41jV6',
            redirect_url='https://ant.aliceblueonline.com/plugin/callback',
            app_id='SePv1JYhfu')

        # update the newly generated token in token.txt file
        print(new_token)
        token_file = open('token.txt', 'w')
        token_file.write(new_token)
        token_file.close()

        open_date = open(os.path.join(CURRENT_PATH, 'date.txt'), 'w')
        open_date.write(str(date.today()))
        open_date.close()
        return new_token
    # if token is already generated for the day then read it from token.txt file.
    else:
        print("getting existing token value")
        open_token = open(TOKEN_FILE_PATH)
        token_info = open_token.read()
        open_token.close()
        return token_info


def buy_order(stock_name, buy_price):

    responce =  alice_instance.place_order(transaction_type=TransactionType.Buy,
                          instrument=alice_instance.get_instrument_by_symbol('NSE', stock_name),
                          quantity=1,
                          order_type=OrderType.StopLossLimit,
                          product_type=ProductType.Intraday,
                          price= buy_price,
                          trigger_price=8.0,
                          stop_loss=None,
                          square_off=None,
                          trailing_sl=None,
                          is_amo=False)

    print(type(responce))
    print(responce)

    if responce['status'] == 'success':
        order_id = responce.get('data')['oms_order_id']

    print("order-id****")
    print(order_id)

    order_history = alice_instance.get_order_history(order_id)
    print("*******order history********")
    print(order_history)
    order_status = order_history.get('order_status')

    return order_status

def sell_order(stock_name, buy_price):

    responce = alice_instance.place_order(transaction_type=TransactionType.Sell,
                                          instrument=alice_instance.get_instrument_by_symbol('NSE', stock_name),
                                          quantity=1,
                                          order_type=OrderType.StopLossLimit,
                                          product_type=ProductType.Intraday,
                                          price=buy_price,
                                          trigger_price=8.0,
                                          stop_loss=None,
                                          square_off=None,
                                          trailing_sl=2,
                                          is_amo=False)

    print(type(responce))
    print(responce)

    if responce['status'] == 'success':
        order_id = responce.get('data')['oms_order_id']

    print("order-d****")
    print(order_id)

    order_history = alice_instance.get_order_history(order_id)
    print(order_history)

        
        
if __name__== '__main__':
    # variables
    DATE_TODAY = str(date.today())
    CURRENT_PATH = os.getcwd()
    TOKEN_FILE_PATH = os.path.join(CURRENT_PATH, 'token.txt')

    logger.debug(f"token file path is {TOKEN_FILE_PATH}")
    print(TOKEN_FILE_PATH)
    stock_price = 0
    # Fetch the token
    token_value = generate_token()

    if token_value or token_value is not None:
        print("---------------TOKEN-------------------------")
        print(token_value)
        print("---------------------------------------------")

        # Creating alice token for all future calls
        alice_instance = AliceBlue(username='193734',
                                   password='PKswamy@15697',
                                   access_token=token_value,
                                   master_contracts_to_download=['NSE'])

        print(alice_instance)
        # print(alice_instance.get_profile())

        # get instrunment by symbol
        tata_motors_nse_eq = alice_instance.get_instrument_by_symbol('NSE', 'TATAMOTORS')


    ######################LIVE FEED#################

    socket_opened = False
    def event_handler_quote_update(message):
        stock_data = message
        print(stock_data['ltp'])
        stock_price = stock_data['ltp']
        print(stock_price)
        ret = buy_order(stock_name='ONGC', buy_price=stock_price)
        print(ret)
        # sell_order()

    def open_callback():
        global socket_opened
        socket_opened = True


    #alice_instance.start_websocket(subscribe_callback=event_handler_quote_update,
    #                               socket_open_callback=open_callback,
    #                               run_in_background=True)

    #while (socket_opened == False):
    #    pass

  
    #alice_instance.subscribe(
    #   alice_instance.get_instrument_by_symbol('NSE', 'ONGC'),
    #   LiveFeedType.MARKET_DATA)



    ##########LIVE FEED #################


################# LIVE FEED TRY #################
    # time.sleep(10)
    # value = 10
    # while (value < 100):
    #     alice_instance.subscribe(
    #         alice_instance.get_instrument_by_symbol('NSE', 'TATAMOTORS'),
    #         LiveFeedType.MARKET_DATA)
    #     print("wowwwwww")
    #     # print(stock_price)
    #     time.sleep(1)
    #     value = value + 1

    buy_order(stock_name="ONGC", buy_price=139.0)
    sell_order(stock_name="ONGC", buy_price=139.0)

#########################################################


