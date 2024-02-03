
const product = [

    {
        id: 0,
        image: "images/f1.png",
        title: 'Kit-Kat bar',
        price: 50,
    },
    {
        id: 1,
        image: 'image/hh-2.jpg',
        title: 'Cheez-It',
        price: 70,
    },
    {
        id: 2,
        image: 'image/ee-3.jpg',
        title: 'Cheetos',
        price: 150,
    },
    {
        id: 3,
        image: 'image/aa-1.jpg',
        title: 'Dove Chocolate',
        price: 200,
    },
    {
        id: 4,
        image: 'image/aa-1.jpg',
        title: 'Snickers',
        price: 15,
    },
    {
        id: 3,
        image: 'image/aa-1.jpg',
        title: 'Pringles Original',
        price: 90,
    },
    {
        id: 3,
        image: 'image/aa-1.jpg',
        title: 'Lays Classic',
        price: 76,
    },
    {
        id: 3,
        image: 'image/aa-1.jpg',
        title: 'Oreo 405g',
        price: 310,
    }

];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
           
        <div class='bottom'>
        <p class="www">${title}</p>
        <h2>₱ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
               
                <p style='font-size:12px;'>${title}</p>
                <h1 style='font-size: 15px;'>₱ ${price}.00</h1>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}