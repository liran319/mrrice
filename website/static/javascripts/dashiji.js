(function() {
    typeout('.typeout', ['美食', '享受', '生活方式'], {
        numLoops: 3,
        interval: 3000,
        max: 110, // upper limit for typing speed
        min: 40,
        callback: function(el) {
            el.innerHTML += "。";
        }
    });
})(jQuery);