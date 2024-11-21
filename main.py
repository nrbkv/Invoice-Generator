from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fpdf import FPDF
import os

app = FastAPI()

# Serve the frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class InvoiceItem(BaseModel):
    description: str
    quantity: int
    price: float

class InvoiceData(BaseModel):
    client_name: str
    client_address: str
    freelancer_name: str
    freelancer_address: str
    items: list[InvoiceItem]
    invoice_number: str
    date: str

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Invoice', 0, 1, 'C')

    def invoice_header(self, invoice):
        # Invoice Title and Date
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, f"Invoice #{invoice.invoice_number}", 0, 1, 'C')
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, f"Date: {invoice.date}", 0, 1, 'C')
        self.ln(10)

    def freelancer_client_info(self, invoice):
        # Freelancer Info
        self.set_font('Arial', 'B', 12)
        self.cell(100, 10, "Freelancer Information", 0, 0)
        self.cell(100, 10, "Client Information", 0, 1)
        
        self.set_font('Arial', '', 12)
        self.cell(100, 10, f"Name: {invoice.freelancer_name}", 0, 0)
        self.cell(100, 10, f"Name: {invoice.client_name}", 0, 1)

        self.cell(100, 10, f"Address: {invoice.freelancer_address}", 0, 0)
        self.cell(100, 10, f"Address: {invoice.client_address}", 0, 1)
        self.ln(10)

    def invoice_items_table(self, invoice):
        # Table Header
        self.set_font('Arial', 'B', 12)
        self.cell(80, 10, 'Description', 1)
        self.cell(30, 10, 'Quantity', 1)
        self.cell(40, 10, 'Price', 1)
        self.cell(40, 10, 'Total', 1)
        self.ln()

        # Table Body
        self.set_font('Arial', '', 12)
        total_amount = 0
        for item in invoice.items:
            line_total = item.quantity * item.price
            total_amount += line_total
            self.cell(80, 10, item.description, 1)
            self.cell(30, 10, str(item.quantity), 1, 0, 'C')
            self.cell(40, 10, f"${item.price:.2f}", 1, 0, 'C')
            self.cell(40, 10, f"${line_total:.2f}", 1, 0, 'C')
            self.ln()

        # Total Amount
        self.cell(150, 10, 'Total Amount', 1)
        self.cell(40, 10, f"${total_amount:.2f}", 1, 0, 'C')
        self.ln(10)

@app.post("/generate-invoice/")
async def generate_invoice(invoice: InvoiceData):
    pdf = PDF()
    pdf.add_page()

    # Header
    pdf.invoice_header(invoice)

    # Freelancer and Client Info
    pdf.freelancer_client_info(invoice)

    # Invoice Items Table
    pdf.invoice_items_table(invoice)

    # Save the PDF
    invoice_file = f"invoice_{invoice.invoice_number}.pdf"
    pdf.output(invoice_file)

    # Return the PDF as a downloadable file
    return FileResponse(invoice_file, media_type='application/pdf', filename=invoice_file)

# Serve the home page with index.html
@app.get("/")
async def serve_home():
    return FileResponse("frontend/index.html")