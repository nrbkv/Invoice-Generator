# Invoice-Generator

This project is a **Freelancer Invoice Generator** built using FastAPI, Pydantic for data validation, and FPDF for generating PDF invoices. The system allows freelancers to create detailed invoices for their clients, including itemized services with descriptions, quantities, and pricing. Here's a detailed description of the functionality:
**Key Features:**
1. Invoice Data Input:
○ Freelancers can input invoice details including client and freelancer
information, the invoice number, date, and itemized services or products.
2. PDF Invoice Generation:
○ The API generates a professional-looking PDF invoice based on the input data.
○ The PDF includes a header with the invoice number and date, freelancer and client details, and an itemized table of services/products with quantities, prices, and total amounts.
○ The total amount due is automatically calculated.
3. Downloadable Invoices:
○ Once generated, the PDF invoice is returned as a downloadable file for easy distribution.
Endpoints:
● POST/generate-invoice/:AcceptsinvoicedataasJSONinput,generatesa PDF invoice, and returns the invoice as a downloadable file.
● GET/:Servesthehomepagewithastaticfrontend,enablinguserstoinputtheir invoice details.
Input Data Structure:
● InvoiceData:
○ client_name:Nameoftheclient.
○ client_address:Addressoftheclient.
○ freelancer_name:Nameofthefreelancer.
○ freelancer_address:Addressofthefreelancer.
○ items:Alistofitems(description,quantity,andprice). ○ invoice_number:Auniqueidentifierfortheinvoice. ○ date:Dateofinvoicecreation.
● InvoiceItem:
○ description:Descriptionoftheserviceorproduct. ○ quantity:Numberofunitsorhours.
○ price:Priceperunitorhour.
Stack:

 ● Backend: FastAPI for API handling and business logic.
● Frontend: Static files served for user interaction.
● PDF Generation: FPDF for creating and formatting the invoice.
● Data Validation: Pydantic for enforcing correct input structure.
This tool provides an efficient and professional solution for freelancers to generate and share invoices with their clients. The generated invoices can be easily customized, stored, and printed.

