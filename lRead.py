# Last Read Content
lRead_search_entry_frame = customtkinter.CTkFrame(home_frame,width=650,height=50,fg_color="transparent",corner_radius=45)
lRead_search_entry_frame.place(x = 440, y = 10)

lRead_search_entry = customtkinter.CTkEntry(lRead_search_entry_frame,width=550,height=50,fg_color="white",corner_radius=45,placeholder_text="Search Titles...",font=("Quando",20))
lRead_search_entry.place(x = 5,y=5)

lRead_search_entry_button_img = customtkinter.CTkImage((Image.open("icons\searchicon.png")),size=(30,30))
lRead_search_entry_button = customtkinter.CTkButton(lRead_search_entry,text="",image=lRead_search_entry_button_img,width=30,height=30,fg_color="white",corner_radius=0,border_color="white")
lRead_search_entry_button.place(x = 500 , y=5)

lRead_firstShelf_frame = customtkinter.CTkScrollableFrame(home_frame, width=1165 , height=650, fg_color="#B88B68")
lRead_firstShelf_frame.place(x=100, y=70)
