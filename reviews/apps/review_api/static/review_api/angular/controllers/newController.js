app.controller('newController', function($scope, $location, reviewerFactory){

	var self = this;
	$scope.form = {
		'first_name': '',
		'last_name': '',
		'email': '',
		'password': '',
		'password_confirm': ''
	}

	this.register = function(){
		reviewerFactory.create($scope.form, function(response){
			if (response.errors){
				$scope.errors = response.errors;
			} else {
				$scope.errors = false;
				$scope.form = {
					'first_name': '',
					'last_name': '',
					'email': '',
					'password': '',
					'password_confirm': ''
				}
				$scope.token = response.token;
			}
		})
	}

})
