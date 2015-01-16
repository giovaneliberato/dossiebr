var app = angular.actions_app;

app.factory('MainActionsApi', function(){
    function save_link(link, tags){
       return $.post('/actions/link/save', {link:link, tags:tags})
    }

    return {
        save_link: save_link
    };
});