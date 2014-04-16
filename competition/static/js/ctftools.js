$(document).ready(function() {
    $('#base-conversion-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serialize();
        var resultId = this.id.replace('-form', '-result');
        $.post(this.action, data, function(jdata){
            $('#' + resultId).text(jdata['result']);
        });
    });
});

$(document).ready(function() {
    $('#xor-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serialize();
        var resultId = this.id.replace('-form', '-result');
        $.post(this.action, data, function(jdata){
            $('#' + resultId).text(jdata['result']);
        });
    });
});

$(document).ready(function() {
    $('#hash-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serialize();
        var resultId = this.id.replace('-form', '-result');
        $.post(this.action, data, function(jdata){
            $('#' + resultId).text(jdata['result']);
        });
    });
});

$(document).ready(function() {
    $('#rot-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serialize();
        var resultId = this.id.replace('-form', '-result');
        $.post(this.action, data, function(jdata){
            $('#' + resultId).text(jdata['result']);
        });
    });
});