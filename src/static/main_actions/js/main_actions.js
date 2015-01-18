
var mod = angular.module('MainActions', ['mgcrea.ngStrap', 'HomeRestApi', 'ui.select']);

mod.directive('addLink', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/add_link.html",
        controller: function($scope, $alert, HomeRestApi) {
            $scope.data = {};
            $scope.form = {};
            $scope.data.foundTags = [];
            $scope.successAlertOptions = {
                animation: "am-fade-and-slide-top",
                content: 'Seu item foi salvo com sucesso!',
                placement: 'top',
                type: 'success',
                container: '.section',
                show: true,
                keyboard: true,
                duration: 3
            }

            $scope.errorAlertOptions = {
                animation: "am-fade-and-slide-top",
                content: 'Ocorreu um erro e nossa equipe foi avisada. Por favor, tente novamente.',
                placement: 'top',
                type: 'danger',
                show: true,
                container: '.section',
                keyboard: true,
                duration: 4
            }

            $scope.saveLink = function(callback){
                if ($scope.form.addlinkform.$valid) {
                    var url = $scope.data.url;
                    var tags = $scope.data.tags;
                    HomeRestApi.saveLink(url, $scope.data.tags).
                    success(function(){
                        $alert($scope.successAlertOptions);
                        callback();
                        $scope.form.addlinkform.submitted = true;
                        $scope.data = {};
                        $scope.addArticleToGrid(url, tags);
                        $scope.data.foundTags = [];
                    }).error(function(){
                        callback();
                        $alert($scope.errorAlertOptions);
                    })
                }                
            }

            $scope.searchTags = function(prefix){
                if (!prefix) return;

                return HomeRestApi.searchTags(prefix).then(function(result){
                    $scope.data.foundTags = result.data;
                });
            }
        }
    }
})

mod.filter('addHashPrefix', function() {
    return function(items, select) {
        if (select.search[0] != "#" && select.search[0] != "@" && select.search.length > 0){
            select.search = "#" + select.search;
        }
        return items;
    };
});

mod.directive('search', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/search.html",
        controller: function($scope, HomeRestApi) {
            $scope.searchArticles = function(){
                $scope.originalArticles = $scope.articles;
                if ($scope.form.searchForm.$valid) {
                    HomeRestApi.searchArticles($scope.data.searchString).success(function(data){
                        $scope.articles = data.articles;
                        $scope.splitArticles();
                    })
                }
            }
            $scope.cleanSearch = function(){
                $scope.articles = $scope.originalArticles;
                $scope.splitArticles();
            }
        }
    }
})