# FPDF is the class that creates PDF instances
from fpdf import FPDF

# Creating a PDF document (through a FPDF instance)
# Arguments to FPDF object: 
# orientation ["L" - landscape, or , "P" - portrait]
# units (size of the dimensions of elements in the PDF that we add such as breaklines, etc.)
# format (format of the PDF, in our case the standard A4)
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Adding pages to our newly created PDF (the FPDF instance) through .add_page() method
pdf.add_page()

# Setting the overall font for the PDF (family = font, size = size of text, style = bold, italicized, underlined, etc.)
pdf.set_font(family = "Times", style = "b", size = 12)

# Text is added to the PDF through "cells" and the .cell() method
# parameters: 
# w = width of cell (0 = expand to width of the page)
# h = height of cell
# ln = breakline (0 = no breakline for next cell, 1 = set breakline to next line after width of next cell)
# align = alignment for text (L = left aligned, R = right aligned, etc.)
# border = displays a border for the cell (0 to n, numbers represent the thickness of border)
pdf.cell(w=0, h=12, ln=1, align = "L", border = 1, txt = "Awesome!")
pdf.cell(w=0, h=12, ln=1, align = "L", border = 1, txt = "No!")
    
pdf.output("output.pdf")

