let display = document.getElementById('display');
console.log(display);
let display_value = display.innerHTML;
console.log(display_value);
let current = [];
function my_f(num){
	let display = document.getElementById('display');
	current.push(num);
	display.innerHTML = current.join(' ');
	console.log(num);
}
