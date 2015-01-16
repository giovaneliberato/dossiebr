
var app = angular.app;

app.directive('addLink', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/add_link.html",
        controller: function($scope, $alert, $http) {
            $scope.data = {};
            $scope.form = {};
            $scope.successAlertOptions = {
                animation: "am-fade-and-slide-top",
                container: ".container",
                content: 'Seu item foi salvo com sucesso!',
                placement: 'top',
                type: 'success',
                show: true,
                keyboard: true,
                duration: 3
            }

            $scope.saveLink = function(callback){
                if ($scope.form.addlinkform.$valid) {
                    $http.post('/actions/link/save', {link:$scope.data.link,
                                                  tags:$scope.data.tags}).
                    success(function(){
                        $alert($scope.successAlertOptions);
                        callback();
                        $scope.form.addlinkform.submitted = true;
                        $scope.data = {}
                    })
                }                
            }
        }
    }
})
