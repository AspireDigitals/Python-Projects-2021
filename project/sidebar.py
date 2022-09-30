sidebar_frame = Frame(main, bg="black", width=200)
sidebar_frame.grid(row=1, column=0)



reg_btn = Button(sidebar_frame, text="Register", width=30, font=("Helvetica", 15))
reg_btn.grid(row=1, column=0)

display_btn = Button(sidebar_frame, text="Display Entries", width=30, font=("Helvetica", 15))
display_btn.grid(row=2, column=0)

save_btn = Button(sidebar_frame, text="Save Entries", width=30, font=("Helvetica", 15))
save_btn.grid(row=3, column=0)

update_btn = Button(sidebar_frame, text="Update Entries", width=30, font=("Helvetica", 15))
update_btn.grid(row=4, column=0)

delete_btn = Button(sidebar_frame, text="Delete Entries", width=30, font=("Helvetica", 15))
delete_btn.grid(row=5, column=0)

read_btn = Button(sidebar_frame, text="Read Entries", width=30, font=("Helvetica", 15))
read_btn.grid(row=6, column=0)


