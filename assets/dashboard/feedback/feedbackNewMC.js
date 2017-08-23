import jQuery from 'jquery';

const AddMultipleChoice = ( function ($) {
    var addChoice;

    var container;
    var choiceForm;

    var choiceContainer;

    var choiceFormCount;

    var formAppend;

    return {
        init() {
            choiceFormCount = 0;
            container = document.getElementById("form-fields");
            choiceContainer = document.getElementById("choice-container");
            choiceForm = document.getElementById("choice-generator");

            container.removeChild(choiceForm);

            addChoice = $('.new-choice-question');

            // Bind click listener for add question button
            addChoice.on('click', (e) => {
                AddMultipleChoice.newChoice();
            });
        },
        newChoice() {
            formAppend = choiceForm.cloneNode(true);
            formAppend.id = "choice-form-" + choiceFormCount;

            var i;
            for (i = 0; i < formAppend.childNodes.length; i++) {
                try {
                    formAppend.childNodes[i].querySelector("#id_text_display").value = choiceFormCount;
                }
                catch (e) {
                    continue;
                }
            }
            choiceContainer.appendChild(formAppend);
            choiceFormCount += 1;
        },
    }
}(jQuery));

export default AddMultipleChoice;
