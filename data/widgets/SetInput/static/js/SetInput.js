var set = angular.module('set', []);

// Sets the AngularJS interpolators as <[ and ]>, to not conflict with Django.
set.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('<[');
  $interpolateProvider.endSymbol(']>');
});

function SetInput($scope) {
  $scope.answer = [];

  $scope.addElement = function(newElement) {
    if (newElement !== 0 && !newElement) {
      return;
    }
    $scope.answer.push(newElement);
    $scope.newElement = '';
  };

  $scope.deleteElement = function(index) {
    $scope.answer.splice(index, 1);
  };

  $scope.submitAnswer = function(answer) {
    // Send a JSON version of $scope.answer to the backend.
    window.parent.postMessage(
      {'submit': JSON.stringify(answer)}, window.location.origin
    );
  };
}
