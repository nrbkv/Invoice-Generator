document.getElementById("invoice-form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const invoiceData = {
        freelancer_name: formData.get("freelancer_name"),
        freelancer_address: formData.get("freelancer_address"),
        client_name: formData.get("client_name"),
        client_address: formData.get("client_address"),
        invoice_number: formData.get("invoice_number"),
        date: formData.get("date"),
        items: []
    };

    const descriptions = formData.getAll("description[]");
    const quantities = formData.getAll("quantity[]");
    const prices = formData.getAll("price[]");

    for (let i = 0; i < descriptions.length; i++) {
        invoiceData.items.push({
            description: descriptions[i],
            quantity: parseInt(quantities[i]),
            price: parseFloat(prices[i])
        });
    }

    const response = await fetch("/generate-invoice/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(invoiceData)
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `invoice_${invoiceData.invoice_number}.pdf`;  // Set the file name for download
        document.body.appendChild(a);  // Append link to body
        a.click();  // Trigger download
        a.remove();  // Remove the link after download
    } else {
        alert("Failed to generate invoice.");
    }
});

document.getElementById("add-item").addEventListener("click", function() {
    const itemContainer = document.getElementById("items");

    // Create a new div for the item
    const newItem = document.createElement("div");
    newItem.classList.add("item");

    // Add new input fields for description, quantity, and price
    newItem.innerHTML = `
        <input type="text" placeholder="Description" name="description[]" required>
        <input type="number" placeholder="Quantity" name="quantity[]" required>
        <input type="number" placeholder="Price" name="price[]" required>
    `;

    // Append the new item div to the items container
    itemContainer.appendChild(newItem);
});
