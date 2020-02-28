var prevScrollpos = window.pageYOffset;
$(document).ready(function() {
    // to open the home menu
    $("#goofy").click();
    // for ajax request in tetrino
    $('#form_grid_tetrino').submit(function(event) {

        var data = {};
        var Form = this;

        $.each(this.elements, function(i, v) {
            var input = $(v);
            data[input.attr("name")] = input.val();
            delete data["undefined"];
        });
        $.ajax({
            type: 'POST',
            url: '/fillit_ajax',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data),
            context: Form,
            success: function(cb_data) {
                var res = $('#end_form_tetrino').get(0);
                if (cb_data.canvas == false) {
                    res.innerHTML = '<div>' + cb_data.html + '</div>';
                }
                else
                {
                    res.innerHTML = cb_data.html;
                    if (cb_data.for3d == true) {
                        example_drawing3d(cb_data.sizex, cb_data.sizey, cb_data.data);
                    }
                    else {
                        example_drawing(cb_data.sizex, cb_data.sizey, cb_data.data);
                    }
                }
            },
            error: function() {
                $(this).html("Error! something went wrong! Sorry, Refresh page and try again!");
            }
        });
        event.preventDefault();
    });

    window.onscroll = function() {
        var currentScrollPos = window.pageYOffset;

        if (prevScrollpos > currentScrollPos) {
            document.getElementById("navbar").style.top = "0";
        } else {
            document.getElementById("navbar").style.top = "-90px";
        }
        prevScrollpos = currentScrollPos;
    }

});