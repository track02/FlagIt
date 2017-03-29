/*
*Script is called each time body is loaded
*Retrieves the check array which denotes which flags have been already matched
*Sets appropiate class for each image depending on returned check arrays (found / not found)
*Binds onclick and onhover event handlers to each flag image
*/

function init_setup(country_name, country_regions){

	//Begin by retrieving the check array promise
	var check_promise = browser.storage.local.get(country_name);

	//Resolve the promise, process check array and setup page
	check_promise.then(setup);

  /*-------------------Function Defs----------------------*/
  //close functions inside init_setup giving them access 
  //to initial parameters (country_name, country_regions)

	//Event handler for onclick
	//Swaps the className of the parent cell to toggle transparency
	//missing -> found
	//found -> missing
	function checkHandler(event){
		target = event.target; //Retrieve image that has been clicked
		parent = target.parentElement;

		index = parent.id; //The index to update is found by examining the parent id (region name)
		value = false;

		if(parent.className == "missing"){
		  parent.className = "found"
		  value = true;
		}else {
		  parent.className = "missing"
		}

		//Write this to the check array
		var result_promise = browser.storage.local.get(country_name);
		result_promise.then(updateResults);

		//Update check array - closed inside checkHandler, allows value to be used in update process
		//Closed within checkHandler, has access to the required value 
		function updateResults(check_obj){

		  //When item is retrieved update it using the index and value
		  check_obj[country_name][index] = value;

		  let set = browser.storage.local.set(check_obj);
		  set.then();
		}
	}

	//Setup function firstly generates the map structure required to track flags (associative array)
	//If no previous data is found (first time page is loaded) then a blank mapping will be made
	//If updating from a previous version (using check array) this is converted to a map
	//If a previous map is found then all valid flags are copied over into a new map of the correct size 
	function setup(check_obj) {

		//Empty check object or length difference
		if(isEmpty(check_obj)){
			//Generate empty array of blank arrayss
			var blank_mapping = {};

			//mapping of country_name -> 0
			//Iterate over all td elements and extract id's
			var flag_table = document.getElementById("flag-table");
			var flag_cells = flag_table.getElementsByTagName("td");

			for(var i = 0; i < flag_cells.length; i++){
				blank_mapping[flag_cells[i].id] = false;
			}
			
			//Assign the mapping to provided name (country name)
			var obj = {};
			obj[country_name] = blank_mapping;
			let set = browser.storage.local.set(obj);

			//Attempt to store the array
			set.then();

			//Bind event handlers and set correct class using the blank_mapping
			setupTable(blank_mapping);
		}
		else{

			//Pull out already populated array from results_obj
			check_mapping = check_obj[country_name];

			//One off operation for upgrade from V0.37
			//Remove in V0.40++
			//Convert previous 0/1 array into new associative array
			//Then rebuild using latest flags
			if(Array.isArray(check_mapping)){

				var blank_mapping = {};
				//First populate the blank array
				var flag_table = document.getElementById("flag-table");
				var flag_cells = flag_table.getElementsByTagName("td");

				for(var i = 0; i < flag_cells.length; i++){
					blank_mapping[flag_cells[i].id] = Boolean(check_mapping[i]);
				}

				//Overwrite old array with new map
				//Carry on with rebuild as normal
				check_mapping = blank_mapping;
			}

			//We'll rebuild using current page contents, ensures that flags are up to date
			var blank_mapping = {};
			//First populate the blank array
			var flag_table = document.getElementById("flag-table");
			var flag_cells = flag_table.getElementsByTagName("td");

			for(var i = 0; i < flag_cells.length; i++){
				blank_mapping[flag_cells[i].id] = false;
			}

			//Now loop over each key in the old array
			var keys = Object.keys(check_mapping)
			for(var i = 0; i < keys.length; i++){

				if(keys[i] in blank_mapping){
					blank_mapping[keys[i]] = check_mapping[keys[i]];
				}
			}

			var obj = {};
			obj[country_name] = blank_mapping;
			let set = browser.storage.local.set(obj);
			//Attempt to store the array
			set.then();

			//Bind event handlers and set correct class using the populated array
			setupTable(blank_mapping);			
		}
	}

	//Binds onhover and onclick event handlers to each img in the table
	//Sets correct class to cells (missing / found)
	function setupTable(check_mapping){

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
		  if(check_mapping[flag_cells[i].id]){
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
