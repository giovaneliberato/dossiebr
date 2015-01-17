var mod = angular.module('Thumbnails', ['HomeRestApi']);


mod.directive('thumbnailGrid', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/thumbnail_grid.html",
        controller: function($scope, HomeRestApi) {
            $scope.splitArticles = function(){
                if (!$scope.articles) return;

                $scope.splittedArticles = []
                var articles = $scope.articles.slice(0);
                while (articles.length) {
                    $scope.splittedArticles.push(articles.splice(0, 3))
                }
            }

            $scope.addArticleToGrid = function(url){
                $scope.articles.unshift(url);
                $scope.splitArticles();
            }

            HomeRestApi.getUserArticles().success(function(data){
                $scope.articles = data.articles;
                $scope.splitArticles();
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
            article: '=',
        },
        controller: function($scope, HomeRestApi) {
            HomeRestApi.getPreviewData($scope.article.url).success(function(data){
                $scope.article.title = data.title;
                $scope.article.description = data.description;
                $scope.article.thumbnail_url = data.thumbnail_url;
            })
        }
    }
})
