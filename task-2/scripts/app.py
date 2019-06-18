# Modules imported 

import mysql.connector, json, os, subprocess, datetime, dropbox
from subprocess import Popen, PIPE

# function - to select data
def selectData(cursor):
    cursor.execute('SELECT * FROM mytable')
    data = json.dumps(cursor.fetchall())
    return (str({data}))

# main-function
if __name__ == '__main__':
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'sql-service',
        'port': '3306',
        'database': 'knights'
    }

    # MySQL Connection - 3306 Port
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    backup =+ '/' + time.strftime('%Y%m%d-%H%M%S')

    os.system('export PATH="/usr/local/opt/mysql-client/bin:$PATH";export LIBRARY_PATH="$LIBRARY_PATH:/usr/local/opt/openssl/lib/"')
    
    try:
        os.stat(backup)
    except:
        os.mkdir(backup)

    filename = 'BACKUP-'+ time.strftime('%Y%m%d-%H%M%S') + '.sql'

    f = open(filename, 'wb')

    p1 = subprocess.Popen(['mysqldump', '-u', 'root', '-p','root', '--add-drop-database', '--databases', 'knights'], stdout=PIPE)
    P2 = subprocess.Popen('gzip', stdin=p1.stdout, stdout=f)
    
    p2.communicate()

    subprocess.call(["ls","-lha"])

    client = dropbox.client.DropboxClient(<auth_token>)
    response = client.put_file(filename, f)

