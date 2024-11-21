This project is a **Freelancer Invoice Generator** built using FastAPI, Pydantic for data validation, and FPDF for generating PDF invoices. The system allows freelancers to create detailed invoices for their clients, including itemized services with descriptions, quantities, and pricing. Here's a detailed description of the functionality:

**Key Features:**

1. **Invoice Data Input**:
   1. Freelancers can input invoice details including client and freelancer information, the invoice number, date, and itemized services or products.
1. **PDF Invoice Generation**:
   1. The API generates a professional-looking PDF invoice based on the input data.
   1. The PDF includes a header with the invoice number and date, freelancer and client details, and an itemized table of services/products with quantities, prices, and total amounts.
   1. The total amount due is automatically calculated.
1. **Downloadable Invoices**:
- Once generated, the PDF invoice is returned as a downloadable file for easy distribution.

**Endpoints:**

- POST /generate-invoice/: Accepts invoice data as JSON input, generates a PDF invoice, and returns the invoice as a downloadable file.
- GET /: Serves the home page with a static frontend, enabling users to input their invoice details.

**Input Data Structure:**

- **InvoiceData**:
- client\_name: Name of the client.
- client\_address: Address of the client.
- freelancer\_name: Name of the freelancer.
- freelancer\_address: Address of the freelancer.
- items: A list of items (description, quantity, and price).
- invoice\_number: A unique identifier for the invoice.
- date: Date of invoice creation.
- **InvoiceItem**:
- description: Description of the service or product.
- quantity: Number of units or hours.
- price: Price per unit or hour.

**Stack:**

- **Backend**: FastAPI for API handling and business logic.
- **Frontend**: Static files served for user interaction.
- **PDF Generation**: FPDF for creating and formatting the invoice.
- **Data Validation**: Pydantic for enforcing correct input structure.

This tool provides an efficient and professional solution for freelancers to generate and share invoices with their clients. The generated invoices can be easily customized, stored, and printed.
