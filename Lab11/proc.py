from configparser import ConfigParser

def config(file='database.ini', section='postrgresql'):
    parser = ConfigParser()
    parser.read(file)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('not found')

    return db

commands = {
   'update': """ 
    CREATE OR REPLACE PROCEDURE insertT(id INT, name_input VARCHAR, phone VARCHAR) 
    AS $$ 
    BEGIN 
        IF EXISTS (SELECT * FROM phonebook WHERE name = name_input) THEN 
            UPDATE phonebook SET number = phone WHERE name = name_input; 
        ELSE 
            INSERT INTO phonebook VALUES(id, name_input, phone); 
        END IF; 
    END; $$ 
    LANGUAGE PLPGSQL; 
    
    CALL insertT(%s, %s, %s); 
    """,
    
    'delete': """ 
    CREATE OR REPLACE PROCEDURE deleteT(input VARCHAR) 
    AS $$ 
    BEGIN 
        DELETE FROM phonebook WHERE phonebook.name = input OR phonebook.number = input; 
    END; $$ 
    LANGUAGE PLPGSQL; 
    
    CALL deleteT(%s); 
    """,
}

 