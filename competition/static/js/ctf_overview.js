"use strict";
$(document).ready(function () {
    $('#challenges').find('tbody').find('tr').on('click', function(event) {
        event.preventDefault();
        document.location = $(this).data('href');
    });
});