# Calendar

Create A4 landscape calendars to organize my life.

## Data in the /db folder

Inside the db folder are the required files to be found. Each year has its own folder. Inside are the relevant listed dates as `.csv` files. For example the `vacation.csv` for all kind of holidays. The structure is to be determined later

## Program in the /python folder

The program is written in the `create.py` file and executed as `python create.py 2024` to create the 2024 calendar.

## Software used: [fpdf2](https://py-pdf.github.io/fpdf2/index.html)

For some time I used to work with reportlab and it suited my needs very well. But in summer 2024 I discovered limitations with regards to font shaping (like for Khmer and Sinhala) and the support for RTL languages. The implementation in fpdf2 worked, so I switched the python pdf generator package.

## Dimensions

An A4 paper in landscape is 297 x 210 mm. Given 5 mm border the calendar with 31 lines for days, one more line for month and some 2 lines for the year on top have a remaining area of 287 mm width and 200 mm height. Each month would therefore get 287/12 = 23.9mm = 67.8pt width. If weekends get a different color then the days don't need to be labeled. As for the line height, we would need 31 + 1 + 2 = 34 lines. Each has a height of 200/34 = 5.89 mm. One point is 0.3515 mm, this line height is 17.1 points.
