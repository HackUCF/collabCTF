"use strict";
$(document).ready(function () {
    $('#challenges').find('tbody').find('tr').on('click', function (event) {
        event.preventDefault();
        document.location = $(this).data('href');
    });

    var xhr = $.ajax({
        url: '.chart',
        cache: false
    });
    xhr.done(function (data) {
        var solvedMetr = new Metr($('#solved-container'), {
            background: true,
            colors: ['#D00000', '#A00000'],
            progress: [60, 88]
        });
        var timeMetr = new Metr($('#time-container'), {
            background: true,
            colors: ['#C0C000', '#A0A000'],
            progress: [17, 72]
        });
        var usersMetr = new Metr($('#users-container'), {
            background: true,
            colors: ['#0000D0', '#0000A0'],
            progress: [38, 65]
        });
        var pointsMetr = new Metr($('#points-container'), {
            background: true,
            colors: ['#00D000', '#00A000'],
            progress: [27, 53]
        });
        var a = 0, b = 0;
        setInterval(function () {
            timeMetr.update([a, b]);
            a = a < 100 ? a + 1 : 0;
            b = b < 100 ? b + 2 : 0;
        }, 33);
    })
});