from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases")
root.geometry('400x400')

# Databases
# Create or connect to a database=
conn = sqlite3.connect('addressBook.db')

# Create a cursor
cursor = conn.cursor()

# Create table

'''#Only done once to create the table

cursor.execute("""CREATE TABLE addresses (
    firstName text,
    lastName text,
    address text,
    city text,
    state text,
    zipcode integer)""")
'''
# Create Submit Function for database
def submit():
    # Create or connect to a database=
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    cursor = conn.cursor()

    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:fname, :lname, :address, :city, :state, :zipcode)", 
                {
                    'fname': fname.get(),
                    'lname': lname.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                }
    )


    # Clear textboxes
    fname.delete(0, END)
    lname.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # Commit changes
    conn.commit()

    # Close  connection
    conn.close()

# Create Query function
def query():
    # Create or connect to a database=
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    #print(records)

    printRecords = ''
    for rec in records:
        printRecords += str(rec[0]) + ' ' + str(rec[1]) + '\t' + str(rec[6]) + '\n'

    queryLabel = Label(root, text=printRecords)
    queryLabel.grid(row=12, column=0, columnspan=2)


    # Commit changes
    conn.commit()

    # Close  connection
    conn.close()

# Create a function to Delete data from database
def delete():
    # Create or connect to a database=
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    cursor = conn.cursor()

    # Delete a record
    cursor.execute("DELETE FROM addresses WHERE oid=" + deleteBox.get())

    # Commit changes
    conn.commit()

    # Close  connection
    conn.close()

# Create a function to Update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Editor")
    editor.geometry('400x400')

    # Create or connect to a database=
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    cursor = conn.cursor()

    recordID = deleteBox.get()
    # Query the database
    cursor.execute("SELECT * FROM addresses WHERE OID=" + recordID)
    records = cursor.fetchall()
    #print(records)

    global fname_e
    global lname_e
    global address_e
    global city_e
    global state_e
    global zipcode_e

    # Create text boxes
    fname_e = Entry(editor, width=30)
    fname_e.grid(row=0, column=1, padx=20, pady=(10, 0))
    lname_e = Entry(editor, width=30)
    lname_e.grid(row=1, column=1)
    address_e = Entry(editor, width=30)
    address_e.grid(row=2, column=1)
    city_e = Entry(editor, width=30)
    city_e.grid(row=3, column=1)
    state_e = Entry(editor, width=30)
    state_e.grid(row=4, column=1)
    zipcode_e = Entry(editor, width=30)
    zipcode_e.grid(row=5, column=1)

    # Create text box labels
    fnamelabel = Label(editor, text="First Name")
    fnamelabel.grid(row=0, column=0, pady=(10, 0))
    lnamelabel = Label(editor, text="Last Name")
    lnamelabel.grid(row=1, column=0)
    addressl = Label(editor, text="Address")
    addressl.grid(row=2, column=0)
    cityl = Label(editor, text="City")
    cityl.grid(row=3, column=0)
    statel = Label(editor, text="State")
    statel.grid(row=4, column=0)
    zipcodel = Label(editor, text="Zipcode")
    zipcodel.grid(row=5, column=0)

    
    # Loop through results
    for rec in records:
        fname_e.insert(0, rec[0])
        lname_e.insert(0, rec[1])
        address_e.insert(0, rec[2])
        city_e.insert(0, rec[3])
        state_e.insert(0, rec[4])
        zipcode_e.insert(0, rec[5])

    # Button to save edited records
    saveBtn = Button(editor, text="Save Record", command=update)
    saveBtn.grid(row=6, column=1, pady=10, padx=10)

    # Commit changes
    conn.commit()

    # Close  connection
    conn.close()

def update():
    # Create or connect to a database=
    conn = sqlite3.connect('addressBook.db')

    # Create a cursor
    cursor = conn.cursor()

    recordID = deleteBox.get()

    cursor.execute("""UPDATE addresses SET 
        firstName = :first,
        lastName = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first': fname_e.get(),
            'last': lname_e.get(),
            'address': address_e.get(),
            'city': city_e.get(),
            'state': state_e.get(),
            'zipcode': zipcode_e.get(),

            'oid': recordID
        })


    # Commit changes
    conn.commit()

    # Close  connection
    conn.close()

    editor.destroy()



# Create text boxes
fname = Entry(root, width=30)
fname.grid(row=0, column=1, padx=20, pady=(10, 0))
lname = Entry(root, width=30)
lname.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
deleteBox = Entry(root, width=30)
deleteBox.grid(row=9, column=1, pady=5)

# Create text box labels
fnamelabel = Label(root, text="First Name")
fnamelabel.grid(row=0, column=0, pady=(10, 0))
lnamelabel = Label(root, text="Last Name")
lnamelabel.grid(row=1, column=0)
addressl = Label(root, text="Address")
addressl.grid(row=2, column=0)
cityl = Label(root, text="City")
cityl.grid(row=3, column=0)
statel = Label(root, text="State")
statel.grid(row=4, column=0)
zipcodel = Label(root, text="Zipcode")
zipcodel.grid(row=5, column=0)
deleteBoxl = Label(root, text="Select Number:")
deleteBoxl.grid(row=9, column=0, pady=5)

# Create Sumbit Button
submitBtn = Button(root, text="Add Record to Database", command=submit)
submitBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
queryBtn = Button(root, text="Show Records", command=query)
queryBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a Delete Button
deleteBtn = Button(root, text="Delete Record", command=delete)
deleteBtn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=129)

# Create an Update Button
editBtn = Button(root, text="Edit Record", command=edit)
editBtn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)



# Commit changes
conn.commit()

# Close  connection
conn.close()

root.mainloop()