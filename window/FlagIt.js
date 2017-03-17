/*
*Script is called each time body is loaded
*Retrieves the check array which denotes which flags have been already matched
*Sets appropiate class for each image depending on returned check arrays (found / not found)
*Binds onclick and onhover event handlers to each flag image
*/

//Firstly retrieve the check array promise
var check_promise = browser.storage.local.get("check_array");

//Resolve the promise, if check array is retrieved then begin setup
//Otherwise call the error function (logs error)
check_promise.then(setup, error);

//Setup function determines whether the retrieved check object is empty (no array)
//If so, then a new empty array is created and stored in local
//Otherwise, the check array is extracted from the check object
//setupTable is then called with the check-array
function setup(check_obj) {

  //Empty check object
  if(isEmpty(check_obj)){
    //Generate empty array and attempty store it at check_array
    var blank_array = new Array(275).fill(1)
    let set = browser.storage.local.set({check_array: blank_array});

    //Attempt to store the array
    set.then(addItem, error);

    //Bind event handlers and set correct class using the blank_array
    setupTable(blank_array);
  }
  //Otherwise we have a results object
  else{

    //Pull out already populated array from results_obj
    check_array = check_obj.check_array;

    //Bind event handlers and set correct class using the populated array
    setupTable(check_array);
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
      if(check_array[img_no] == 0){
        flag_cells[i].className = "missing";
      }
      else{
          flag_cells[i].className = "found";
      }
  }
}

//hoverHandler
//Simply updates a paragraph element with the currently selected flag name
function hoverHandler(event){

  target = event.target;
  document.getElementById("hover_text").innerHTML = target.title;
}

//Event handler for onclick
//Swaps the className of the parent cell to toggle transparency
//missing -> found
//found -> missing
function checkHandler(event){
    target = event.target; //Retrieve image that has been clicked
    parent = target.parentElement;

    index = (event.target.id ) - 1;
    value = 0;

    if(parent.className == "missing"){
      parent.className = "found"
      value = 1;
    }else {
      parent.className = "missing"
    }

    //Write this to the check array
    var result_promise = browser.storage.local.get("check_array");
    result_promise.then(updateResults, error);

    //Update check array
    function updateResults(check_obj){

      //When item is retrieved update it using the index and value
      check_obj.check_array[index] = value;
      let set = browser.storage.local.set(check_obj);
      set.then(addItem, error);
    }
}

//Empty object check
function isEmpty(obj){
    return (Object.getOwnPropertyNames(obj).length === 0);
}

//Fulfill error
function addItem(item){
  console.log("Done adding item");
}

//Promise Error
function error(error) {
  console.log(`Error: ${error}`);
}
