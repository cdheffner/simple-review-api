app.controller('tokenController', function($scope, $location, reviewerFactory){

	var self = this;

	$scope.form = {
		'email': '',
		'password': '',
	}

	this.getToken = function(){
		reviewerFactory.getToken($scope.form, function(response){
			if (response.errors){
				$scope.errors = response.errors;
			} else {
				$scope.errors = false;
				$scope.form = {
					'email': '',
					'password': '',
				}
				$scope.token = response.token;
			}
		})
	}

})
