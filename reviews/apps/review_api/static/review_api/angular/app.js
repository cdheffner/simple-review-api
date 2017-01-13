var app = angular.module('reviewApp', ['ngRoute']);

app.config(function($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: '/partials/index.html',
			controller: 'reviewController',
			controllerAs: 'rC'
		})
		.otherwise({
			redirectTo: '/'
		})
})
