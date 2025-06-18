from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np

# Create plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("plot.png")
plt.close()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Sample Report with Sine Wave", ln=True)
pdf.image("plot.png", x=10, y=30, w=180)
pdf.output("report1.pdf")
