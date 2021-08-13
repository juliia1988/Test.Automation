import pyodbc

server = 'fracvaultstagingdbserver.database.windows.net'
database = 'DR_Testing'
username = 'fracvaultsql'
password = 'Halliburton1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

