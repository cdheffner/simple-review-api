$(document).ready(function(){

	$('.navpill').click(function(){
		$('.navpill').parents().removeClass('active');
		$(this).parent().addClass('active');
	})

})