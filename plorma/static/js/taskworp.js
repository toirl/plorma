$(function() {
    $('#taskworp button').click(function() {
        var taskid = $('#taskworp input').val();
        if (taskid) {
            window.location.href = "/tasks/update/"+taskid;
        }
    });
    $('#taskworp input').keypress(function (e) {
        var key = e.which;
        if (key == 13)  { // 13 is enter key.
            $('#taskworp button').click();
            return false;
        }
    });
});
