var mod = angular.module('Thumbnails', ['HomeRestApi']);


mod.directive('thumbnailGrid', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/thumbnail_grid.html",
        scope: {},
        controller: function($scope, HomeRestApi) {
            HomeRestApi.getUserArticles().success(function(data){
                $scope.articles = [];
                while (data.articles.length) {
                    $scope.articles.push(data.articles.splice(0, 3))
                }                
            })
        }
    }
    
})

mod.directive('thumbnail', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/thumbnail.html",
        scope: {
            url: '=',
        },
        controller: function($scope, HomeRestApi) {
            HomeRestApi.getPreviewData($scope.url).success(function(data){
                $scope.title = data.title;
                $scope.description = data.description;
                $scope.thumbnail_url = data.thumbnail_url;
            })
        }
    }
})
