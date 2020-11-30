/*
//exercice 1
let addressStreet=" yaounde";
let country = "Cameroun";
let addressNumber = "52423";
let global_address = 'je vis au '+ addressNumber+addressStreet+ ' au ' + country;
console.log(global_address);

//exercice 2

let birthyear = 1933;
let futureyear = 2025;
let futureage = futureyear - birthyear;
console.log('i will be '+ futureage + " in "+ futureyear);

//exercice 3



let val1 = prompt("enter un nombre svp");
let val2 = prompt("entier un segond nombre svp");
let val3 = parseInt (val1) + parseInt(val2);
alert("la somme est "+val3);



let valeur1 = parseInt(prompt("enter un nombre svp"));
let valeur2 = parseInt(prompt("enter un segond nombre svp"));
let signe = prompt("entrer un operateur svp");
 switch(signe) {
	case "+":
		resultat = valeur1 + valeur2;
	break
	case"-":
	resultat = valeur1 - valeur2;
	break
	case "*":
	resultat = valeur1*valeur2;
	break
	case "/":
	resultat = valeur1 / valeur2;
	default : 
	console.log("ce n'est pas possible");
}
alert(resultat);


let val1 = "i am finding Nemo !";
let val2 = val1.split(' ');
let result = val2.indexOf('Nemo');
console.log(val2);
console.log("i found Nemo at " + result + "!");


let val1 = "il ya nemo dans cette phrase";
let array_nemo = 

*/
//Daily challenge

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);
console.log(fruits.sort());
fruits.push('kiwi');
console.log(fruits);
let index= fruits.indexOf('Apples');
fruits.splice(index,1);1y
console.log(fruits);
console.log(fruits.reverse());
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][]);






