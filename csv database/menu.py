import log_in,one
def menu1():
	entry = int(input( "\nAvailable operations: \n1. Add New "
					"Students\n2."
				"Student Login\n3. Faculty Login\n4. "
					"Proctor Login\n5. Admin View\n"
				"6. Exit\nEnter option: "))
	while entry > 6 or entry <1:
		entry = int(input("Invalid option. Enter again: "))
	if entry == 1:
		one.data_entry()
	if entry == 2:
		log_in.add_student()
    menu1()