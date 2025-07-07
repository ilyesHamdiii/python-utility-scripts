import urllib.request as urlib


def check(url="https://fr.wikipedia.org/wiki/Drapeau_de_la_Palestine"):
    print("Checking connectivity . . . ")
    response=urlib.urlopen(url)
    if response.getcode()==200:
        print(f"connected to {url } succesfully")
        print(f"the response code was :{response.getcode()}")
    else:
        print("Server is down or under  maintenance")


if __name__== "__main__":
    url=input("input the site of the url u want to check ")
    while url=="":
        url=input("input the site of the url u want to check ")


        
    check(url)