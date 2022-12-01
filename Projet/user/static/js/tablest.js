


    $(document).ready(function() {
        var table = $('#example').DataTable( {
          /*export files*/ 
          "columnDefs": [ 
        
            {
                "targets": [ 6 ],
                "searchable": false,
                'orderable': false,
            }
            ,
            {
                "targets": [ 7 ],
                "searchable": false,
                'orderable': false
            }
        ],
            dom: 'Blfrtip',
            lengthMenu: [
                [ 10, 25, 50, 100 ],
                [ '10', '25', '50', '100' ]
                ],
              buttons:[
           "copy", 'pdf', 'excel','print'
          ]
          ,
        "oLanguage": {
          "sSearch": "Rechercher" //search
        },
        "language": { "lengthMenu": "Afficher _MENU_", 
         "zeroRecords": "Aucun enregistrement trouvé", 
         "info": " ", 
         "paginate": {
            "previous": "<<",
            "next": ">>"  },
         "infoEmpty": " ",
         "infoFiltered": "" 
        }   
      } );
      /*
      .dataTables_wrapper .dataTables_info {visibility:hidden}*/   
      $('.buttons-excel span').html("<i class='fa fa-file-excel-o' aria-hidden='true'></i> <br> <span class='petit'>Excel</span>")
      $('.buttons-print span').html("<i class='fa fa-print' aria-hidden='true'></i>  <br> <span class='petit'>Editer</span>")
      $('.buttons-copy span').html("<i class='fa fa-clone' aria-hidden='true'></i>  <br> <span class='petit'>Copier</span>")
      $('.buttons-pdf span').html("<i class='fa fa-file-pdf-o' aria-hidden='true'></i>  <br> <span class='petit'>Pdf</span>")
        
      

       
       /* ----search column---*/
        $('#example tfoot th').each( function () {
            var title = $('#example thead th').eq( $(this).index() ).text();
            $(this).html( '<input type="text" placeholder="  '+title+'" />' );
        } );
     
        // DataTable
        var table = $('#example').DataTable();
     
        // Apply the filter
        table.columns().eq( 0 ).each( function ( colIdx ) {
            $( 'input', table.column( colIdx ).footer() ).on( 'keyup change', function () {
                table
                    .column( colIdx )
                    .search( this.value )
                    .draw();
            } );
        } );
    
      /***** show hide columns ****/
    
        $('a.toggle-vis').on( 'click', function (e) {
            e.preventDefault();
            $(this).toggleClass( "blue" )
            $(this).toggleClass( "grey" )
            // Get the column API object
            var column = table.column( $(this).attr('data-column') );
     
            // Toggle the visibility
            column.visible( ! column.visible() );
        } );
    
    
    } );
    
    

