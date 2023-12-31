# Filesystem Starter Class

import sqlite3
from sqliteCRUD import SQLiteCrud
from prettytable import PrettyTable


class FileSystem:
    def __init__(self,db_name=None):
        if not db_name:
            self.db_path = "filetable.sqlite"
        else:
            self.db_path = db_name
        self.crud = SQLiteCrud(self.db_path)
        self.cwd = "/home/user"
        self.cwdid = 1

    def __getFileId(self,**kwargs):
        """ Find a file id using current location + name
        """
        pass

    def load_csv(self):
      """
      1,0,rwxr-xr-x,bob,bob,directory,2018-06-23 19:15:35,2018-08-18 09:05:02,1024,linux
      """
      columns = ["id INTEGER PRIMARY KEY", "pid INTEGER","Permissions TEXT","Owner TEXT","_Group TEXT", "Type TEXT", "Created_date TEXT",
                  "Modified_date TEXT","size REAL","Filename TEXT" ]
      self.crud.create_table("filetable", columns)
      
      with open("filesysdata.csv") as f:
        data = f.readlines()
        for row in data:
            row = row.strip().split(",")
        #   row.append(random.randint(500,1000000))
            print(row)
            self.crud.insert_data("filetable",row)    
    
    def list(self,**kwargs):
        """ List the files and folders in current directory
        """


    def chmod(self,**kwargs):
        """ Change the permissions of a file
            1) will need the file / folder id

            2) select permissions from the table where that id exists
            3) 
        Params:
            id (int) :  id of file or folder
            permission (string) : +x -x 777 644

            if its a triple just overwrite or update table 

        Example:
            +x 
            p = 'rw-r-----'
            p[2] = x
            p[5] = x
            p[8] = x


        """
        pass

        def cd(self,**kwargs):
            """
            cd .. = move to parent directory from cwd
            cd ../.. 
            cd /root  (need to find id of that folder, and set swd )
            cd homework/english (involves a check to make sure folder exist)
            """

# Example usage:
if __name__ == "__main__":
    """
    THIS USAGE REALLY JUST SHOWS THE SqliteCRUD CLASS BUT WITH A FILESYSTEM THEME.
    WILL FIX AS WE ADD FUNCTIONALITY INTO THE FileSystem CLASS ABOVE
    SORRY FOR ALL CAPS DIDN'T WANT YOU TO MISS    
    """
    #  # Define table schema
    # table_name = "filesysdata.csv"
    # columns = ["type TEXT","name TEXT","owner TEXT","groop TEXT","id INTEGER PRIMARY KEY", "pid INTEGER",  "created_date TEXT", "modified_date TEXT", "size REAL","permissions TEXT"]
    # # Load table
    # test_data = [
    #     (1, None, 'Folder1', '2023-09-25 10:00:00', '2023-09-25 10:00:00', 0.0, 'folder', 'user1', 'group1', 'rwxr-xr-x'),
    #     (2, 1, 'File1.txt', '2023-09-25 10:15:00', '2023-09-25 10:15:00', 1024.5, 'file', 'user1', 'group1', 'rw-r--r--'),
    #     (3, 1, 'File2.txt', '2023-09-25 10:30:00', '2023-09-25 10:30:00', 512.0, 'file', 'user2', 'group2', 'rw-rw-r--'),
    #     (4, None, 'Folder2', '2023-09-25 11:00:00', '2023-09-25 11:00:00', 0.0, 'folder', 'user2', 'group2', 'rwxr-xr--'),
    #     (5, 4, 'File3.txt', '2023-09-25 11:15:00', '2023-09-25 11:15:00', 2048.75, 'file', 'user3', 'group3', 'rw-r--r--'),
    #     (6, 4, 'File4.txt', '2023-09-25 11:30:00', '2023-09-25 11:30:00', 4096.0, 'file', 'user3', 'group3', 'rw-r--r--'),
    #     (7, None, 'Folder3', '2023-09-25 12:00:00', '2023-09-25 12:00:00', 0.0, 'folder', 'user4', 'group4', 'rwxr-x---'),
    #     (8, 7, 'File5.txt', '2023-09-25 12:15:00', '2023-09-25 12:15:00', 8192.0, 'file', 'user4', 'group4', 'rw-------'),
    #     (9, None, 'Folder4', '2023-09-25 13:00:00', '2023-09-25 13:00:00', 0.0, 'folder', 'user5', 'group5', 'rwxr-xr-x'),
    #     (10, 9, 'File6.txt', '2023-09-25 13:15:00', '2023-09-25 13:15:00', 3072.25, 'file', 'user5', 'group5', 'rwxr-xr--'),
    # ]

    conn = FileSystem()

    conn.load_csv()

    # conn.create_table(table_name, columns)
    # print(conn.describe_table(table_name))

    # for row in test_data:
    #     conn.insert_data(table_name, row)

    # print(conn.formatted_print(table_name))
