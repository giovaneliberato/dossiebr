var app = angular.module('MainActionsApi', []);

app.factory('MainActionsApi', function($http){
    function saveLink(url, tags){
       return $http.post('/actions/link/save', {url:url, tags:tags})
    }

    function getPreviewData(url)

    return {
        saveLink: saveLink
    };
});