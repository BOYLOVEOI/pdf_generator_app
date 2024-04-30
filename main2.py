# FPDF is the class that creates PDF instances
from fpdf import FPDF
import pandas as pd

# Creating a PDF document (through a FPDF instance)
# Arguments to FPDF object: 
# orientation ["L" - landscape, or , "P" - portrait]
# units (size of the dimensions of elements in the PDF that we add such as breaklines, etc.)
# format (format of the PDF, in our case the standard A4)
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Ensuring that any content that goes on the pdf page does not automatically break the page (spill into a new page)
pdf.set_auto_page_break(auto=False, margin=0)

# Adding pages to our newly created PDF (the FPDF instance) through .add_page() method
# Example:
# pdf.add_page()

# Setting the overall font for the PDF (family = font, size = size of text, style = bold, italicized, underlined, etc.)
# Example:
# pdf.set_font(family = "Times", style = "b", size = 12)

# Text is added to the PDF through "cells" and the .cell() method
# parameters: 
# w = width of cell (0 = expand to width of the page)
# h = height of cell
# ln = breakline (0 = no breakline for next cell, 1 = set breakline to next line after width of next cell)
# align = alignment for text (L = left aligned, R = right aligned, etc.)
# border = displays a border for the cell (0 to n, numbers represent the thickness of border)

# Examples:
# pdf.cell(w=0, h=12, ln=1, align = "L", border = 1, txt = "Awesome!")
# pdf.cell(w=0, h=12, ln=1, align = "L", border = 1, txt = "No!")

# Reading in the data as a Pandas dataframe
df = pd.read_csv("topics.csv", delimiter=",")

# Setting the font
pdf.set_font(family = "Times", style = "b", size = 24)

# creating counter for page number
page = 1

# REMEMBER to get on a row by row basis, we can utilize the pandas .iterows() method (returns the contents of the row and index of the row as a tuple)
for index, row in df.iterrows():
    # Title Page
    pdf.add_page()
    # Setting font for header
    pdf.set_font(family = "Times", style = "b", size = 24)
    pdf.cell(w=0, h=12, ln=1, align="L", border=0, txt=row["Topic"])
    # Setting the font's color to black  RGB (0,0,0)
    pdf.set_text_color(r=0, g=0, b=0)
    # Adding a break line after the title
    # pdf.line requires 4 parameters -> x1 and y1 (the coordinates for the starting point of the line) and x2 and y2 (coordinates for endpoint of the line)
    pdf.line(10, 21, 200, 21)

    # Generating lined documents
    for i in range(30, 290, 10):
        pdf.line(10, i, 200, i)

    # Title Page Footer
    # Adding page footers
    # Setting breakline and starting point to 265mm (26.5cm down the page)
    pdf.ln(265)
    # Setting font for the footer with that is italicized and size 8 
    pdf.set_font(family="Times", style="i", size = 8)
    # Setting footer color
    pdf.set_text_color(r=0,g=0,b=0)
    # Adding the footer text (the page number)
    pdf.cell(w=0, h=10, align='R', txt=str(page))

    # Adding extra pages for each topic/section
    for pages in range(row["Pages"]-1):
        pdf.add_page()
        # incrementing page number for each additional page that was added
        page+=1
        # when a new page is created, breakpoint is set automatically back to 0
        # set the breakpoint for 277mm for new pages since we cover the difference between the cell's height on the title page that the new page is missing
        pdf.ln(277)
        pdf.cell(w=0, h=10, align='R', txt = str(page))
        
        # Creating lined documents 
        for i in range(20, 290, 10):
            pdf.line(10, i, 200, i)
    
    # incrementing page number
    page +=1

pdf.output("CompSciNotes.pdf")



