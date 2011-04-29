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
});

