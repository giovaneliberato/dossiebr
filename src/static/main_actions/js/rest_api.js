var app = angular.module('HomeRestApi', []);

app.factory('HomeRestApi', function($http){
    function saveLink(url, tags){
       return $http.post('/articles/article/save', {url:url, tags:tags})
    }

    function getPreviewData(url) {
        var embedly_url = 'http://api.embed.ly/1/oembed?url=';
        return $http.get(embedly_url + encodeURIComponent(url));
    }

    function getUserArticles() {
        return $http.post("/articles/article/list", {});
    }

    return {
        saveLink: saveLink,
        getPreviewData: getPreviewData,
        getUserArticles: getUserArticles,
    };
});