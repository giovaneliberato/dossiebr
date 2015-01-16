
var app = angular.app;

app.directive('addLink', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: "/static/main_actions/html/add_link.html",
        controller: function($scope) {
            $scope.data = {};

            $scope.saveLink = function(callback){
                if ($scope.data.addlinkform.$valid) {
                    callback();
                } else {
                  $scope.data.addlinkform.submitted = true;
                }                
            }
        }
    }
})
