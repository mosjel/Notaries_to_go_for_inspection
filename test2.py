# # Define ANSI escape codes for text colors
# color_codes = {
#     'light_blue': '\033[94m',
#     'red': '\033[91m',
#     'neon_green': '\033[92m',
#     'yellow': '\033[93m',
#     'reset': '\033[0m'
# }

# # Define the text to print
# lines = [
#     (color_codes['light_blue'] + 'First line with light blue neon' + color_codes['reset']),
#     (color_codes['red'] + 'Second line red' + color_codes['reset']),
#     (color_codes['neon_green'] + 'Third line neon green' + color_codes['reset']),
#     (color_codes['yellow'] + 'Fourth line yellow' + color_codes['reset'])
# ]
# for i in range(len(lines)):
#     print(lines[i])



# # Define ANSI escape codes for text colors
# color_codes = {
#     'black': '\033[30m',
#     'red': '\033[31m',
#     'green': '\033[32m',
#     'yellow': '\033[33m',
#     'blue': '\033[34m',
#     'purple': '\033[35m',
#     'cyan': '\033[36m',
#     'white': '\033[37m',
#     'reset': '\033[0m'
# }

# # Define the text to print
# lines = [
#     f"{color_codes['red']}Red Text{color_codes['reset']}",
#     f"{color_codes['green']}Green Text{color_codes['reset']}",
#     f"{color_codes['blue']}Blue Text{color_codes['reset']}",
#     f"{color_codes['yellow']}Yellow Text{color_codes['reset']}",
#     f"{color_codes['purple']}Purple Text{color_codes['reset']}",
#     f"{color_codes['cyan']}Cyan Text{color_codes['reset']}",
#     f"{color_codes['white']}White Text{color_codes['reset']}"
# ]

# # Print the text
# for line in lines:
#     print(line)

# color_codes = {
#     'black': '\033[30m',
#     'dark_gray': '\033[90m',
#     'light_gray': '\033[37m',
#     'reset': '\033[0m'
# }

# # Define the text to print
# lines = [
#     f"{color_codes['black']}Black Text{color_codes['reset']}",
#     f"{color_codes['dark_gray']}Dark Gray Text{color_codes['reset']}",
#     f"{color_codes['light_gray']}Light Gray Text{color_codes['reset']}"
# ]

# # Print the text
# for line in lines:
#     print(line)

# color_codes = {
#     'neon_black': '\033[30;48;5;235m',
#     'neon_red': '\033[38;5;196m',
#     'neon_green': '\033[38;5;46m',
#     'neon_yellow': '\033[38;5;226m',
#     'neon_blue': '\033[38;5;33m',
#     'neon_purple': '\033[38;5;165m',
#     'neon_cyan': '\033[38;5;87m',
#     'neon_white': '\033[38;5;15m',
#     'reset': '\033[0m'
# }

# # Define the text to print
# lines = [
#     f"{color_codes['neon_black']}Neon Black Text{color_codes['reset']}",
#     f"{color_codes['neon_red']}Neon Red Text{color_codes['reset']}",
#     f"{color_codes['neon_green']}Neon Green Text{color_codes['reset']}",
#     f"{color_codes['neon_yellow']}Neon Yellow Text{color_codes['reset']}",
#     f"{color_codes['neon_blue']}Neon Blue Text{color_codes['reset']}",
#     f"{color_codes['neon_purple']}Neon Purple Text{color_codes['reset']}",
#     f"{color_codes['neon_cyan']}Neon Cyan Text{color_codes['reset']}",
#     f"{color_codes['neon_white']}Neon White Text{color_codes['reset']}"
# ]

# # Print the text
# for line in lines:
#     print(line)

# Define ANSI escape codes for bold and font size
# Define ANSI escape codes for bold and text color
text_style = {
    'bold': '\033[1m',
    'blue_neon': '\033[38;5;33m',  # Blue neon color
    'reset': '\033[0m'  # Reset all styles
}

# Define the text to print
text = "hamed"

