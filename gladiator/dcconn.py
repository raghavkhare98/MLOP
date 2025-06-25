import mysql 
import mysql.connector

class DCConnector:

    database_connector = mysql.connector.connect(
        host='localhost',
        user='root',
        password='pass@123',
        database='gladiator'
    )

    cur=database_connector.cursor()

    def insert_dc(self, team_dc_data):

        insert_query = "INSERT INTO dc VALUES(%s, %s, %s, %s, %s)"
        for i in range(len(team_dc_data)):
            data=[i]
            data.append(team_dc_data[i]['name'])
            data.append(team_dc_data[i]['height'])
            data.append(team_dc_data[i]['weight'])
            data.append(team_dc_data[i]['games_played'])
            self.cur.execute(insert_query, data)
            self.database_connector.commit()
    
    def display_dc(self):

        display_query = "SELECT * FROM dc"
        self.cur.execute(display_query)
        result=self.cur.fetchall()
        for i in result:
            print(i)

