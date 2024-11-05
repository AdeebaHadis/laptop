$(document).ready(function() {
    //display speaker message
    eel.expose(Displaymessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

// Display hood
eel.expose(ShowHood)
Function showHood() {
    $("#oval").attr("hidden",false);
    $("#siriwave").attr("hidden",true);
}
});