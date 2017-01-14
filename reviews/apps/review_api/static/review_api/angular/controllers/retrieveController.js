app.controller('retrieveController', function($scope, $location, reviewFactory){

	var self = this;

	this.retrive = function(){
		reviewFactory.index(token, function(response){
			console.log(response);
		})
	}

})
