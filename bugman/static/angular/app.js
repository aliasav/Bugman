/* nmad module is defined here */
/* Define all states here using angular-ui router */
/* Do not define any controllers/services/utilities here, all controllers/services/utilities must go in their specific modules */

(function(){
	angular.module('bugman', ['ui.router', 'ngCookies', 'ngAnimate', 'bugman.controllers', 'ngResource', 'bugman.services'])

	// Changing interpolation start/end symbols.
	.config(function($interpolateProvider, $httpProvider){
     $interpolateProvider.startSymbol('[[').endSymbol(']]');
      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
 	})

	// CSRF token setting
	.run(function($http, $cookies){
		$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
	})

	/* All app states defined here, refer to angular-ui-router to understand concept of states */
	/* Use inheritence whereever needed, use ui-sref in templates rather than URLs */

	.config(function($stateProvider, $urlRouterProvider){
		$stateProvider

		.state('app', {
			url: "/",
			templateUrl: "templates/landing_page/home.html",
		});

		// if none of the above states are matched, use this as the fallback
  		$urlRouterProvider.otherwise('/app/home');
	})

	.config(['$resourceProvider', function($resourceProvider){
		// Don't strip trailing slashes from calculated URLs
		$resourceProvider.defaults.stripTrailingSlashes = false;
	}])

	.constant('SERVER', {

	})

	.constant('SERVER1', {

	})


})();