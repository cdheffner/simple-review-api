app.controller('retrieveController', function($scope, $location, reviewFactory){

	var self = this;

	this.retrieve = function(){
		reviewFactory.index($scope.token, function(response){
			console.log(response);
		})
	}

})
