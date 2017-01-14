app.factory('reviewerFactory', function($http){

	function ReviewerFactory(){};

	ReviewerFactory.prototype.create = function(newReviewer, callback) {
		$http.post('/register', newReviewer)
			.then(function(result){
				callback(result.data);
			})
	};

	ReviewerFactory.prototype.getToken = function(info, callback) {
		$http.post('/token', info)
			.then(function(result){
				callback(result.data);
			})
	};
	
	return new ReviewerFactory();
})
