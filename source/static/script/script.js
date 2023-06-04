$(document).ready(function(){
        
    var display_table = $('#display_table').DataTable();

    $('#display_table tbody').on('click', 'td', function(){
            
            var column_index = display_table.cell(this).index().column
            var column_header = display_table.column(column_index).header()
            const modification = $(column_header).html() + '='
            document.getElementById("modification").value = modification
            
            var conditions = []
            var row_index = display_table.cell(this).index().row
            var keys = primary_keys.split(',')
            for(index = 0; index < keys.length; index++){
                const key = keys[index]
                var key_header = display_table.column(key).header()
                const condition = $(key_header).html() + '=' + display_table.row(row_index).data()[key]
                conditions.push(condition)
            }
            document.getElementById("condition").value = conditions.join(' and ')
            
        }
    );

});

function comfirm() {
    if (confirm("Comfirm for execution?")) {
        return true;
    }
    else {
        return false;
    }
}
