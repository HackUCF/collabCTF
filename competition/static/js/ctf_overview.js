"use strict";
$(document).ready(function () {
    $('#challenges').find('tbody').find('tr').on('click', function (event) {
        event.preventDefault();
        document.location = $(this).data('href');
    });

    function timePercentage(startTime, endTime) {
        var nowUTC = new Date().getTime();
        var totalTime = endTime - startTime;
        var nowAdjusted = nowUTC - startTime;
        return nowAdjusted / totalTime;
    }

    var xhr = $.ajax({
        url: '.chart',
        cache: false
    });

    xhr.done(function (data) {
        var challenges = data['challenges'];
        var points = data['points'];
        var users = data['users'];
        var startTime = data['start_time'] * 1000;
        var endTime = data['end_time'] * 1000;
        var solvedMetr = new Metr($('#solved-container'), {
            background: true,
            colors: ['#D00000', '#A00000'],
            progress: [challenges['solved'] / challenges['total'] * 100, (challenges['solved'] + challenges['in_progress']) / challenges['total'] * 100]
        });
        var timeMetr = new Metr($('#time-container'), {
            background: true,
            colors: ['#C0C000', '#A0A000'],
            progress: [timePercentage(startTime, endTime) * 100, 100]
        });
        var usersMetr = new Metr($('#users-container'), {
            background: true,
            colors: ['#0000D0', '#0000A0'],
            progress: [users['participating'] / users['total'] * 100, 100]
        });
        var pointsMetr = new Metr($('#points-container'), {
            background: true,
            colors: ['#00D000', '#00A000'],
            progress: [points['earned'] / points['total'] * 100, points['in_progress'] / points['total'] * 100]
        });


        // time circle thing updates every second
        var timeInterval = setInterval(function () {
            var tp = timePercentage(startTime, endTime);
            console.log(tp);
            timeMetr.update([tp * 100, 100]);
            if (tp > 1) {
                clearInterval(timeInterval);
                console.log("Stopping time update - CTF has ended");
            }
        }, 1000);
    });

    $.post('/.challenge-visit', {url: location.pathname});
});