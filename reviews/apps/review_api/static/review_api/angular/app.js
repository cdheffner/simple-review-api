var app = angular.module('reviewApp', ['ngRoute']);

app.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{/');
	$interpolateProvider.endSymbol('/}');
})

app.config(['$httpProvider', function ($httpProvider) {
	$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);

app.config(function($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: 'static/review_api/angular/partials/register.html',
			controller: 'newController',
			controllerAs: 'nC'
		})
		.when('/register', {
			templateUrl: 'static/review_api/angular/partials/register.html',
			controller: 'newController',
			controllerAs: 'nC'
		})
		.when('/gettoken', {
			templateUrl: 'static/review_api/angular/partials/token.html',
			controller: 'tokenController',
			controllerAs: 'tC'
		})
		.when('/submit', {
			templateUrl: 'static/review_api/angular/partials/submit.html',
			controller: 'submitController',
			controllerAs: 'sC'
		})
		.when('/retrieve', {
			templateUrl: 'static/review_api/angular/partials/retrieve.html',
			controller: 'retrieveController',
			controllerAs: 'rC'
		})
		.otherwise({
			redirectTo: '/'
		})
})
