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

function hoverBackArrow(element) {
  element.setAttribute('src', '/static/img/leftArrowFull.svg');
}

function unhoverBackArrow(element) {
  element.setAttribute('src', '/static/img/leftArrowEmpty.svg');
}

function hoverHeartLike(element) {
  element.setAttribute('src', '/static/img/HeartLikeFull.svg');
}

function unhoverHeartLike(element) {
  element.setAttribute('src', '/static/img/HeartLikeEmpty.svg');
}