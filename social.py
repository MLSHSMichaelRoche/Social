# social

import sqlite3

conn = sqlite3.connect('OscurDeletesShit.db')
cursor = conn.cursor()


def CreateStudetTable() -> None:
    cursor.execute('DROP TABLE IF EXISTS Student')

    studentTable = """CREATE TABLE Student(
        StudentID INTEGER PRIMARY KEY,
        FirstName VARCHAR(30),
        LastName VARCHAR(30)
        );
        """
    cursor.execute(studentTable)
    conn.commit()

def AddStudent(firstName: str, lastName: str) -> None:
    cursor.execute("INSERT INTO Student(FirstName, LastName) VALUES('" + firstName + "','" + lastName + "')")
    conn.commit()

def ListRecords(TableName: str) -> None:
    print('Records in ' + TableName)
    for row in cursor.execute("SELECT * FROM " + TableName):
        print(row)

def DeleteRecord(TableName: str, ID: int) -> None:
    cursor.execute("DELETE FROM " + TableName + " WHERE " + TableName + "ID=" + ID)
    conn.commit()

def UpdateField(TableName: str, ID: int, FieldName: str, NewValue, DataType: str) -> None:
    sql = "UPDATE " + TableName + " SET " + FieldName + "="
    if DataType == 's':
        sql = sql + "'" + NewValue + "'"
    else:
        sql = sql + NewValue
    cursor.execute(sql)
    conn.commit


CreateStudetTable()
AddStudent('Oscar','IsADeletor')
ListRecords('Student')
    # UpdateField('Student', 1, 'LastName', 'IsAlwaysADeletor', 's')
    # ListRecords('Student')
    # DeleteRecord('Student', 1)
    # ListRecords('Student')
