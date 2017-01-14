app.controller('retrieveController', function($scope, $location, reviewFactory){

	var self = this;

	this.retrieve = function(){
		reviewFactory.index($scope.token, function(response){
			if (response.errors){
				$scope.errors = response.errors;
			} else {
				$scope.errors = false;
				$scope.reviews = response.reviews;
			}
		})
	}

})
