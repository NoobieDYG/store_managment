document.addEventListener("DOMContentLoaded", function() {
    fetchOrders();
    fetchProducts();
    fetchorder_details();
});

function fetchOrders() {
    fetch('/getallorder')
        .then(response => response.json())
        .then(data => {
            const ordersList = document.getElementById("ordersList");
            data.forEach(order => {
                const row = `<tr>
                                <td>${order.order_id}</td>
                                <td>${order.customer_name}</td>
                                <td>${order.date_time}</td>
                                <td>${order.total}</td>
                            </tr>`;
                ordersList.innerHTML += row;
            });
        })
        .catch(error => console.log("Error fetching orders:", error));
}

function fetchorder_details(){
    fetch('/getorderdetail')
        .then(response => response.json())
        .then(data => {
            const orderDetailsList=document.getElementById('orderDetailsList');
            data.forEach(order => {
                const row = `<tr>
                                <td>${order.order_id}</td>
                                <td>${order.price_per_unit}</td>
                                <td>${order.product_name}</td>
                                <td>${order.quantity}</td>
                                <td>${order.total_price}</td>
                            </tr>`;
                orderDetailsList.innerHTML +=row;
            })
        })
        .catch(error => console.log("Error fetching orders:", error));

}

document.getElementById('orderForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from refreshing the page

    // Collect form data
    const customerName = document.getElementById('customerName').value;
    const totalPrice = document.getElementById('totalPrice').value;
    const orderDate = document.getElementById('orderDate').value;
    const productId = document.getElementById('productId').value;
    const quantity = document.getElementById('quantity').value;
    const productTotalPrice = document.getElementById('productTotalPrice').value;

    // Create the order object
    const order = {
        customer_name: customerName,
        total: totalPrice,
        date_time: orderDate,
        order_details: [
            {
                product_id: productId,
                quantity: quantity,
                total_price: productTotalPrice
            }
        ]
    };

    // Send the data to the backend using fetch
    fetch('/insertorder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data:order })
    })
    .then(response => response.json())
    .then(data => {
        // Close the modal and reset the form
        $('#addOrderModal').modal('hide');
        document.getElementById('orderForm').reset();

        // Refresh the orders list
        fetchOrders();

        // Show success message
        alert('Order added successfully with ID: ' + data.order_id);
    })
    .catch(error => console.error('Error adding order:', error));
});

function fetchProducts() {
    fetch('/getProduct')
        .then(response => response.json())
        .then(data => {
            const productsList = document.getElementById("productsList");
            data.forEach(product => {
                const row = `<tr>
                                <td>${product.product_id}</td>
                                <td>${product.product_name}</td>
                                <td>${product.umid}</td>
                                <td>${product.umname}</td>
                                <td>${product.price_per_unit}</td>
                            </tr>`;
                productsList.innerHTML += row;
            });
        })
        .catch(error => console.log("Error fetching orders:", error));
}