// This is an adaptation of http://jonraasch.com/blog/a-simple-jquery-slideshow
function slideSwitch() {
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
    setInterval( "slideSwitch()", 5000 );
});
