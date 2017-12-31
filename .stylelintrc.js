module.exports = {
  extends: "stylelint-config-standard",
  plugins: [
    "stylelint-selector-bem-pattern"
  ],
  rules: {
    "selector-list-comma-newline-after": "always-multi-line",
    "plugin/selector-bem-pattern": {
      preset: "bem",
      componentSelectors: function(componentName) {
        var WORD = '[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*';
        var element = '(?:__' + WORD + ')?';
        var modifier = '(?:--' + WORD + '){0,2}';
        var attribute = '(?:\\[.+\\])?';
        return new RegExp('^\\.' + componentName + element + modifier + attribute + '$');
      }
    }
  }
}
