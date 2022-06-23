# * GUI for the twitter scraper
# * Still needs a lot of work


from tkinter import *
import tkinter as tk
import tkinter.scrolledtext  as st
from scrape import scrap

def display(tweet):
   
   text_box.insert(tk.INSERT, tweet)

 #hashtag and find the top 5 tweets
def submit():
   text_box.delete(1.0, END)
   text = hashtag_var.get()
   hashtag = "#"
   hashtag += text
   scrape = scrap(hashtag, 5)
   
  
   x = scrape.scraper()
   display(x)
 



root = Tk()

hashtag_var = tk.StringVar()
root.title("TwiScraper")
root.geometry("700x800")
padding = {'padx': 50, 'pady' : 0}
ypadd = {'padx': 0, 'pady' : 12}
label1 = Label(root, text="Tweets", font=("Times", 12)).grid(column=3, row=0, sticky="NSWE", padx=20)


text_box = st.ScrolledText(root, bg='white', width=60, height=30, font=("Times", 12))
text_box.grid(row=1, column=3, **ypadd)



label2 = Label(root, text="Enter Hashtag: (e.g. nba)").grid(row=2, column=2)
hashtag = Entry(root, textvariable=hashtag_var, width=39).grid(row=2, column=3)
Search = Button(root, text='Search', width=15, command=submit).grid(row=3, column=3)



root.mainloop()