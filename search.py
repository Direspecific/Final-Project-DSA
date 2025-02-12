# Search Content
search_advanceSearch_frame = customtkinter.CTkFrame(search_frame,width=700,height=1080,fg_color="#433F3D",corner_radius=0)
search_advanceSearch_frame.place(x = (window_width/2)-710, y = 0)

search_library_frame_inner = customtkinter.CTkFrame(search_frame,width=1509,height=1122,fg_color="#B88B68",corner_radius=0)
search_library_frame_inner.place(x = 600, y = 0)
        
search_advanceSearch_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 35), text_color="white", width=450, height=69, fg_color="transparent", corner_radius=0, text="Advanced Search")
search_advanceSearch_label.place(x=180, y=20)

search_title_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Title")
search_title_label.place(x=220, y=100)
        
search_genre_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_genre_entry.place(x = 300,y = 100)

search_genre_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Genre")
search_genre_label.place(x=220, y=150)
        
search_genre_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_genre_entry.place(x = 300,y = 150)

search_author_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Author")
search_author_label.place(x=220, y=200)
        
search_author_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_author_entry.place(x = 300,y = 200)

search_theme_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", .00002 * (window_width * window_height)), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Theme")
search_theme_label.place(x=220, y=250)
        
search_theme_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_theme_entry.place(x = 300,y = 250)
        
search_rating_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Rating")
search_rating_label.place(x=220, y=300)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_rating_entry.place(x = 300,y = 300)

search_keyword_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Keyword")
search_keyword_label.place(x=210, y=350)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_rating_entry.place(x = 300,y = 350)

search_publishDate_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.E, font=("Quando",20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Publish Date")
search_publishDate_label.place(x=180, y=400)
        
search_publishDate_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20),border_width=0)
search_publishDate_entry.place(x = 300,y = 400)

search_resetFilter_button = customtkinter.CTkButton(search_advanceSearch_frame,width=150,height=40,font=("Quando",20),fg_color="#c0c0c0",text_color="black" ,hover_color="dark grey" ,corner_radius=60,text="Reset")
search_resetFilter_button.place(x = 150, y = 450)   

search_search_button = customtkinter.CTkButton(search_advanceSearch_frame,width=150,height=40,font=("Quando",20),fg_color="#C8DF8C",text_color="black" ,hover_color="#8c9c62" ,corner_radius=60,text="Search")
search_search_button.place(x = 330, y = 450)
