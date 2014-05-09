(function () {
    var $deleteModal = $('.delete-modal');
    $deleteModal.find('input[type=reset]').on('click', function (event) {
        event.preventDefault();
        $deleteModal.foundation('reveal', 'close');
    });
})();