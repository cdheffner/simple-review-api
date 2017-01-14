app.factory('reviewFactory', function($http){

	function ReviewFactory(){};

	ReviewFactory.prototype.submit = function(submission, callback) {
		$http.post('/submit', submission)
			.then(function(result){
				callback(result.data);
			})
	};
	
	ReviewFactory.prototype.index = function(token, callback) {
		url = '/retrieve/' + token;
		$http.get(url)
			.then(function(result){
				callback(result.data)
			})
	};

	return new ReviewFactory();
})

