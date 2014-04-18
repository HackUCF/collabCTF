$(document).ready(function() {
    $('.datetimeinput').datetimepicker({
        format:'Y-m-d H:m:s'
    });
    new Chat($('#chat'));
});
