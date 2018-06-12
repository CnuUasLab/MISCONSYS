/*
  *******************************************
  *   Dasboard controller and functionality *
  *                                         *
  *           Author: davidkroell           *
  *          Version: 1.2.0                 *
  *                                         *
  *******************************************
*/

angular.module('MISCONSYS')
    .config(['$routeProvider', '$locationProvider',
        function($routeProvider, $locationProvider) {

	    // Route functionality for the Angular module
	    // on the Dashboard page.
	    
	    $routeProvider
		.when('/', {
		    templateUrl: './dashboard/dashboard.html',
		    controller: 'DashController',
		    controllerAs: 'vm',
		    css: './dashboard/dashboard.css'
		});
	}
    ])

    .controller("DashController", function($scope) {
	var vm = this;


	
    }
);
