app.controller('newController', function($scope, $location, reviewerFactory){

	var self = this;
	$scope.success = false;
	$scope.failure = false;

	this.register = function(){
		$scope.errors = [];
		reviewerFactory.create($scope.form, function(response){
			if (response.errors){
				$scope.errors = response.errors;
			} else {
				$scope.token = response.token;
			}
		})
	}

})
