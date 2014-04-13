$(document).ready(function() {
    var $sidebar = $('#sidebar');
    $sidebar.hide();
    // get the sidebar
    $.get('/sidebar?url=' + location.pathname, function(data) {
        $sidebar.html(data);
        $sidebar.fadeIn('fast');
    });
});