
function hoverBackArrow(element) {
  element.setAttribute('src', '/static/img/leftArrowFull.svg');
}

function unhoverBackArrow(element) {
  element.setAttribute('src', '/static/img/leftArrowEmpty.svg');
}

function like(ID, img){
  $.ajax({
			type: 'POST',
			url: 'challengeLike/'+ID,
		}).done(function(data) {
		    var hidden = $('#inputnr'+ID);
		    if(hidden.val() == 0){
                hidden.val(1);
                img.setAttribute('src', '/static/img/HeartLikeFull.svg');
                var likeScore = document.getElementById('likeCount'+ID);
                console.log(likeScore);
                var number = likeScore.innerHTML;
                number++;
                likeScore.innerHTML = number;
            }
            else{
                hidden.val(0);
                img.setAttribute('src', '/static/img/HeartLikeEmpty.svg');
                var likeScore = document.getElementById('likeCount'+ID);
                console.log(likeScore);
                var number = likeScore.innerHTML;
                number--;
                likeScore.innerHTML = number;
            }
			console.log('done: '+data);
		}).fail(function(data) {
			// Aktionen bei einem Fehler
			console.log('fail: '+data);
		});

}

function likevote(ID, img){
  $.ajax({
			type: 'POST',
			url: 'challengeLike/'+ID,
		}).done(function(data) {
		    var hidden = $('#inputnr'+ID);
		    if(hidden.val() == 0){
                hidden.val(1);
                img.setAttribute('src', '/static/img/HeartLikeFull.svg');
            }
            else{
                hidden.val(0);
                img.setAttribute('src', '/static/img/HeartLikeEmpty.svg');
            }
			console.log('done: '+data);
		}).fail(function(data) {
			// Aktionen bei einem Fehler
			console.log('fail: '+data);
		});

}
