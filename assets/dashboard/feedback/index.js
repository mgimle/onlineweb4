import jQuery from 'jquery';

const addFeedback = ( function ($) {
    var addFields;
    var questionForm;
    var container;
    var formCount;
    var submitAll;
    var formAppend;

    return {
        init() {
            formCount = 0;
            container = document.getElementById("form-fields");
            questionForm = document.getElementById("questions");
            container.removeChild(questionForm);

            addFields = $('.new-question');
            submitAll = $('.submit');

            // Bind click listener for add question button
            addFields.on('click', (e) => {
                formAppend = questionForm.cloneNode(true);
                formAppend.id = "question-form-" + formCount;
                var i;
                for (i=0; i<formAppend.childNodes.length; i++) {
                    try {
                        formAppend.childNodes[i].querySelector("#id_display").value = formCount;
                    }
                    catch (e) {
                        continue;
                    }
                }
                container.appendChild(formAppend);
                formCount += 1;
            });
        }
    }
}(jQuery));

addFeedback.init();
