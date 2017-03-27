/*
*Script is called each time body is loaded
*Retrieves the check array which denotes which flags have been already matched
*Sets appropiate class for each image depending on returned check arrays (found / not found)
*Binds onclick and onhover event handlers to each flag image
*/

//Wrap functions inside init_setup, giving them access to parameters
function init_setup(array_name, array_size){

	//Begin by retrieving the check array promise
	var check_promise = browser.storage.local.get(array_name);

	//Resolve the promise, if check array is retrieved then begin setup
	check_promise.then(setup);


  /*-------------------Function Defs-----------------------------------*/

	//Event handler for onclick
	//Swaps the className of the parent cell to toggle transparency
	//missing -> found
	//found -> missing
	function checkHandler(event){
		target = event.target; //Retrieve image that has been clicked
		parent = target.parentElement;

		index = parent.id;
		value = false;

		if(parent.className == "missing"){
		  parent.className = "found"
		  value = true;
		}else {
		  parent.className = "missing"
		}

		//Write this to the check array
		var result_promise = browser.storage.local.get(array_name);
		result_promise.then(updateResults);

		//Update check array
		function updateResults(check_obj){

		  //When item is retrieved update it using the index and value
		  check_obj[array_name][index] = value;

		  let set = browser.storage.local.set(check_obj);
		  set.then();
		}
	}

	//Setup function determines whether the retrieved check object is empty (no array)
	//If so, then a new empty array is created and stored in local
	//Otherwise, the check array is extracted from the check object
	//setupTable is then called with the check-array
function setup(check_obj) {

	//Empty check object or length difference
	if(isEmpty(check_obj)){
		//Generate empty array of blank arrayss
		var blank_array = {};
		console.log("Empty array built");
		console.log(blank_array);

		//mapping of country_name -> 0
		//Iterate over all td elements and extract id's
		var flag_table = document.getElementById("flag-table");
		var flag_cells = flag_table.getElementsByTagName("td");

		for(var i = 0; i < flag_cells.length; i++){
			blank_array[flag_cells[i].id] = false;
		}

		console.log("Populated");
		console.log(blank_array);

		//Map array to provided array name (country name)
		var obj = {};
		obj[array_name] = blank_array;
		let set = browser.storage.local.set(obj);

		//Attempt to store the array
		set.then();

		//Bind event handlers and set correct class using the blank_array
		setupTable(blank_array);
	}
	else{

		//Pull out already populated array from results_obj
		check_array = check_obj[array_name];

		//One off operation for upgrade from V0.37
		//Remove in V0.40++
		//Convert previous 0/1 array into new associate array
		//Assuming flags have not changed since previous release!
		if(Array.isArray(check_array)){

			console.log("Updating");
			console.log(check_array);

			var blank_array = {};
			//First populate the blank array
			var flag_table = document.getElementById("flag-table");
			var flag_cells = flag_table.getElementsByTagName("td");

			for(var i = 0; i < flag_cells.length; i++){
				blank_array[flag_cells[i].id] = Boolean(check_array[i]);
			}

			console.log("Done");
			console.log(blank_array);

			var obj = {};
			obj[array_name] = blank_array;
			let set = browser.storage.local.set(obj);
			//Attempt to store the array
			set.then();

			//Bind event handlers and set correct class using the populated array
			setupTable(blank_array);
		}
		//Standard operation
		else{

			console.log("Rebuilding");
			console.log(check_array);

			//We'll rebuild using current page contents, ensures that flags are up to date
			var blank_array = {};
			//First populate the blank array
			var flag_table = document.getElementById("flag-table");
			var flag_cells = flag_table.getElementsByTagName("td");

			for(var i = 0; i < flag_cells.length; i++){
				blank_array[flag_cells[i].id] = false;
			}

			//Now loop over each key in the old array
			var keys = Object.keys(check_array)
			for(var i = 0; i < keys.length; i++){

				if(keys[i] in blank_array){
					blank_array[keys[i]] = check_array[keys[i]];
				}else{
						console.log("Key no longer present");
						console.log(keys[i]);
				}
			}

			console.log(blank_array);

			var obj = {};
			obj[array_name] = blank_array;
			let set = browser.storage.local.set(obj);
			//Attempt to store the array
			set.then();

			//Bind event handlers and set correct class using the populated array
			setupTable(blank_array);
		}
	}
}

	//Binds onhover and onclick event handlers to each img in the table
	//Sets correct class to cells (missing / found)
	function setupTable(check_array){

	  //Extract table and cells
	  var flag_table = document.getElementById("flag-table");
	  var flag_cells = flag_table.getElementsByTagName("td");

	  //Var to store img within each cell
	  var cell_img;

	  //Loop over all cells, extract child img, bind handlers and set class name
	  for(var i = 0; i < flag_cells.length; i++){

		  //Extract child
		  cell_img = flag_cells[i].children[0];

		  //Get child id, used to lookup stored array
		  img_no = cell_img.id;
		  //Subtract one, zero indexed arrays
		  img_no--;

		  //Bind handlers
		  cell_img.onclick = checkHandler;
		  cell_img.onmouseover = hoverHandler;

		  //Determine class type
		  //0 -> missing
		  //1 -> found
		  if(check_array[flag_cells[i].id]){
			flag_cells[i].className = "found";
		  }
		  else{
			  flag_cells[i].className = "missing";
		  }
	  }
	}

	//hoverHandler
	//Simply updates a paragraph element with the currently selected flag name
	function hoverHandler(event){
	  target = event.target;
	  document.getElementById("hover_text").textContent = target.title;
	}

	//Empty object check
	function isEmpty(obj){
		return (Object.getOwnPropertyNames(obj).length === 0);
	}

}
