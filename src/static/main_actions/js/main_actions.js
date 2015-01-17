
var mod = angular.module('MainActions', ['mgcrea.ngStrap', 'HomeRestApi']);

mod.directive('addLink', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/add_link.html",
        controller: function($scope, $alert, HomeRestApi) {
            $scope.data = {};
            $scope.form = {};
            $scope.successAlertOptions = {
                animation: "am-fade-and-slide-top",
                content: 'Seu item foi salvo com sucesso!',
                placement: 'top',
                type: 'success',
                show: true,
                keyboard: true,
                duration: 3
            }

            $scope.errorAlertOptions = {
                animation: "am-fade-and-slide-top",
                content: 'Ocorreu um erro e nossa equipe foi avisada. Por favor, tente novamente.',
                placement: 'top',
                type: 'error',
                show: true,
                keyboard: true,
                duration: 4
            }

            $scope.saveLink = function(callback){
                if ($scope.form.addlinkform.$valid) {
                    var url = $scope.data.url;
                    HomeRestApi.saveLink(url, $scope.data.tags).
                    success(function(){
                        $alert($scope.successAlertOptions);
                        callback();
                        $scope.form.addlinkform.submitted = true;
                        $scope.data = {};
                        $scope.addArticleToGrid(url);
                    }).error(function(){
                        $alert($scope.errorAlertOptions);
                    })
                }                
            }
        }
    }
})
