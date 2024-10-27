from tkinter import *
import random as rd
root = Tk()
root.config(bg='black')
root.title("Quiz Application")

# Quiz data
questions_kid = [
    "Which month of the year has the least number of days?",
    "Which is the world’s largest flower?",
    "How many bones does an Adult human have?",
    "How many grams are there in 1 kilogram?",
    "What color symbolizes peace?",
    "Which is the nearest star to planet earth?", 
    "Which is the largest ocean in the world?",
    "What is the name of Nobita's mother?",
    "How many players are there in a cricket team?", 
    "Which of these channels telecasts the Shinchan show?",
    "What is the position of Earth in our Solar system?",
    "How many digits are there in Mathematics?",
    "What is 2+2(3+7)?",
    "Who is the father of mathematics?",
    "How many bananas are there in a dozen bananas?"
]

option_A_kid = [
    "April", "Lotus", "206", "1000", "orange", "sun", "Indian Ocean", "Honekawa", 
    "12", "Pogo", "second", "10,000", "15", "Archimedes", "12"
]

option_B_kid = [
    "February", "Sunflower", "217", "2000", "pink", "Jupiter", "Pacific Ocean", "Tamako Nobi", 
    "20", "Cartoon Network", "third", "100,000", "22", "Aryabhatta", "17"
]

option_C_kid = [
    "March", "Rafflesia", "309", "1001", "green", "Pluto", "Nile", "Dorami", 
    "11", "Nick", "fifth", "infinite", "20", "Thales of Miletus", "20"
]

option_D_kid = [
    "October", "Tulip", "409", "3000", "white", "moon", "Atlantic Ocean", "Suzuka", 
    "10", "Hungama", "seventh", "300,000,000", "40", "Terence Tao", "15"
]

answers_kid = [
    "February", "Rafflesia", "206", "1000", "white", "sun", "Pacific Ocean", "Tamako Nobi", 
    "11", "Hungama", "third", "infinite", "22", "Archimedes", "12"
]

extra_question_kids=["what do you call a group of wolves?",
        "what was the name of simba's mother?",
        "how many 'wonders of the world' are there?",
        "what's the closest planet to the sun?",
        "which blood cells fight the diseases?"
        ]
extra_optionA_kids=["A Pack",
            "zazu",
            "seven",
            "mercury",
            "white blood cells"]
extra_optionB_kids=["pride",
            "pumbaa",
            "eight",
            "earth",
            "red blood cells"]
extra_optionC_kids=["mob",
            "trival",
            "six",
            "jupiter",
            "Lymph"]
extra_optionD_kids=["colony",
            "sarabi",
            "eleven",
            "venus",
            "plasma"]
extra_answers_kids=["A Pack",
                    "sarabi",
                    "seven",
                    "mercury",
                    "white blood cells"]

questions_Teen = [
    "What is the name of the hottest planet in the solar system?",
    "What is the name of the planet with the longest day?",
    "Who heads RBI?",
    "What is the largest lake in India?",
    "What is the richest state in India?",
    "Name of the largest ocean in the world is?",
    "What is the name of the coldest planet in the world?",
    "Which gas is most abundant in Earth’s atmosphere?",
    "What is the protective layer of gas surrounding Earth?",
    "The force of gravity is attracted to what?",
    "Bahubali festival is related to?",
    "The International Literacy Day is observed on?",
    "Who is the author of the epic Meghdoot?",
    "Which of the following is observed as Sports Day every year?",
    "World Health Day is observed on?"
]

option_A_Teen = [
    "Venus", "Venus", "Prime minister", "Dal lake", "Bihar", "Pacific ocean", "Neptune", 
    "Nitrogen", "Oxygen", "Magnetic field", "Islam", "Nov 28", "Valmiki", "26th July", "Mar 6"
]

option_B_Teen = [
    "Mercury", "Jupiter", "Governor", "Vembanad", "Maharashtra", "Atlantic ocean", "Uranus", 
    "Oxygen", "Atmosphere", "Mass", "Buddhism", "Sep 22", "Banabhatta", "29th August", "Mar 15"
]

option_C_Teen = [
    "Mars", "Uranus", "President", "Nile", "Uttar Pradesh", "Indian ocean", "Saturn", 
    "Carbon dioxide", "Ozone", "Radiation", "Hinduism", "Sep 8", "Vishakadatta", "2nd October", "Apr 7"
]

