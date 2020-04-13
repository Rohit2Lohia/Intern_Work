const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');
const slugufy = (val) =>{
   return val.toString().toLowerCase().trim()
   .replace(/&/g,'-and-') //replace '&' with '-and-'
   .replace(/[\s\W-]+/g,'-')
};
// event listner
titleInput.addEventListener('keyup',(e) => {
   slugInput.setAttribute('value',slugufy(titleInput.value))
});
