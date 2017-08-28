import jQuery from 'jquery';

const AddFeedback = ( function ($) {
    var addTextQuestion;
    var addRatingQuestion;
    var addMultipleChoice;

    var textQuestionForm;
    var ratingQuestionForm;
    var multipleChoiceForm;

    var container;
    var textQuestionContainer;
    var ratingQuestionContainer;
    var multipleChoiceContainer;

    var textFormCount;
    var ratingFormCount;
    var multipleChoiceCount;

    var formAppend;

    return {
        init() {
            textFormCount = 0;
            ratingFormCount = 0;
            multipleChoiceCount = 0;

            container = document.getElementById("form-fields");
            textQuestionContainer = document.getElementById("text-question-container");
            ratingQuestionContainer = document.getElementById("rating-question-container");
            multipleChoiceContainer = document.getElementById("multiple-choice-container");

            textQuestionForm = document.getElementById("text-question-generator");
            ratingQuestionForm = document.getElementById("rating-question-generator");
            multipleChoiceForm = document.getElementById("multiple-choice-generator");

            container.removeChild(textQuestionForm);
            container.removeChild(ratingQuestionForm);
            container.removeChild(multipleChoiceForm);

            addTextQuestion = $('.new-text-question');
            addRatingQuestion = $('.new-rating-question');
            addMultipleChoice = $('.new-mc-question');

            // Bind click listener for add question button
            addTextQuestion.on('click', (e) => {
                AddFeedback.addElement(textQuestionForm, textQuestionContainer,textFormCount,
                    "#id_text_display");
            });

            // Bind click listener for add rating question button
            addRatingQuestion.on('click', (e) => {
               AddFeedback.addElement(ratingQuestionForm, ratingQuestionContainer,ratingFormCount,
                   "#id_rating_display");
            });

            // Bind click listener for add mutiple choice question
            addMultipleChoice.on('click', (e) => {
                AddFeedback.addElement(multipleChoiceForm, multipleChoiceContainer,textFormCount,
                    "#id_mc_relation_display");
            });
        },
        addElement(htmlElement, elementContainer, count, queryTxt) {
            formAppend = htmlElement.cloneNode(true);

            var i;
            for (i=0; i<formAppend.childNodes.length; i++) {
                try {
                    formAppend.childNodes[i].querySelector(queryTxt).value = count;
                }
                catch  (e) {
                    continue;
                }
            }
            elementContainer.appendChild(formAppend);
            count += 1;
        }
    }
}(jQuery));

export default AddFeedback;
