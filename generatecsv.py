import mysql.connector 
import pandas as pd 
 
# Connect to database 
mydb = mysql.connector.connect( 
  host= '127.0.0.1', 
  user= 'root', 
  database = 'movie_recomen'
) 
 
mycursor = mydb.cursor() 
mycursor.execute("""SELECT * FROM  users_movie""") 

 
df = pd.DataFrame(mycursor.fetchall(),columns=["movie_id","name","video","genre_id","language_id","actors","description","director","is_banner","movieDuration","ratedfor","releasedAt","image"]) 
df.to_csv("users_movie.csv", index=False)