const titleInput = document.querySelector('input[name=title]');
const titleInput = document.querySelector('input[name=slug]');


const slugify = (val)=> {
	return val.toString().toLowerCase().trim()
	  .replace(/&/g,'-and-') //replace & with '-and-'
	  .replace(/[\s\W-]+/g,'_') // replace spaces, none word chars and dashes with a single dash
};

titleInput.addEventListner('keyup',(e)=> {
	slugInput.setAttribute('value',slugify(titleInput.value));

});