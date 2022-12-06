

from textblob import TextBlob
from pdfminer.high_level import extract_text
import os
from tkinter import Tk, filedialog


root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
open_file = filedialog.askdirectory() # Returns opened path as str

#directory = 'watani'
new_names = []

# iterate over files in
# that directory
for filename in os.listdir(open_file):
    
     path = open_file
     # get pdf name and read it
     full_filename = path+'/'+filename
     text = extract_text(full_filename)

     blob = TextBlob(text)
     # find the id
     std_id = [v for (v,t) in blob.tags if t == 'CD' and v.isdigit() and len(v)==10]
     new_names.append(std_id[0])
count = 0
for file in os.listdir(open_file):
     new_filename = path + '/' + new_names[count] + '.pdf'
     old_filename = path + '/' + file
     os.rename(old_filename, new_filename)
     count += 1
res = os.listdir(open_file)
print(f'{count} files renamed\n {res}')
     

