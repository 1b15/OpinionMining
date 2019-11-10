jQuery(document).ready(function($)
{
	$("#FormButton").click(function(event) {
		// Standard-Aktion abbrechen
		event.preventDefault();
        // Get form
        var form = $('#main')[0];

		// Create an FormData object
        var data = new FormData(form);

		// disabled the submit button
        $("#FormButton").prop("disabled", true);

		$.ajax({
			type: 'POST',
			url: form['action'],
			enctype: 'multipart/form-data',
            data: data,
            processData: false,
            contentType: false,
		}).done(function(data) {
			// Aktionen bei Erfolg
            document.location.reload();
			console.log('done: '+data);
		}).fail(function(data) {
			// Aktionen bei einem Fehler
			console.log('fail: '+data);
		});
	});
});