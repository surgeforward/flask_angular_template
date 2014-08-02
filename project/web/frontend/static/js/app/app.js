angular.module('app.services', []);
angular.module('app.controllers', ['app.services']);

angular.module('app', ['ngRoute', 'app.controllers', 'app.services', 'angular-loading-bar'])
    .config(function($routeProvider){
        $routeProvider
            .when('/', {
            allowAnonymous: true,
            templateUrl: 'static/js/app/login/login.html',
            controller: 'LoginCtrl'
            })
            .when('/profile', {
            templateUrl: 'static/js/app/profile/profile.html',
            controller: 'ProfileCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    }).run(function($rootScope, $location, AuthService){
        $rootScope.$on('$routeChangeStart', function (event, next, current) {
            var token = AuthService.getToken();
            if (token === '' && !next.allowAnonymous) {
                $location.path('/');
            }
        });
    });
