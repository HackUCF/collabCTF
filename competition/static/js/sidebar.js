$(document).ready(function() {
    var $sidebar = $('#sidebar');
    $sidebar.hide();
    // get the sidebar
    var xhr = $.ajax({
        url: '/.sidebar?url=' + location.pathname,
        cache: false
    });
    xhr.done(function(data) {
        var $resp = $(data);
        $resp.hide();
        $sidebar.after($resp);
        $sidebar.remove();
        $resp.fadeIn('fast');
    });

});