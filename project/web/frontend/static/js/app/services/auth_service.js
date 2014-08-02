angular.module('app.services')
    .service('AuthService', ['$http', function AuthService($http){
        var token = '';

        this.login = function(login){
            return $http.post('/api/auth', login).then(function(result){
                    token = result.data.token;
                    $http.defaults.headers.common.Authorization = 'Bearer ' + token;
            });
        };

        this.clearToken = function(){
            token = '';
            $http.defaults.headers.common.Authorization = null;
        };

        this.getToken = function(){
            return token;
        };
    }]);
