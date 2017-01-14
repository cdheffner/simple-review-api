app.controller('submitController', function($scope, $location, reviewFactory){

	var self = this;

	this.submit = function(){
		$scope.success = false;
		reviewFactory.submit($scope.form, function(response){
			if (response.errors){
				$scope.errors = response.errors;
			} else {
				$scope.errors = false;
				$scope.form = {
					'token': '',
					'title': '',
					'company': '',
					'rating': '',
					'summary': ''
				};
				$scope.success = response.success;
			}
		})
	}

})
