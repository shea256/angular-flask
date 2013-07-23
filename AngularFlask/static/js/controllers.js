'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
	$scope.postsQ = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function PostDetailController($scope, $routeParams, Post) {
	$scope.postId = $routeParams.postId;
	$scope.post = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.postTitle = post.title;
		$scope.postBody = post.body;
	}, function(response, responseHeaders) {
	})
	;

}
