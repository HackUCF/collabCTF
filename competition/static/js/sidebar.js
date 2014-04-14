$(document).ready(function() {
    var $sidebar = $('#sidebar');
    $sidebar.hide();
    // get the sidebar
    var xhr = $.ajax({
        url: '/sidebar?url=' + location.pathname,
        cache: false
    });
    xhr.done(function(data) {
        $sidebar.html(data);
        $sidebar.fadeIn('fast');
    });

});