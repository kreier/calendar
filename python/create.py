# create calendar 2024-10-03

from fpdf import FPDF
import pandas as pd
import os, sys

version      = "24.09"
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
    global pdf, x1, y1, page_width, page_height
    return x1

def pos_y(day):
    return y1

def create_canvas(year):
    global filename, pdf
    filename = "../export/" + str(year) + ".pdf"
    pdf = FPDF(unit="pt", format=(page_width, page_height))       # don't use orientation ="landscape" since it only swaps width and height
    pdf.set_margin(0)
    pdf.c_margin = 0
    pdf.add_font("Aptos", style="", fname="fonts/aptos.ttf")
    pdf.set_font("Aptos", "", 10)
    pdf.set_text_color(0)
    pdf.add_page(format=(page_width, page_height))
    pdf.set_author("Matthias Kreier")
    pdf.set_title(f"Calendar {year}")
    pdf.set_subject("Organizing your Time, Documenting Main Events")
    pdf.set_xy(x1, y1 + 20)
    pdf.cell(text=str(year))
    pdf.set_draw_color(100, 150, 200)
    pdf.set_fill_color(200, 150, 100)
    pdf.rect(x1, y1 + 30, 100, 20, style="FD")
    return True

def create_vacation(year):
    print("no vacation")
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
    year = sys.argv[1]
    create_calendar(year)