# Print the text in bold and blue neon color
formatted_text = f"{text_style['bold']}{text_style['blue_neon']}{text}{text_style['reset']}"
print(formatted_text)

print("\033[1m\033[38;5;196m" + "king")
print("\033[38;5;196m" + "king")
print("\033[1m\033[38;5;33m" + "hamed")
print( "\033[38;5;33m" + "karimkkkkkkkkkkkkkkkkkkkkkk")
print("\033[1m" + "\033[38;5;33m" + "karim")

print("\033[1m" + "\033[38;5;33m" + "hamed\033[0m")


print("\033[38;5;33m"+"hamyyyyyyyyyyyyyyyyyyyyyyyyyyyyed")
print("u'\u202B'اسم من حامد است")

print("fdsfsdgerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
import shutil

import os 
columns = os.get_terminal_size().columns
from shutil import get_terminal_size
import pandas as pd
pd.set_option("display.width",get_terminal_size()[0])
def revrse_sentence(sentence):
    rev_sen=[]
    sep_sen=sentence.split()
    for i in range(len(sep_sen)):
        rev_sen.append(sep_sen[-(i+1)])
    

    return " ".join(rev_sen)
def reverse_text(text):
    len_t=len(text)
    out=""
    for i in range(len_t):
        out=out+text[len_t-i-1]
        out=str(out)
    return(out)
def introduction():
    s=[]
    s.append("--------------------تندر افزار نرم--------------------")
    s.append("(بازرسی جهت رسمی اسناد دفاتر نوبت تعیین)")
    s.append("1403 بهار - 1.1 نسخه")
    s.append ("نسخه 1.1")
    s.append("-------------------------")
    s.append("جلوه مصطفی")
    s.append("Email: mostafaajelveh@gmail.com")

    for num,i in enumerate(s):
        
        padding = columns - len(i)
        div_pd=padding//2
        if num<5:
            print('\033[1m'+"\033[38;5;226m"+'-' * (div_pd)+i+'-' * (div_pd))
        else:
            print('\033[1m'+'\033[38;5;15m'+'-' * (div_pd)+i+'-' * (div_pd))

    return()

process_label="......[notary_visited_total.xlsx] فایل اطلاعات پردازش حال در"
success_label=".شد ایجاد موفقیت با [notaries_togo.xlsx]  فایل"
error_label="{e}: شد مواجه خطا با فایل ایجاد"
# # Get the terminal size
# columns = shutil.get_terminal_size().columns

# # The string to print
# text = "hamed khubi?"
# # Calculate the padding needed to right-align the text
# padding = columns - len(text)

# # Print the text with the calculated padding
# print(' ' * padding + text)

os.system('cls' if os.name == 'nt' else 'clear')
introduction()
for i in range(4):   
    print()

for i in range(7):
    print('\033[1m'+"\033[38;5;196m"+"*"*columns)


print('\033[1m'+'\033[38;5;33m'+" "*(columns-len(process_label)-1),process_label)
print('\033[1m'+'\033[38;5;46m'+" "*(columns-len(success_label)-2),success_label)

# reverse_text("mamad")

# print(revrse_sentence(" i am good dasffw"))
# import shutil
# from bidi.algorithm import get_display

# # Get the terminal size
# columns = shutil.get_terminal_size().columns

# def introduction():
#     s = []
#     s.append("--------------------تندر افزار نرم--------------------")
#     s.append("(تعیین نوبت دفاتر اسناد رسمی جهت بازرسی)         ")
#     s.append("نسخه 1.1- بهار 1403")
#     s.append("-------------------------")
#     s.append("مصطفی جلوه")
#     s.append("Email: mostafaajelveh@gmail.com")
    
#     for num, text in enumerate(s):
#         # Convert the text for proper RTL display
#         display_text = get_display(text)  # Ensure proper RTL display
#         # Calculate the padding needed to right-align the text
#         padding = columns - len(display_text)
#         # Print the text right-aligned
#         print(' ' * padding + display_text)
#         print(num)  # Print the enumeration number

# # Call the introduction function to test
# introduction()