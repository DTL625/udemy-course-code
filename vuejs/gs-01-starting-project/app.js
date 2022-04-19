// let btnEl = document.querySelector('button')
// let inputEl = document.querySelector('input')
// let listEl = document.querySelector('ul') 

// btnEl.addEventListener('click', function (el) {
//    const listItemEl = document.createElement('li') 
//    listItemEl.textContent = inputEl.value
//    listEl.append(listItemEl)
// })


// $(document).ready(function(){
    function copyFunction() {
    //   var copyText = "$myInput";
    var copyText = document.getElementById("myInput");

    //   var copyText = document.createElement("cpText");
    //   copyText.textContent = 'foooooo';
      copyText.select();
      document.execCommand("Copy");
      alert("Copied the text: " + copyText.value);
    }
// });