option_D_Teen = [
    "Jupiter", "Neptune", "Home minister", "Wular lake", "Mumbai", "Arctic", "Jupiter", 
    "Methane", "Nitrogen", "Electric field", "Jainism", "May 2", "Kalidas", "29th August", "April 28"
]

answers_Teen = [
    "Venus", "Venus", "Governor", "Vembanad", "Maharashtra", "Pacific ocean", "Uranus", 
    "Nitrogen", "Ozone", "Mass", "Jainism", "Sep 8", "Kalidas", "29th August", "Apr 7"
]

extra_question_Teen=['An average human takes how many breaths in a day?',
                     'What is the study of fossils called?',
                     "Which planet is often referred to as Earth’s “sister planet” due to its similar size and composition?",
                     'What sport is known for its iconic phrase “Love-15”?',
                     'What is the diameter of a basketball hoop?'
                     ]
extra_optionA_Teen=['23000','Seismology','Venus','Volley Ball','10 inches']
extra_optionB_Teen=['25000','Paleontology','Mars','Badminton','22 inches']
extra_optionC_Teen=['50000','ornithology','Jupiter','Football','15 inches']
extra_optionD_Teen=['15003','entomology','Mercury','Tennis','18 inches']
extra_answers_Teen=['23000','Paleontology','Venus','Tennis','18 inches']

questions_Adult = [
    "What is the capital of Australia?",
    "Which river flows through marble stones in Madhya Pradesh?",
    "In which year was the first ever IPL match played?",
    "Where are the WHO headquarters located?",
    "Which of these Indian cities is the capital of more than one state?",
    "What was the name of the first primate launched into space?",
    "Which of these films won the Academy Award for Best Picture in 2021?",
    "How many official languages does New Zealand have?",
    "Which of the following places is NOT officially recognised as a country?",
    "Which social networking company made Parag Agrawal its CEO in 2021?",
    "How many religions are there in India?",
    "When is the National Hindi Diwas celebrated?",
    "How many states are there in India?",
    "Who wrote Vande Mataram?",
    "Which of the following musical instruments is NOT of foreign origin?"
]

option_A_Adult = [
    "Sydney", "Narmada", "2006", "Paris, France", "Bhopal", "George", "Parasite", 
    "One", "Moldova", "Instagram", "6", "13 September", "28", "Sarat Chandra Chattopadhyay", "Tabla"
]

option_B_Adult = [
    "Melbourne", "Shipra", "2007", "Monaco", "Imphal", "Albert", "Nomadland", 
    "Two", "Transnistria", "Twitter", "7", "14 September", "27", "Rabindranath Tagore", "Flute"
]

option_C_Adult = [
    "Brisbane", "Ganga", "2008", "Austin, Texas", "Hyderabad", "Harrison", "Minari", 
    "Three", "Romania", "Tumblr", "8", "14 July", "35", "Bankim Chandra Chatterjee", "Sitar"
]

option_D_Adult = [
    "Canberra", "Brahmaputra", "2009", "Geneva, Switzerland", "Kavaratti", "John", "Sound of Metal", 
    "Four", "Belarus", "Reddit", "9", "August", "29", "Ishwar Chandra Vidyasagar", "Violin"
]

answers_Adult = [
    "Canberra", "Narmada", "2008", "Geneva, Switzerland", "Hyderabad", "Albert", "Nomadland", 
    "Three", "Transnistria", "Twitter", "6", "14 September", "28", "Bankim Chandra Chatterjee", "Sitar"
]

extra_question_Adult = [
    "The International Literacy Day is observed on",
    "The language of Lakshadweep. a Union Territory of India, is",
    "Bahubali festival is related to",
    "Which day is observed as the World Standards  Day?",
    "Who is the author of the epic 'Meghdoot'?"
    
]

extra_optionA_Adult = [
    "8 September",
    "Tamil",
    "Islam",
    "26 June",
    "Vishakadatta"
]

extra_optionB_Adult = [
    "24 November",
    "Hindi",
    "Hinduism",
    "14 Octuber",
    "Valmiki"
    
]

extra_optionC_Adult = [
    "2 may ",
    "Malayalam",
    "Buddhism",
    "15 November",
    "Banabhatta"
    
]

