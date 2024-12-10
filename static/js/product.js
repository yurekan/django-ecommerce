// var product = document.getElementsByClassName("view-product")

// for(i=0; i<product.length; i++){
//     product[i].addEventListener("click", function(){
//         var productId = this.dataset.product
//         console.log(productId)
//         renderProductPage(productId)
//     })
// }

// function renderProductPage(productId){

//     var url = '/product/'

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({'productId': productId}),
//     })
//     .then((response) => {
//         return response.json()
//     })
//     .then((data) => {
//         console.log('Data: ', data)
//     })

// }