app.factory('reviewerFactory', function($http){

	function ReviewerFactory(){};

	ReviewerFactory.prototype.create = function(newReviewer, callback) {
		$http.post('/register', newReviewer)
			.then(function(result){
				if (result.data.errors){
					return result.data;
				} else {
					return result.data;
				}
			})
	};
	
	return new ReviewerFactory();
})
