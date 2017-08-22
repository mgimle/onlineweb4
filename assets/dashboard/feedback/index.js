import jQuery from 'jquery';

const AddFeedback = ( function ($) {
    var addTextQuestion;
    var addRatingQuestion;

    var textQuestionForm;
    var ratingQuestionForm;

    var container;
    var textQuestionContainer;
    var ratingQuestionContainer;

    var textFormCount;
    var ratingFormCount;

    var formAppend;

    return {
        init() {
            textFormCount = 0;
            ratingFormCount = 0;
            container = document.getElementById("form-fields");
            textQuestionContainer = document.getElementById("text-question-container");
            ratingQuestionContainer = document.getElementById("rating-question-container")
            textQuestionForm = document.getElementById("text-question-generator");
            ratingQuestionForm = document.getElementById("rating-question-generator");

            container.removeChild(textQuestionForm);
            container.removeChild(ratingQuestionForm);

            addTextQuestion = $('.new-text-question');
            addRatingQuestion = $('.new-rating-question');

            // Bind click listener for add question button
            addTextQuestion.on('click', (e) => {
                AddFeedback.newTextQuestion();
            });

            // Bind click listner for add rating question button
            addRatingQuestion.on('click', (e) => {
               AddFeedback.newRatingQuestion();
            });
        },
        newTextQuestion() {
            formAppend = textQuestionForm.cloneNode(true);
            formAppend.id = "question-form-" + textFormCount;

            // Iterate through the child nodes of question to find the checkbox,
            // then adds a unique value to the checkbox, so it is possible to check
            // which questions had the checkbox checked and which did not
            var i;
            for (i = 0; i < formAppend.childNodes.length; i++) {
                try {
                    formAppend.childNodes[i].querySelector("#id_display").value = textFormCount;
                }
                catch (e) {
                    continue;
                }
            }
            textQuestionContainer.appendChild(formAppend);
            textFormCount += 1;
        },
        newRatingQuestion() {
            formAppend = ratingQuestionForm.cloneNode(true);
            formAppend.id = "rating-form-" + ratingFormCount;

            var i;
            for (i = 0; i < formAppend.childNodes.length; i++) {
                try {
                    formAppend.childNodes[i].querySelector("#id_display").value = ratingFormCount;
                }
                catch (e) {
                    continue;
                }
            }
            ratingQuestionContainer.appendChild(formAppend);
            ratingFormCount += 1;
        },
    }
}(jQuery));

AddFeedback.init();
