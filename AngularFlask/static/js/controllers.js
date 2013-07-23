'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function PostDetailController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}
