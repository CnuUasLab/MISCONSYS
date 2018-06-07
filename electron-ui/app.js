
/*

 *****************************************
 *   Root application for the MISCONSYS  *
 *         Ground Station System         *
 *                                       *
 *          Author: davidkroell          *
 *         Version: 1.0.0                *
 *                                       *
 *****************************************

*/

angular.module("MISCONSYS", ['ngRoute'])

    .config(['$routeProvider', '$locationProvider',
	     function($routeProvider, $locationProvider){

	$routeProvider
		 // Otherwise go to the root of the project.
		     .otherwise({ redirectTo: '/'})
		 // When route for the intro home page.
		     .when('./home', {
			 templateUrl:'./home/home.html',
			 controller: 'HomeController',
			 css: './home/home.css'
		     });
    }])

    .controller("AppController", function($scope) {
	var vm = this;

	// Continue with controller using the vm placeholder.
	// I use vm to represent a binding scope. This allows me
	// to eliminate the use of the stupid $scope variable.
	//
	// We can then decorate vm with the members that should be exposed
	// and data-binded to the view. This secures the code. If you use
	// $scope in AngularJS, you should be ashamed of yourself and read
	// johnpapa's article on AngularJS Controller As and the vm Variable.

	
    });

