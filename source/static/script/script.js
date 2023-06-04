$(document).ready(
    function(){
        $('#display_table').DataTable(
        );
    }
);

function comfirm() {
    if (confirm("Comfirm for execution?")) {
        return true;
    }
    else {
        return false;
    }
}