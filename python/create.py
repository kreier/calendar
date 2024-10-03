# create calendar 2024-10-03

from fpdf import FPDF
from datetime import datetime
import pandas as pd
import os, sys, math

version      = "24.10"
mm           = 2.834645669      # document is in pt, 46 rows with 12pt height, text 10pt
border_lr    = 5*mm              
border_tb    = 5*mm          
page_width   = 297*mm           # A4 landscape width
page_height  = 210*mm           # A4 landscape height
x1           = border_lr        # left starting point for x
y1           = border_tb        # top starting point for y (in fpdf2)

# Check execution location, exit if not in /timeline/python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the python folder.")
    exit()

def pos_x(month):
    global x1
    return x1 + 67.8*month

def pos_y(day):
    global y1
    return y1 + 20 + 17.1*day

def is_valid_date(year, month, day):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4==0 and (year%100 != 0 or year%400==0):
        day_count_for_month[2] = 29
    return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

def create_canvas(year):
    global filename, pdf, colors
    filename = "../export/" + str(year) + ".pdf"
    pdf = FPDF(unit="pt", format=(page_width, page_height))       # don't use orientation ="landscape" since it only swaps width and height
    pdf.set_margin(0)
    pdf.c_margin = 0
    pdf.add_font("Aptos", style="", fname="fonts/aptos.ttf")
    pdf.set_font("Aptos", "", 10)
    pdf.add_page(format=(page_width, page_height))
    pdf.set_author("Matthias Kreier")
    pdf.set_title(f"Calendar {year}")
    pdf.set_subject("Organizing your Time, Documenting Main Events")
    pdf.set_xy(x1, y1)
    pdf.set_font_size(20)
    pdf.set_text_color(0, 0, 155)
    pdf.cell(text=str(year))                                      # Cell takes the upper left corner as reference for printing text
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    colors = [[255, 255, 5]]
    # create outlines for 365 days
    pdf.set_line_width(0.8)
    pdf.set_draw_color(0, 0, 0)                                   # pure black outside lines
    pdf.set_text_color(0)
    pdf.set_font_size(12)
    fill_white = (255, 255, 255)
    for month in range(12):
        fill_color = (220 + 25*math.sin(month/6*math.pi + 4.2), 220 + 25*math.sin(month/6*math.pi), 220 + 25*math.sin(month/6*math.pi + 2.15))
        pdf.set_fill_color(fill_color)
        for day in range(32):
            pdf.set_xy(pos_x(month)+1, pos_y(day))
            if day == 0:
                pdf.rect(pos_x(month), pos_y(day), 67.8, 17.1, style="FD")
                pdf.set_font_size(12)
                pdf.cell(w=67.8, h=17.1, align='C', text=months[month])
            else:
                if is_valid_date(year, month + 1, day):
                    if datetime(year, month +1, day).isoweekday() < 6:  # weekday
                        pdf.set_fill_color(fill_white)
                    else:
                        pdf.set_fill_color(fill_color)
                    pdf.rect(pos_x(month), pos_y(day), 67.8, 17.1, style="FD")
                    pdf.set_font_size(8)
                    pdf.cell(text=str(day))

def create_vacation(year):
    print("no vacation yet")
    return True

def render_to_file():
    global pdf, filename
    pdf.output(filename)

def create_calendar(year):
    create_canvas(year)
    create_vacation(year)
    render_to_file()

if __name__ == '__main__':
    print(f"Calendar v{version}")
    if len(sys.argv) < 2:
        print("You did not provide a year as argument. Put it as a parameter after create.py")
        exit()
    year = int(sys.argv[1])
    create_calendar(year)
