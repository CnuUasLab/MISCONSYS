/*

*/


angular.module('MISCONSYS')
    .config(['$routeProvider', '$locationProvider',
	     function($routeProvider, $locationProvider) {

		 // Route functionality for the interop
		 // section of the application

		 $routeProvider
		     .when('/plane', {
			 templateUrl: './plane/plane.html',
			 controller: 'PlaneController',
			 controllerAs: 'vm',
			 css: './plane/plane.css'
		     });	 
	     }])
	    .controller("PlaneController", function($scope) {
		var vm = this;
		
	    });
