var names= ["john", "sarah", 23, "Rudolf",34];
for (let i = 0; i < names.length; i++) {
	if (typeof(name[i]) != "string" ){
		continue;
	}
	else if (typeof(names[i]) == "string"){
		if(names[i].charAt(0) == names[i].charAt(0).toUpperCase()){
		console.log(names[i]);
	}

		else {
	console.log(names[i].charAt(0).toUpperCase() + names[i].substring(1,names[i].length));
}
}
}