import tkinter as tk
import mysql.connector

root = tk.Tk()
root.attributes('-fullscreen', True)]\
root.title("Airport Reservation System")

def minimize_window():
    root.iconify()  
def close_window():
    root.destroy()

minimize_button = tk.Button(root, text="Minimize", command=minimize_window)
minimize_button.grid(row=0, column=0, padx=10, pady=10)

close_button = tk.Button(root, text="Close", command=close_window)
close_button.grid(row=0, column=1, padx=10, pady=10)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MSDhoni@07",
    database="airline"
)
cursor = db.cursor()

main_frame = tk.Frame(root)
main_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = tk.Frame(main_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Welcome to the Airport Reservation System")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def book_flight():
    passenger_name = name_entry.get()
    last_name = last_name_entry.get()
    destination = destination_entry.get()
    mobile_no = mobile_no_entry.get()
    address = address_entry.get()
    date = date_entry.get()
    flight_name = flight_name_entry.get()

    query = "INSERT INTO details1 (passenger_name, last_name, destination, mobile_no, address, date, flight_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (passenger_name, last_name, destination, mobile_no, address, date, flight_name)

    try:
        cursor.execute(query, data)
        db.commit()
        result_label.config(text=f"Booking for {passenger_name} to {destination} is confirmed.")
    except mysql.connector.Error as err:
        result_label.config(text=f"Error: {err}")

name_label = tk.Label(main_frame, text="Enter Passenger Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(main_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

last_name_label = tk.Label(main_frame, text="Enter Last Name:")
last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
last_name_entry = tk.Entry(main_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

destination_label = tk.Label(main_frame, text="Enter Destination:")
destination_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
destination_entry = tk.Entry(main_frame)
destination_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

mobile_no_label = tk.Label(main_frame, text="Enter Mobile No:")
mobile_no_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
mobile_no_entry = tk.Entry(main_frame)
mobile_no_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

address_label = tk.Label(main_frame, text="Address:")
address_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
address_entry = tk.Entry(main_frame)
address_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

date_label = tk.Label(main_frame, text="Date:")
date_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
date_entry = tk.Entry(main_frame)
date_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

flight_name_label = tk.Label(main_frame, text="Flight Name:")
flight_name_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")
flight_name_entry = tk.Entry(main_frame)
flight_name_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

flight_id_label = tk.Label(main_frame, text="Enter Flight ID:")
flight_id_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")
flight_id_entry = tk.Entry(main_frame)
flight_id_entry.grid(row=3, column=3, padx=5, pady=5, sticky="ew")


def select_flight():
    destination = destination_entry.get()

    query = "SELECT * FROM details1 WHERE destination = %s"
    data = (destination,)
    cursor.execute(query, data)
    results = cursor.fetchall()

    if results:
        result_label.config(text=f"Found {len(results)} flights to {destination}:")
        for row in results:
            print(row)  
    else:
        result_label.config(text=f"No flights found to {destination}.")

def add_flight():
    passenger_name = name_entry.get()
    destination = destination_entry.get()
    mobile_no = mobile_no_entry.get()
    address = address_entry.get()
    date = date_entry.get()
    flight_name = flight_name_entry.get()

    query = "INSERT INTO details1 (passenger_name, destination, mobile_no, address, date, flight_name) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (passenger_name, destination, mobile_no, address, date, flight_name)
    cursor.execute(query, data)
    db.commit()
    result_label.config(text=f"Booking for {passenger_name} to {destination} added.")

def update_flight():
    flight_id = flight_id_entry.get()
    new_destination = new_destination_entry.get()

    query = "UPDATE details1 SET destination = %s WHERE flight_id = %s"
    data = (new_destination, flight_id)
    cursor.execute(query, data)
    db.commit()
    result_label.config(text=f"Flight {flight_id} updated with new destination: {new_destination}.")

def delete_flight():
    flight_id = flight_id_entry.get()

    query = "DELETE FROM details1 WHERE flight_id = %s"
    data = (flight_id,)
    cursor.execute(query, data)
    db.commit()
    result_label.config(text=f"Flight {flight_id} deleted.")

def reset_fields():
    for entry in input_entries:
        entry.delete(0, tk.END)
    result_label.config(text="")


add_button = tk.Button(main_frame, text="Add Flight", command=add_flight)
add_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

update_button = tk.Button(main_frame, text="Update Flight", command=update_flight)
update_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

delete_button = tk.Button(main_frame, text="Delete Flight", command=delete_flight)
delete_button.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

reset_button = tk.Button(main_frame, text="Reset Fields", command=reset_fields)
reset_button.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

select_button = tk.Button(main_frame, text="Select Flight", command=select_flight)
select_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")


book_button = tk.Button(main_frame, text="Book Flight", command=book_flight)
book_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

new_destination_label = tk.Label(main_frame, text="Enter New Destination:")
new_destination_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
new_destination_entry = tk.Entry(main_frame)
new_destination_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

input_entries = [name_entry, destination_entry, mobile_no_entry, address_entry, date_entry, flight_name_entry]

root.mainloop()

db.close()


