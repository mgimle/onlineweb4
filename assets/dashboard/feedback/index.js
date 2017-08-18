import jQuery from 'jquery';

const addFeedback = ( function ($) {

    let addFields;
    return {
        init() {
            addFields = $('.new-question')

          // Bind click listener for search button
          addFields.on('click', (e) => {
            console.log("click")
          });

       }
    }

    // Number of inputs to create
    var number = document.getElementById("member").value;
    // Container <div> where dynamic content will be placed
    var container = document.getElementById("container");
    // Clear previous contents of the container
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        // Append a node with a random text
        container.appendChild(document.createTextNode("Member " + (i+1)));
        // Create an <input> element, set its type and name attributes
        var input = document.createElement("input");
        input.type = "text";
        input.name = "member" + i;
        container.appendChild(input);
        // Append a line break
        container.appendChild(document.createElement("br"));
    }
}(jQuery));

addFeedback.init();
