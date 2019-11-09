$("#submitButton").click(function(){
    var objectData =
         {
             data1: $("#data1").val(),
             data2: $("#data2").val()
         };

    var objectDataString = JSON.stringify(objectData);
    $.ajax({
        url: "/challenge",
        method:'POST',
        dataType: 'json',
        processData: false,
        contentType: 'application/json',
        data: objectDataString,
    })
    .done(function( msg ) {
        alert( "Data Saved: " + msg );
    });
});