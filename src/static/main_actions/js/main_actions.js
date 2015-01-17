
var mod = angular.module('MainActions', ['mgcrea.ngStrap', 'HomeRestApi']);

mod.directive('addLink', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/add_link.html",
        controller: function($scope, $alert, $http, HomeRestApi) {
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

            $scope.saveLink = function(callback){
                if ($scope.form.addlinkform.$valid) {
                    HomeRestApi.saveLink($scope.data.url, $scope.data.tags).
                    success(function(){
                        $alert($scope.successAlertOptions);
                        callback();
                        $scope.form.addlinkform.submitted = true;
                        $scope.data = {}
                    })
                    HomeRestApi.getPreviewData($scope.data.url).success(function(data){
                        console.log(data);
                    })
                }                
            }
        }
    }
})
