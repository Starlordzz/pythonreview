dic = {"apple": "A fruit that is typically red, green, or yellow.",
       "banana": "A long yellow fruit.",
       "orange": "A round citrus fruit with a tough skin.",
       input("Please enter a fruit name: "): input("Please enter the description of the fruit: ")}
query = input( "Please enter the fruit name you want to know about: " )
if query in dic:
    print( dic[query] )
else:
    print( "Sorry, the fruit is not in the dictionary." )
