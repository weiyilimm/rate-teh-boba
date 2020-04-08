
$(document).ready(function() {
    $(."nav-item nav-link").hover(
        function() {
            $(this).css('color', 'black');
    },
    function() {
        $(this).css('color', 'white');
});
});