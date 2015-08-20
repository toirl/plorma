$( document ).ready(function() {
    $('table.sortable tbody').sortable({
        cancel: 'th',
        helper: fixWidthHelper,
        stop: stopSortListener
    }).disableSelection();

    function fixWidthHelper(e, ui) {
        ui.children().each(function() {
            $(this).width($(this).width());
        });
        return ui;
    };

    function stopSortListener(e, ui) {
        var data = $('table.sortable tbody').sortable('toArray', {attribute: "id"});
    }
});
