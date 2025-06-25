# create database connection
# pip install python-sql-connector
import mysql
import mysql.connector

class MarvelConnector:
    
    databse_connector=mysql.connector.connect(

     host="localhost",
     user="root",
     password="pass@123",
     database="gladiator",
     auth_plugin="my_sql_native_password"

    )
    
    cur=databse_connector.cursor()


    # def insert_marvel(self):
    #     sql="insert into marvel value(%s,%s,%s,%s,%s)"
    #     data=("25","Thor",200,150,200)
    #     self.cur.execute(sql,data)
    #     self.databse_connector.commit()

    def insert_marvel(self, team_marvel_data):
        sql="insert into marvel value(%s,%s,%s,%s,%s)"
        
        for i in range(len(team_marvel_data)):
            data=[i]
            data.append(team_marvel_data[i]['name'])
            data.append(team_marvel_data[i]['height'])
            data.append(team_marvel_data[i]['weight'])
            data.append(team_marvel_data[i]['games_played'])
            self.cur.execute(sql,data)
            self.databse_connector.commit()

    def display_marvel(self):
        fetch_query="select * from marvel"
        self.cur.execute(fetch_query)
        result=self.cur.fetchall()
        for i in result:
            print(i)


# MarvelConnector().insert_marvel()
# MarvelConnector().display_marvel()






