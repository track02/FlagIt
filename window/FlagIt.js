//First pull results array (or add new one if it doesn't exist)
var result_promise = browser.storage.local.get("results");
result_promise.then(setup, error);

//When the promise is fulfilled, start setup
function setup(results_obj) {

  //Check if a results string was returned
  //If no results string is present - add a new one
  if(isEmpty(results_obj)){
    console.log("No results array");
    let set = browser.storage.local.set({results: new Array(250).fill(0)});
    set.then(addItem, error);
  }

  //Otherwise we have a results object, start processing
  else{

    //Pull out array from results_obj
    results_array = results_obj.results;

    //Extract table and cells
    var flag_table = document.getElementById("flag-table");
    var flag_cells = flag_table.getElementsByTagName("td");

    //Bind handler to onclick for each cell image
    //Determine cell class
    var cell_img;


    for(var i = 0; i < flag_cells.length; i++){

        //Extract child
        cell_img = flag_cells[i].children[0];

        //Get child id, used to lookup stored array
        img_no = cell_img.id;
        console.log(img_no);
        //Subtract one, zero indexed arrays
        img_no--;
        console.log(img_no);

        //Bind handler
        cell_img.onclick = checkHandler;

        //Determine class type
        //0 -> missing
        //1 -> found
        if(results_array[img_no] == 0){
          flag_cells[i].className = "missing";
        }
        else{
            flag_cells[i].className = "found";
        }

    }
  }
}



//Event handler for onclick
function checkHandler(event){
    target = event.target; //Retrieve image that has been clicked
    parent = target.parentElement;

    index = (event.target.id ) - 1;
    value = 0;


    console.log(target.parentElement)

    if(parent.className == "missing"){
      parent.className = "found"
      value = 1;
    }else {
      parent.className = "missing"
    }

    //Write this to the results array
    var result_promise = browser.storage.local.get("results");
    result_promise.then(updateResults, error);

    //Update results array
    function updateResults(results_obj){

      //When item is retrieved update it using the index and value
      results_obj.results[index] = value;
      let set = browser.storage.local.set(results_obj);
      set.then(addItem, error);

    }


}

//Empty object check
function isEmpty(obj){
    return (Object.getOwnPropertyNames(obj).length === 0);
}

//Fulfill error
function addItem(item){
  console.log("Done adding");
}

//Promise Error
function error(error) {
  console.log(`Error: ${error}`);
}
