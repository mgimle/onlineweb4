import  AddFeedback from './feedbackNew';
import AddMultipleChoice from './feedbackNewMC';

if(window.location.pathname.match(/dashboard\/feedback\/new_mc\//)) {
    AddMultipleChoice.init();
}
else if (window.location.pathname.match(/dashboard\/feedback\/new\//)){
    AddFeedback.init();
}
