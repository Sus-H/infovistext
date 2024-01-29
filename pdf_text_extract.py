# importing required modules 
from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('VAD-2021.pdf') 
  
# printing number of pages in pdf file 
pages = len(reader.pages)

page_range = range(7)

with open("infovis_text_v2.rtf", "w+", encoding="utf-16") as file:

    for page in page_range:
        # extracting text from page
        text = reader.pages[page].extract_text()

        bullet_indices = [i for i, x in enumerate(text) if x == "•"]
        # print(bullet_indices)
        for bullet_index in bullet_indices:
            text =  text[:bullet_index-1] + "\n" + text[bullet_index:] 

        # dash_indices = [j for j, y in enumerate(text) if y == "-"] 
        # for dash_index in dash_indices:
        #     text =  text[:dash_index] + "\n" + text[dash_index:]
              
        file.write(text)
        file.write("\n" + "\n")


# with open("infovis_text_v2.rtf", "w", encoding="utf-16") as file:
#     file.write(text)
    # file.write("{\\rtf1")
    # file.write("•don’t")
    # file.write("}")
    # file.write("""{\\rtf1 This is \\b Bold\\b0}""")
        


"""
# initializing N
N = 5
 
# using list slicing
# Add substring at specific index
res = test_string[ : N] + add_string + test_string[N : ]
     
# print result
print("The string after performing addition : " + str(res))
"""