extra_optionD_Adult = [
    "20 july",
    "Telugu",
    "Jainism",
    "2 july",
    "Kalidas"

]

extra_answers_Adult = ["8 September", "Malayalam", "Jainism", "14 Octuber", "Kalidas"]


capture_question=''
capture_index=''
current_question_index = 0
current_category = "kid"  # to keep track of the current category
flip_condition=False
def start_quiz_kid():
    global current_category
    current_category = "kid"
    start_frame.pack_forget()
    quiz_frame.pack(fill='both', expand=True)
    update_question()

def start_quiz_teen():
    global current_category
    current_category = "teen"
    start_frame.pack_forget()
    quiz_frame.pack(fill='both', expand=True)
    update_question()

def start_quiz_Adult():
    global current_category
    current_category = "Adult"
    start_frame.pack_forget()
    quiz_frame.pack(fill='both', expand=True)
    update_question()

def check_answer(selected_option):
    global current_question_index
    
    if current_category == "kid":
        correct_answer = answers_kid[current_question_index]
    elif current_category == "teen":
        correct_answer = answers_Teen[current_question_index]
    elif current_category == "Adult":
        correct_answer = answers_Adult[current_question_index]

    if selected_option == correct_answer:
        print("Correct!")
        current_question_index += 1
        if current_category == "kid" and current_question_index < len(questions_kid):
            update_question()
        elif current_category == "teen" and current_question_index < len(questions_Teen):
            update_question()
        elif current_category == "Adult" and current_question_index < len(questions_Adult):
            update_question()
        else:
            def winning_screen():
                root3=Toplevel()
                root3.overrideredirect(True)
                root3.geometry('528x442+250+70')
                frame2=Frame(root3,highlightbackground='blue',highlightthickness='5',bg='black')
                frame2.pack()
                win_label=Label(frame2,image=winning_img,bg='black')
                win_label.pack()
                close_button=Button(frame2,text='Close',command=closep,bg='black',fg='white',font=('Arial',10,'bold'))
                close_button.place(x=240,y=400)
                root3.mainloop()
            
            Textarea.delete('1.0', END)
            Textarea.insert(END, "Quiz Completed!")
            score.config(image=scoreimg[current_question_index])
            def closep():
                root.destroy()
            disable_buttons()

            winning_screen()
    else:
        def closep():
            root.destroy()
            
        def tryp():
            global current_question_index,flip_condition
            current_question_index=0
            if current_category=='kid':
                if flip_condition==True:
                    questions_kid[capture_index]=capture_question
                    option_A_kid[capture_index]=capture_option_A_kid
                    option_B_kid[capture_index]=capture_option_B_kid
                    option_C_kid[capture_index]=capture_option_C_kid
                    option_D_kid[capture_index]=capture_option_D_kid
                    answers_kid[capture_index]=capture_answers_kid
                    flip_condition=False

                root2.destroy()
                Textarea.delete(1.0,END)

                Textarea.insert(END,questions_kid[current_question_index])

                optionAbutton.config(text=option_A_kid[current_question_index],cursor='hand2',command=click1)
                optionbbutton.config(text=option_B_kid[current_question_index],cursor='hand2',command=click2)
                optioncbutton.config(text=option_C_kid[current_question_index],cursor='hand2',command=click3)
                optionDbutton.config(text=option_D_kid[current_question_index],cursor='hand2',command=click4)
                
            if current_category=='teen':
                if flip_condition==True:
                    questions_Teen[capture_index]=capture_question
                    option_A_Teen[capture_index]=capture_option_A_Teen
                    option_B_Teen[capture_index]=capture_option_B_Teen
                    option_C_Teen[capture_index]=capture_option_C_Teen
                    option_D_Teen[capture_index]=capture_option_D_Teen
                    answers_Teen[capture_index]=capture_answers_Teen
                    flip_condition=False

                root2.destroy()
                Textarea.delete(1.0,END)

                Textarea.insert(END,questions_Teen[current_question_index])

                optionAbutton.config(text=option_A_Teen[current_question_index],cursor='hand2',command=click1)
                optionbbutton.config(text=option_B_Teen[current_question_index],cursor='hand2',command=click2)
                optioncbutton.config(text=option_C_Teen[current_question_index],cursor='hand2',command=click3)
                optionDbutton.config(text=option_D_Teen[current_question_index],cursor='hand2',command=click4)
          
            if current_category=='Adult':
                if flip_condition==True:
                    questions_Adult[capture_index]=capture_question
                    option_A_Adult[capture_index]=capture_option_A_Adult
                    option_B_Adult[capture_index]=capture_option_B_Adult
                    option_C_Adult[capture_index]=capture_option_C_Adult
                    option_D_Adult[capture_index]=capture_option_D_Adult
                    answers_Adult[capture_index]=capture_answers_Adult
                    flip_condition=False

                root2.destroy()
                Textarea.delete(1.0,END)

                Textarea.insert(END,questions_Adult[current_question_index])

                optionAbutton.config(text=option_A_Adult[current_question_index],cursor='hand2',command=click1)
                optionbbutton.config(text=option_B_Adult[current_question_index],cursor='hand2',command=click2)
                optioncbutton.config(text=option_C_Adult[current_question_index],cursor='hand2',command=click3)
                optionDbutton.config(text=option_D_Adult[current_question_index],cursor='hand2',command=click4)

            score.config(image=scoreimg[current_question_index])
            lifeline50button.config(image=lifeline50img,command=fifty_fifty)
            flipTQbutton.config(image=flipTQimg,command=flip)
            print(capture_question,capture_index)





        root2=Toplevel()
        root2.overrideredirect(True)

        root2.config(bg='black')
        root2.geometry('287x400+250+70')
        frame=Frame(root2,highlightbackground='blue',highlightthickness='5',height=500,width=400,bg='black')
        frame.pack()
        root2.title('You lose')

        imglabel=Label(frame,image=centerimg,bd=0)
        imglabel.pack(pady=30)

        loselabel=Label(frame,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
        loselabel.pack()

        tryagain=Button(frame,text='Try again',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=tryp)
        tryagain.pack()

        close=Button(frame,text='close',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=closep)
        close.pack()

        root2.mainloop()

def update_question():
    Textarea.delete('1.0', END)
    if current_category == "kid":
        Textarea.insert(END, questions_kid[current_question_index])
        optionAbutton.config(text=option_A_kid[current_question_index],cursor='hand2',command=click1)
        optionbbutton.config(text=option_B_kid[current_question_index],cursor='hand2',command=click2)
        optioncbutton.config(text=option_C_kid[current_question_index],cursor='hand2',command=click3)
        optionDbutton.config(text=option_D_kid[current_question_index],cursor='hand2',command=click4)
        score.config(image=scoreimg[current_question_index])
        
    elif current_category == "teen":
        Textarea.insert(END, questions_Teen[current_question_index])
        optionAbutton.config(text=option_A_Teen[current_question_index],cursor='hand2',command=click1)
        optionbbutton.config(text=option_B_Teen[current_question_index],cursor='hand2',command=click2)
        optioncbutton.config(text=option_C_Teen[current_question_index],cursor='hand2',command=click3)
        optionDbutton.config(text=option_D_Teen[current_question_index],cursor='hand2',command=click4)
        score.config(image=scoreimg[current_question_index])
    elif current_category == "Adult":
        Textarea.insert(END, questions_Adult[current_question_index])
        optionAbutton.config(text=option_A_Adult[current_question_index],cursor='hand2',command=click1)
        optionbbutton.config(text=option_B_Adult[current_question_index],cursor='hand2',command=click2)
        optioncbutton.config(text=option_C_Adult[current_question_index],cursor='hand2',command=click3)
        optionDbutton.config(text=option_D_Adult[current_question_index],cursor='hand2',command=click4)
        score.config(image=scoreimg[current_question_index])

def disable_buttons():
    optionAbutton.config(state=DISABLED)
    optionbbutton.config(state=DISABLED)
    optioncbutton.config(state=DISABLED)
    optionDbutton.config(state=DISABLED)

def click1(): 
    selected_option = optionAbutton['text']
    check_answer(selected_option)

def click2(): 
    selected_option = optionbbutton['text']
    check_answer(selected_option)

def click3(): 
    selected_option = optioncbutton['text']
    check_answer(selected_option)

def click4(): 
    selected_option = optionDbutton['text']
    check_answer(selected_option)

# Create frames for different sections
start_frame = Frame(root,bg='black')
quiz_frame = Frame(root,bg='black')
#####################################################################################################################
def fifty_fifty():
    if current_category == "kid":
        ans=answers_kid[current_question_index]
        rmove=0
        l=[1,2,3,4]
        if option_A_kid[current_question_index]==ans:
            rmove=1
        elif option_B_kid[current_question_index]==ans:
            rmove=2
        elif option_C_kid[current_question_index]==ans:
            rmove=3
        elif option_D_kid[current_question_index]==ans:
            rmove=4
        l.remove(rmove)
        Random_choice=rd.choice(l)
        l.remove(Random_choice)
        for i in l:
            if i==1:
                optionAbutton.config(text='',command=0,cursor='')
            if i==2:
                optionbbutton.config(text='',command=0,cursor='')
            if i==3:
                optioncbutton.config(text='',command=0,cursor='')
            if i==4:
                optionDbutton.config(text='',command=0,cursor='')
        
    elif current_category == "teen":
        ans=answers_Teen[current_question_index]
        rmove=0
        l=[1,2,3,4]
        if option_A_Teen[current_question_index]==ans:
            rmove=1
        elif option_B_Teen[current_question_index]==ans:
            rmove=2
        elif option_C_Teen[current_question_index]==ans:
            rmove=3
        elif option_D_Teen[current_question_index]==ans:
            rmove=4
        l.remove(rmove)
        Random_choice=rd.choice(l)
        l.remove(Random_choice)
        for i in l:
            if i==1:
                optionAbutton.config(text='',command=0,cursor='')
            if i==2:
                optionbbutton.config(text='',command=0,cursor='')
            if i==3:
                optioncbutton.config(text='',command=0,cursor='')
            if i==4:
                optionDbutton.config(text='',command=0,cursor='')
    elif current_category == "Adult":
        ans=answers_Adult[current_question_index]
        rmove=0
        l=[1,2,3,4]
        if option_A_Adult[current_question_index]==ans:
            rmove=1
        elif option_B_Adult[current_question_index]==ans:
            rmove=2
        elif option_C_Adult[current_question_index]==ans:
            rmove=3
        elif option_D_Adult[current_question_index]==ans:
            rmove=4
        l.remove(rmove)
        Random_choice=rd.choice(l)
        l.remove(Random_choice)
        for i in l:
            if i==1:
                optionAbutton.config(text='',command=0,cursor='')
            if i==2:
                optionbbutton.config(text='',command=0,cursor='')
            if i==3:
                optioncbutton.config(text='',command=0,cursor='')
            if i==4:
                optionDbutton.config(text='',command=0,cursor='')
    lifeline50button.config(command=0,image=lifeline50button_crossimg)

def flip():
    global capture_question,flip_condition
    global capture_index,capture_option_A_kid,capture_option_B_kid,capture_option_C_kid,capture_option_D_kid,capture_answers_kid
    global capture_index,capture_option_A_Teen,capture_option_B_Teen,capture_option_C_Teen,capture_option_D_Teen,capture_answers_Teen
    global capture_index,capture_option_A_Adult,capture_option_B_Adult,capture_option_C_Adult,capture_option_D_Adult,capture_answers_Adult
    flip_condition=True

    if current_category=='kid':
        capture_question=questions_kid[current_question_index]
        capture_index=current_question_index
        capture_answers_kid=answers_kid[current_question_index]
        capture_option_A_kid=option_A_kid[current_question_index]
        capture_option_B_kid=option_B_kid[current_question_index]
        capture_option_C_kid=option_C_kid[current_question_index]
        capture_option_D_kid=option_D_kid[current_question_index]
        random_question=rd.choice(extra_question_kids)
        random_question_idex=extra_question_kids.index(random_question)
        questions_kid[current_question_index]=random_question
        option_A_kid[current_question_index]=extra_optionA_kids[random_question_idex]
        option_B_kid[current_question_index]=extra_optionB_kids[random_question_idex]
        option_C_kid[current_question_index]=extra_optionC_kids[random_question_idex]
        option_D_kid[current_question_index]=extra_optionD_kids[random_question_idex]
        answers_kid[current_question_index]=extra_answers_kids[random_question_idex]
        print(answers_kid)
        Textarea.delete(1.0,END)
        Textarea.insert(END,random_question)

        optionAbutton.config(text=extra_optionA_kids[random_question_idex])
        optionbbutton.config(text=extra_optionB_kids[random_question_idex])
        optioncbutton.config(text=extra_optionC_kids[random_question_idex])
        optionDbutton.config(text=extra_optionD_kids[random_question_idex])

    
    elif current_category=='teen':
        
        capture_question=questions_Teen[current_question_index]
        capture_index=current_question_index
        capture_answers_Teen=answers_Teen[current_question_index]
        capture_option_A_Teen=option_A_Teen[current_question_index]
        capture_option_B_Teen=option_B_Teen[current_question_index]
        capture_option_C_Teen=option_C_Teen[current_question_index]
        capture_option_D_Teen=option_D_Teen[current_question_index]
        random_question=rd.choice(extra_question_Teen)
        random_question_idex=extra_question_Teen.index(random_question)
        questions_Teen[current_question_index]=random_question
        option_A_Teen[current_question_index]=extra_optionA_Teen[random_question_idex]
        option_B_Teen[current_question_index]=extra_optionB_Teen[random_question_idex]
        option_C_Teen[current_question_index]=extra_optionC_Teen[random_question_idex]
        option_D_Teen[current_question_index]=extra_optionD_Teen[random_question_idex]
        answers_Teen[current_question_index]=extra_answers_Teen[random_question_idex]
        print(answers_Teen)
        Textarea.delete(1.0,END)
        Textarea.insert(END,random_question)

        optionAbutton.config(text=extra_optionA_Teen[random_question_idex])
        optionbbutton.config(text=extra_optionB_Teen[random_question_idex])
        optioncbutton.config(text=extra_optionC_Teen[random_question_idex])
        optionDbutton.config(text=extra_optionD_Teen[random_question_idex])


    elif current_category=='Adult':
        
        capture_question=questions_Adult[current_question_index]
        capture_index=current_question_index
        capture_answers_Adult=answers_Adult[current_question_index]
        capture_option_A_Adult=option_A_Adult[current_question_index]
        capture_option_B_Adult=option_B_Adult[current_question_index]
        capture_option_C_Adult=option_C_Adult[current_question_index]
        capture_option_D_Adult=option_D_Adult[current_question_index]
        random_question=rd.choice(extra_question_Adult)
        random_question_idex=extra_question_Adult.index(random_question)
        questions_Adult[current_question_index]=random_question
        option_A_Adult[current_question_index]=extra_optionA_Adult[random_question_idex]
        option_B_Adult[current_question_index]=extra_optionB_Adult[random_question_idex]
        option_C_Adult[current_question_index]=extra_optionC_Adult[random_question_idex]
        option_D_Adult[current_question_index]=extra_optionD_Adult[random_question_idex]
        answers_Adult[current_question_index]=extra_answers_Adult[random_question_idex]
        print(answers_Adult)
        Textarea.delete(1.0,END)
        Textarea.insert(END,random_question)

        optionAbutton.config(text=extra_optionA_Adult[random_question_idex])
        optionbbutton.config(text=extra_optionB_Adult[random_question_idex])
        optioncbutton.config(text=extra_optionC_Adult[random_question_idex])
        optionDbutton.config(text=extra_optionD_Adult[random_question_idex])
    flipTQbutton.config(command=0,image=flipTQcrossimg)








# Start screen
start_label = Label(start_frame, text="Welcome to the Quiz!", font=('arial', 50, 'bold'), bg='black', fg='white')
start_label.pack(pady=100)

start_button_kid = Button(start_frame, text="Kid", font=('arial', 30, 'bold'), bg='black', fg='white', command=start_quiz_kid)
start_button_kid.place(x=400,y=200+100)

start_button_teen = Button(start_frame, text="Teen", font=('arial', 30, 'bold'), bg='black', fg='white', command=start_quiz_teen)
start_button_teen.place(y=300,x=600)

start_button_Adult = Button(start_frame, text="Adult", font=('arial', 30, 'bold'), bg='black', fg='white', command=start_quiz_Adult)
start_button_Adult.place(y=300,x=800)

# Images
lifeline50img=PhotoImage(file='Image\\d250-50.png')
lifeline50button_crossimg=PhotoImage(file='Image\\d2cross50-50.png')
flipTQimg=PhotoImage(file='Image\\flipTQ.png')
flipTQcrossimg=PhotoImage(file='Image\\flipTQcross.png')
layimg=PhotoImage(file='lay.png')
centerimg=PhotoImage(file='Image\\center.png')
DDimg=PhotoImage(file='Image\\DD.png')
winning_img=PhotoImage(file='Image\\congo.png')

scoreimg0=PhotoImage(file='Image\\Picture0.png')
scoreimg1=PhotoImage(file='Image\\Picture1.png')
scoreimg2=PhotoImage(file='Image\\Picture2.png')
scoreimg3=PhotoImage(file='Image\\Picture3.png')
scoreimg4=PhotoImage(file='Image\\Picture4.png')
scoreimg5=PhotoImage(file='Image\\Picture5.png')
scoreimg6=PhotoImage(file='Image\\Picture6.png')
scoreimg7=PhotoImage(file='Image\\Picture7.png')
scoreimg8=PhotoImage(file='Image\\Picture8.png')
scoreimg9=PhotoImage(file='Image\\Picture9.png')
scoreimg10=PhotoImage(file='Image\\Picture10.png')
scoreimg11=PhotoImage(file='Image\\Picture11.png')
scoreimg12=PhotoImage(file='Image\\Picture12.png')
scoreimg13=PhotoImage(file='Image\\Picture13.png')
scoreimg14=PhotoImage(file='Image\\Picture14.png')
scoreimg15=PhotoImage(file='Image\\Picture15.png')

scoreimg=[scoreimg0,scoreimg1,scoreimg2,scoreimg3,scoreimg4,scoreimg5,scoreimg6,scoreimg7,scoreimg8,scoreimg9,scoreimg10,scoreimg11,scoreimg12,scoreimg13,scoreimg14,scoreimg15]


# Quiz screen

layout=Label(quiz_frame,image=layimg,bg='black')
layout.place(x=0,y=350)

center=Label(quiz_frame,image=centerimg,bg='black')
center.place(x=225,y=350-200)

lifeline50button=Button(quiz_frame,image=lifeline50img,bg='black',bd=0,activebackground='black',width=180,height=80,command=fifty_fifty)   
lifeline50button.place(x=50+100,y=45)

flipTQbutton=Button(quiz_frame,image=flipTQimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=flip) 
flipTQbutton.place(x=300+100,y=45)


score=Label(quiz_frame,image=scoreimg[0],bg='black')
score.place(x=900,y=20)

Textarea = Text(quiz_frame, wrap='word', cursor='arrow', font=('arial', 18, 'bold'), width=42, height=2, fg='white', bd=0, bg='black', state='normal')
Textarea.place(x=75, y=15+350)
Textarea.bind("<Key>", lambda e: "break")

optionlabelA = Label(quiz_frame, text='A:', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0)
optionlabelA.place(x=60, y=130+350)

optionAbutton = Button(quiz_frame, text='', activebackground='black', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0, activeforeground='white', cursor='hand2', command=click1)
optionAbutton.place(x=100, y=120+350)

optionlabelB = Label(quiz_frame, text='B:', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0)
optionlabelB.place(x=380, y=130+350)

optionbbutton = Button(quiz_frame, text='', activebackground='black', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0, activeforeground='white', cursor='hand2', command=click2)
optionbbutton.place(x=410, y=120+350)

optionlabelc = Label(quiz_frame, text='C:', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0)
optionlabelc.place(x=60, y=230+350)

optioncbutton = Button(quiz_frame, text='', activebackground='black', font=('arial', 18, 'bold'), fg='white', bg='black', bd=0, activeforeground='white', cursor='hand2', anchor='sw', command=click3)
optioncbutton.place(x=90, y=215+350)

optionlabeld = Label(quiz_frame, text='D:', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0)
optionlabeld.place(x=380, y=230+350)

optionDbutton = Button(quiz_frame, text='', activebackground='black', font=('arial', 18, 'bold'), bg='black', fg='white', bd=0, activeforeground='white', cursor='hand2', anchor='sw', command=click4)
optionDbutton.place(x=410, y=215+350)


# Display start screen initially
start_frame.pack(fill='both', expand=True)

root.mainloop()
 