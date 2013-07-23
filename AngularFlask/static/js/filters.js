'use strict';

/* Filters */

angular.module('angularFlaskFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});