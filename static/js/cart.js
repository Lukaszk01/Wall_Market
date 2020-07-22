const updateBtns = document.getElementsByClassName('update-cart')

for(const i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    const productId = this.dataset.product
    const action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
  })
}
