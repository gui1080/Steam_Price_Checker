
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
import unicodedata

# GETS THE GAME APP DATA
def gather_app_data(query):
    # to search
    # query = "Portal Steam"

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):

        j.encode("utf-8")

        i = 35   #steam app data string starts at position 35
        ready = 0   # flag for result == ready

        app_data = []

        while ready == 0:
            if j[i] != "/":
                app_data.append(j[i])
                i += 1
            else:
                ready = 1

        # convert app_data to one integer
        x = int("".join(map(str, app_data)))
        
    return(x)

# GETS THE GAME URL
def gather_url(query):
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):

        j.encode("utf-8")

    return(j)