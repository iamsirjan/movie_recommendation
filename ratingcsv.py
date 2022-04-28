import mysql.connector 
import pandas as pd 
 
# Connect to database 
mydb = mysql.connector.connect( 
  host= '127.0.0.1', 
  user= 'root', 
  database = 'movie_recomen'
) 
 
mycursor = mydb.cursor() 
mycursor.execute("""SELECT * FROM  users_rating""") 


 
df = pd.DataFrame(mycursor.fetchall(), columns=["rating_id","rating","comment","movie_id","user_id"]) 
df.to_csv("users_rating.csv", index=False)

