import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox, simpledialog

# Create a database connection
conn = sqlite3.connect('LibraryDataBase1.db')
c = conn.cursor()

# Create a table for the student details
c.execute('CREATE TABLE IF NOT EXISTS library (BK_NAME TEXT, BK_ID TEXT PRIMARY KEY NOT NULL, AUTHOR_NAME TEXT, BK_STATUS TEXT, Student_card_id TEXT)')
conn.commit()

def add():
    def submit():
        #store values into variable
        bk_name_entry =(bk_name_input.get())
        bk_id_entry =(bk_id_input.get())
        bk_author_entry=(author_name_input.get())
        bk_status_entry=(bk_status_input.get())

        # Add the values to the library table
        c.execute("INSERT INTO library (BK_NAME,BK_ID,AUTHOR_NAME,BK_STATUS)VALUES (?, ?, ?, ?)",(bk_name_entry,bk_id_entry,bk_author_entry,bk_status_entry))
        conn.commit()
        
        # Clear the input fields
        bk_name_input.delete(0, tk.END)
        bk_id_input.delete(0, tk.END)
        author_name_input.delete(0, tk.END)
        bk_status_input.delete(0, tk.END)

    root2=Toplevel(root)
    bk_name_label = tk.Label(root2, text="Book name:")
    bk_name_label.grid(row=0, column=0, padx=10, pady=10)
    bk_name_input = tk.Entry(root2)
    bk_name_input.grid(row=0, column=1, padx=10, pady=10)

    bk_id_label = tk.Label(root2, text="Book id:")
    bk_id_label.grid(row=1, column=0, padx=10, pady=10)
    bk_id_input = tk.Entry(root2)
    bk_id_input.grid(row=1, column=1, padx=10, pady=10)

    author_name_label = tk.Label(root2, text="Author name:")
    author_name_label.grid(row=2, column=0, padx=10, pady=10)
    author_name_input = tk.Entry(root2)
    author_name_input.grid(row=2, column=1, padx=10, pady=10)

    bk_status_label = tk.Label(root2, text="Book status:")
    bk_status_label.grid(row=3, column=0, padx=10, pady=10)
    bk_status_input = tk.Entry(root2)
    bk_status_input.grid(row=3, column=1, padx=10, pady=10)

    summit_button = tk.Button(root2, text="Submit", command=submit)
    summit_button.grid(row=7, column=0, padx=10, pady=10)
    
    root2.configure(bd=2, relief="groove")

def display():
    root4=Toplevel(root)
    # Get all values from the library table
    c.execute("SELECT * FROM library")
    lib = c.fetchall()

    # Display values in display frame
    bk_name_header = tk.Label(root4, text="Book Name", font=("Arial", 12, "bold"))
    bk_name_header.grid(row=0, column=0, padx=10, pady=5)

    bk_id_header = tk.Label(root4, text="Book Id", font=("Arial", 12, "bold"))
    bk_id_header.grid(row=0, column=1, padx=10, pady=5)
    
    bk_author_header = tk.Label(root4, text="Author Name", font=("Arial", 12, "bold"))
    bk_author_header.grid(row=0, column=2, padx=10, pady=5)

    bk_status_header = tk.Label(root4, text="Book status", font=("Arial", 12, "bold"))
    bk_status_header.grid(row=0, column=3, padx=10, pady=5)

    stu_id_header=tk.Label(root4, text="Book received person id", font=("Arial", 12, "bold"))
    stu_id_header.grid(row=0, column=4, padx=10, pady=5)

   
    for i, library in enumerate(lib):
        name_label = tk.Label(root4, text=library[0], font=("Arial", 12))
        name_label.grid(row=i+1, column=0, padx=10, pady=5)

        id_label = tk.Label(root4, text=library[1], font=("Arial", 12))
        id_label.grid(row=i+1, column=1, padx=10, pady=5)

        author_label = tk.Label(root4, text=library[2], font=("Arial", 12))
        author_label.grid(row=i+1, column=2, padx=10, pady=5)

        status_label = tk.Label(root4, text=library[3], font=("Arial", 12))
        status_label.grid(row=i+1, column=3, padx=10, pady=5)
        
        stu_id_label = tk.Label(root4, text=library[4], font=("Arial", 12))
        stu_id_label.grid(row=i+1, column=4, padx=10, pady=5)
        
        root4.configure(bd=2, relief="groove")

def issue():
    def Issue_button():
        #store values into variable
        student=(student_id_input.get())
        book=(book_id_input.get())
        
        #Add the values to the library table
        cmd = "UPDATE library set Student_card_id="+student+", BK_STATUS='Issued' WHERE BK_ID="+book+";"
        c.execute(cmd)
        conn.commit()
        
        # Clear the input fields
        student_id_input.delete(0, tk.END)
        book_id_input.delete(0, tk.END)
                
    root3=Toplevel(root)
    student_id_label = tk.Label(root3, text="Enter the person id:")
    student_id_label.grid(row=1, column=0, padx=10, pady=10)
    student_id_input = tk.Entry(root3)
    student_id_input.grid(row=1, column=1, padx=10, pady=10)

    book_id_label = tk.Label(root3, text="Book id:")
    book_id_label.grid(row=2, column=0, padx=10, pady=10)
    book_id_input = tk.Entry(root3)
    book_id_input.grid(row=2, column=1, padx=10, pady=10)

    Issue_button = tk.Button(root3, text="Issue", command=Issue_button)
    Issue_button.grid(row=7, column=0, padx=10, pady=10)
    
    root3.configure(bd=2, relief="groove")

def returns():
    # Get the ID of the student 
    student_id = int( simpledialog.askinteger("Library Management System", "Enter the received person Id:"))

    # update DB
    c.execute("UPDATE library set Student_card_id='', BK_STATUS='Available' WHERE Student_card_id=?", (student_id,))
    conn.commit()
    
def delete():
    # GET the book id from user for delete the book
    del_id = simpledialog.askinteger("Library Management System", "Enter the Book Id to delete that book from DB:")

    #DELETE
    c.execute("DELETE FROM library WHERE BK_ID=?", (del_id,))
    conn.commit()

# Create the GUI
root = tk.Tk()
root.title("Library Management System")
root.geometry("320x300")
main=tk.Label(root, text="WELCOME TO LIBRARY",font=("Franklin Gothic Heavy", 12))
main.grid(row=0, column=0, padx=60, pady=10)

#ADD BOOKS
add_button = tk.Button(root, text="Add books", command=add)
add_button.grid(row=1, column=0, padx=20, pady=10 )

#Display
display_button = tk.Button(root, text="Display", command=display)
display_button.grid(row=2, column=0, padx=20, pady=10)

#BOOK ISSUE
issue_button = tk.Button(root, text="Issue book", command=issue)
issue_button.grid(row=3, column=0, padx=20, pady=10)

#Return book
return_button = tk.Button(root, text="Return book", command=returns)
return_button.grid(row=4, column=0, padx=30, pady=10)

#DELETE
delete_button = tk.Button(root, text="Delete books", command=delete)
delete_button.grid(row=5, column=0, padx=20, pady=10 )

student_frame = tk.Frame(root)
student_frame.grid(row=9, column=0, )

root.mainloop()

#Close the database connection
conn.close()
