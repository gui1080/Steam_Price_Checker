from steam_app_data import gather_app_data
from steam_app_data import gather_url
from price import get_price
from Tkinter import *


def terminate_program():
    quit()
    
def Click():
    
    game = e.get()
    print(game)
    
    aux = " Steam"
    # join game name + steam
    query = game + aux
    #print(query)

    app_data_main = gather_app_data(query)
    
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
            flag = 'Australian Dollar'
        if j == 4:
            break; 
            
        i = 0
        while(1):
            if (price['Currency'].get(i) == flag):
                break;
            i = i + 1

        print(price['Currency'].get(i))
        
        print(price['Price atm'].get(i))
        
        print(price['Lowest Price Ever'].get(i))
        
        if j == 0:
            
            currency_brl = price['Currency'].get(i)
            price_atm_brl = price['Price atm'].get(i)
            lowest_price_brl = price['Lowest Price Ever'].get(i)
            
        if j == 1:
            
            currency_usd = price['Currency'].get(i)
            price_atm_usd = price['Price atm'].get(i)
            lowest_price_usd = price['Lowest Price Ever'].get(i)
            
        if j == 2:
            
            currency_cnd = price['Currency'].get(i)
            price_atm_cnd = price['Price atm'].get(i)
            lowest_price_cnd = price['Lowest Price Ever'].get(i)
            
        if j == 3:
            
            currency_aud = price['Currency'].get(i)
            price_atm_aud = price['Price atm'].get(i)
            lowest_price_aud = price['Lowest Price Ever'].get(i)
            
            
        j = j + 1
    
    
    top = Toplevel()
    top.title('Results') 
       
    Label_BR = Label(top, text="Price in Brasil: ")
    Label_BR.grid(row=1, column=1)
    Label_Price_BR = Label(top, text=price_atm_brl)
    Label_Price_BR.grid(row=1, column=2)

   
    Label_US = Label(top, text="Price in USA: ")
    Label_US.grid(row=2, column=1)
    Label_Price_usd = Label(top, text=price_atm_usd)
    Label_Price_usd.grid(row=2, column=2)
   
    Label_CND = Label(top, text="Price in Canada")
    Label_CND.grid(row=3, column=1)
    Label_Price_cnd = Label(top, text=price_atm_cnd)
    Label_Price_cnd.grid(row=3, column=2)
    
       
    Label_AUD = Label(top, text="Price in Australia")
    Label_AUD.grid(row=4, column=1)
    Label_Price_aud = Label(top, text=price_atm_aud)
    Label_Price_aud.grid(row=4, column=2)

 
root = Tk()

Label_main = Label(root, text="Enter the name of the Steam game you want to check")
Label_main.grid(row=1, column=1)

e = Entry(root, width=50, borderwidth=5)
e.grid(row=2, column=1)

Button_main = Button(root, text="Submit!", command=Click)
Button_main.grid(row=3, column=1)

Button_Exit = Button(root, text="Exit", command=terminate_program)
Button_Exit.grid(row=4, column=1)

#Label.grid(row=1, column=1)
#e.grid(row=1, column=2)
#Button.grid(row=1, column=3)
#Button_Exit.grid(row=1, column=4)

e.focus()

root.mainloop()
