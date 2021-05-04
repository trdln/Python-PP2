import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
    
def create_tables(username,password):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        )
    command2 = (
        """INSERT INTO users VALUES(%s,%s);
        """
    )
    command3 = (
        "SELECT username,password FROM users;"
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        
        cur.execute(commands)

        cur.execute(command2, (username,password))
        cur.execute(command3)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables(input(),input())
    
