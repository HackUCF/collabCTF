$(document).ready(function() {
    $('section[role=main]').find('form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serialize();
        var resultId = this.id.replace('-form', '-result');
        $.post(this.action, data, function(jdata){
            $('#' + resultId).text(jdata['result']);
        });
    });
});