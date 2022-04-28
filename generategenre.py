import mysql.connector 
import pandas as pd 
 
# Connect to database 
mydb = mysql.connector.connect( 
  host= '127.0.0.1', 
  user= 'root', 
  database = 'movie_recomen'
) 
 
mycursor = mydb.cursor() 
mycursor.execute("""SELECT * FROM  users_genre""") 


 
df = pd.DataFrame(mycursor.fetchall(), columns=["genre_id","genre"]) 
df.to_csv("users_genre.csv", index=False)

