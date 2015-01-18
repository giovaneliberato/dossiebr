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

            $scope.addArticleToGrid = function(url, tags){
                var mentions = tags.filter(function(tag){ return tag[0] === '@'});
                var tags = tags.filter(function(tag){ return tag[0] === '#'});
                $scope.articles.unshift({'url': url, 'tags': tags, 'mentions': mentions});
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
                var url = $scope.getImageUrl(data.thumbnail_url);
                $scope.article.thumbnail_url = url;
            })

            $scope.getImageUrl = function(url){
                var defaultImg = 'http://lorempixel.com/g/300/150/abstract/';
                var imgServiceUrl = 'http://wit.wurfl.io/w_300/h_200/m_cropbox/';
                var articleImgUrl = imgServiceUrl + url;

                if (!url)
                    return defaultImg;
                
                request = new XMLHttpRequest();
                request.open("GET", articleImgUrl, false);
                request.send(null);
                if (request.status != 200)
                    return defaultImg;

                return articleImgUrl;
            }
        }
    }
})
