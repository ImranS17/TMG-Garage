let carts = document.querySelectorAll('.add-cart');

let service = [
    {
        name: 'Battery Boost',
        price: 460,
        incart: 0
    },

    {
        name: 'Battery Cable Replacement',
        price: 640,
        incart: 0
    },

    {
        name: 'Battery Replacement',
        price: 6160,
        incart: 0
    }
];

for (let i=0; i < carts.length; i++) {
    carts[i].addEventListener('click', () => {
        cartNumbers(service[i]);
        totalCost(service[i])
    })
}

function onLoadCartNumbers() {
    let productNumbers =localStorage.getItem('cartNumbers');

    if(productNumbers) {
        document.querySelector('.cart span').textContent = productNumbers;
    }
}

function cartNumbers(service) {
    let productNumbers =localStorage.getItem('cartNumbers');
    productNumbers = parseInt(productNumbers);
    if(productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers + 1);
        document.querySelector('.cart span').textContent = productNumbers + 1;
    }
    else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.cart span').textContent = 1;
    }
    setItems(service);
}

function setItems(service) {
    let cartItems = localStorage.getItem('serviceInCart');
    cartItems = JSON.parse(cartItems);
    
    if(cartItems != null) {
        if(cartItems[service.name] == undefined) {
            cartItems = {
                ...cartItems,
                [service.name]: service
            }
        }
        cartItems[service.name].incart += 1;
    } 
    else {
        service.incart = 1;
        cartItems = {
           [service.name]: service
        }
    }
    localStorage.setItem("serviceInCart", JSON.stringify(cartItems));
}

function totalCost(service) {
    let cartCost = localStorage.getItem('totalCost');

    console.log("My cartCost is", cartCost);
    console.log(typeof cartCost);

    if(cartCost !=null) {
        cartCost = parseInt(cartCost);
        localStorage.setItem("totalCost", cartCost + service.price);
    }
    else {
        localStorage.setItem("totalCost", service.price);
    }
}

function displayCart() {
    let cartItems = localStorage.getItem("serviceInCart");
    cartItems = JSON.parse(cartItems); 
    let serviceContainer = document.querySelector
    (".services");
}

onLoadCartNumbers();
displayCart();