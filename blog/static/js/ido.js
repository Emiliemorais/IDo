$(document).ready(function() {

  $("#notification_read").click( function(event) {
    mark_notification_as_read();
  });
})

function mark_notification_as_read(){
    var id = $("#notification_id").val();
  	var url_post = $( "#urlaccess" ).html()
	$.ajax({
		type:"POST",
		url: url_post,
		data: {
		    'notification_id': id,
		},
	    beforeSend: function(xhr, settings) {
			var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        	xhr.setRequestHeader("X-CSRFToken", token);
      	},
		success: function(){
		}
	});
}
