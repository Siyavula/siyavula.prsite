// This is an adaptation of http://jonraasch.com/blog/a-simple-jquery-slideshow
function slideSwitch() {
    if ($('.banner').length <= 1 ) {
        clearInterval(ss_interval);
        return;
    }
    var $active = $('.banner.banner-active');

    if ( $active.length == 0 ) $active = $('.banner:last');

    // use this to pull the images in the order they appear in the markup
    var $next =  $active.next().length ? $active.next() : $('.banner:first');
    $next.css({opacity: 0.0})
        .addClass('banner-active')
        .animate({opacity: 1.0}, 1500, function() {
            $active.removeClass('last-active');
        });
    $active.addClass('last-active')
        .removeClass('banner-active');
}

// end jonraasch

function isImageOk(img) {
    // During the onload event, IE correctly identifies any images
    // that weren't downloaded as not complete. Others should too.
    // Gecko-based browsers act like NS4 in that they report this
    // incorrectly: they always return true.
    if (!img.complete) {
        return false;
    }

    // However, they do have two very useful properties: naturalWidth
    // and naturalHeight. These give the true size of the image. If
    // it failed to load, either of these should be zero.
    if (typeof img.naturalWidth != "undefined" && img.naturalWidth == 0) {
        return false;
    }

    // No other way of checking: assume it's ok.
    return true;
}

function checkPreload() {
    var loadeds = 0;
    $('.banner img').each(function(index) {
        if (isImageOk(this)) {
            loadeds += 1;
        }
    });
    if ( $('.banner').length == loadeds ) {
        clearInterval(preload_interval_id);
        $('.banner').each(function(index) {
            $(this).removeClass('hidden');
        });
        ss_interval = setInterval(slideSwitch, 5000 );
    }
}

$(document).ready(function()
{
    // Remove the default text if clicking on the textbox.
    $("#textbox").focus(function() {
        if ($(this).val() == $(this)[0].title)
        {
            $(this).removeClass("defaultTextActive");
            $(this).val("");
        }
    });
    
    // Add the default text if the textbox is empty.
    $("#textbox").blur(function() {
        if ($(this).val() == "")
        {
            $(this).addClass("defaultTextActive");
            $(this).val($(this)[0].title);
        }
    });
    
    // Send the user to the shortcode page on fhsst.
    $("#shortcodebutton").click(function(e) {
        e.preventDefault();
        e.stopPropagation();
        window.open('http://www.fhsst.org/'+$("#textbox").val(), '_blank');
        $("#textbox").val("");
        $("#textbox").blur();
    });

    // Initial blur
    $("#textbox").blur();

    // Banner rotator
    // Get the set of images and preload.
    preload_interval_id = setInterval(checkPreload, 1000);

    // Email the user input to the portal address.
    $("#emailbutton").click(function(e) {
        e.preventDefault();
        e.stopPropagation();
        action = $('form#mailform').attr('action');
        $.get(action+'?email='+$("#textbox").val(), function(data) {
            alert(data);
        });
        $("#textbox").val("");
        $("#textbox").blur();
    });

});
