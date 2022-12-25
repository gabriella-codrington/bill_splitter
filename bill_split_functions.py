from tkinter import *
import tkinter
import tkinter.messagebox

def __init__():
    self.num_of_people = num_of_people
    self.bill_total = bill_total


#how to split
def how_to_split(bill_total, num_of_people):
    question1 = "How would you like to split the bill?"

    global window
    window = Tk()
    window.title("Bill Splitter")
    window.geometry("200x200")
    

    text_box = Text(window)
    text_box.insert('end', question1)
    
    def even_option():
        equal_split(bill_total, num_of_people)

    def by_order_option():
        split_by_order(bill_total)
    
    even_btn = Button(window,
                   text = "Split evenly",
                   command = even_option)
    by_order_btn = Button(window,
                   text = "Split by order",
                   command = by_order_option)

    even_btn.pack(side = LEFT)
    by_order_btn.pack(side = RIGHT)



#split the bill evenly
def equal_split(bill_total, num_of_people):
    individual_bill = float(bill_total)/int(num_of_people)
    final_bill = float(individual_bill + add_tip(num_of_people))
    print(f"You each will pay ${final_bill:.2f}")


#split by order 
def split_by_order(bill_total):
    bill = {}
    for i in range(num_of_people):
        person = input("Enter a person's name: ")
        item = float(input("Enter the amount of what they ordered: "))

        bill[person] = float(item)

    add_tip(num_of_people)

    for person, item in bill.items():
        item += individual_tip
        print(f"{person} will pay ${item:.2f}")
    

#add a tip
def add_tip(num_of_people):
    print("Would you like to add a tip?")

    
    #yes, ill tip
    def yes_option():
        total_tip = input("Okay! How much would you like to tip? ")
        global individual_tip
        individual_tip = float(total_tip)/num_of_people
        tkinter.messagebox.showinfo("Add a tip", f"Each person will tip ${individual_tip:.2f}")
        
    #no, i wont tip  
    def no_option():
        tkinter.messagebox.showinfo("No tip", "Okay! Let's continue")
        global individual_tip
        individual_tip = 0
        

    yes_btn = Button(window,
                     text = "YES",
                     command = yes_option)
    no_btn = Button(window,
                    text = "NO",
                    command = no_option)

    yes_btn.pack(side = LEFT)
    no_btn.pack(side = RIGHT)

    return individual_tip



def main():
    global window
    window = Tk()
    window.title("Bill Splitter")
    window.geometry("200x200")

    #root = Tk()

    nop = Entry(window, width=50)
    nop.pack()

    def num_of_people():
        num_of_people_label = Label(window, text = "Got it!")
        num_of_people_label.pack()

    #ask for number of people
    #global num_of_people
    num_of_people_button = Button(window, text = "Enter number of people", command = num_of_people)
    num_of_people_button.pack()
    num_of_people = nop.get()

    bt = Entry(window, width=50)
    bt.pack()
    
    def bill_total():
        bill_total_label = Label(window, text = "Got it!")
        bill_total_label.pack()

    #ask for total
    #global bill_total
    bill_total_button = Button(window, text = "Enter bill total", command = num_of_people)
    bill_total_button.pack()
    bill_total = bt.get()

    #decide how to split the bill
    how_to_split(bill_total, num_of_people)



main()
