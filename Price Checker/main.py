from steam_app_data import gather_app_data
from steam_app_data import gather_url
from price import get_price

while(1):
    
    game = raw_input("Enter the name of the Steam game you want to check (press 1 to exit) : ")

    if game == '1':
        break;
    
    print(game)

    aux = " Steam"
    # join game name + steam
    query = game + aux
    #print(query)

    app_data_main = gather_app_data(query)
    print (app_data_main)

    # structure of url:
    # https://steamdb.info/app/220/
    # https://store.steampowered.com/app/220/HalfLife_2/
    # taking out the name by the end of steam url will get in the same place 

    url = gather_url(query)
    print(url)

    price = {}
    price = get_price(url, app_data_main)
    # print(price)

    j = 0

    while(1):
        
        if j == 0:
            flag = 'Brazilian Real'
        if j == 1:
            flag = 'U.S. Dollar'
        if j == 2:
            flag = 'Canadian Dollar'
        if j == 3:
            flag = 'Chinese Yuan Renminbi'
        if j == 4:
            flag = 'Australian Dollar'
        if j == 5:
            break; 
            
        i = 0
        while(1):
            if (price['Currency'].get(i) == flag):
                break;
            i = i + 1

        print(price['Currency'].get(i))
        print(price['Price atm'].get(i))
        print(price['Lowest Price Ever'].get(i))
        j = j + 1
    