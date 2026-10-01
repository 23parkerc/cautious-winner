countries={
    "england":"london",
    "spain":"madrid"
}
print("1. Insert Country and Capital")
print("2. Display all countries")
print("3. Delete countries")
print("4. Get capitals")
print("5. Exit")
while True:
    option=input("pick a number 1-5")
    if option=="1":
        country=input("pick a country")
        capital=input("whats the capital of "+country)
        countries[country]=capital
    elif option=="2":
        print(countries)
    elif option=="3":
        word=input("what is the country you want to delete")
        countries.pop(word)
        print("")
    elif option=="4":
        name=input("enter the countrys name")
        print(countries[name])
    elif option=="5":
        break




# print(countries["spain"])
# countries["india"]="delhi"
# print(countries)
# countries["spain"]="cambridge"
# print(countries)
# print(countries.keys())
# if "london" in countries.values():
#     print(countries.values())
# for i in countries:
#     print(i,countries[i])