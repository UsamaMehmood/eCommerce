var login = function () {
    var element = $('.login-panel');
    element.css('top', '20%');
};
var hide = function () {
    var element = $('.login-panel');
    element.css('top', '-100%');
};

var showTooltip = function () {
    var elem = $('.navigation-tooltip');
    if (elem.css('opacity') == "0") {
        elem.css('opacity', '1');
    } else {
        elem.css('opacity', '0');
    }
};