$(document).ready(function () {


    $('form').on('submit', function (event) {
        $.ajax({
            data: {
                size: $('#size').val(),
                sector: $('#sector').val(),
                ownership: $('#ownership').val(),
                Revenue: $('#Revenue').val(),
                seniority: $('input[name=seniority]:checked').val(),
                ML: $('input[name=ML]:checked').val(),
                python: $('input[name=python]:checked').val(),
                state: $('#state').val(),
                cloud_computing: $('input[name=cloud_computing]:checked').val(),
                title: $('#title').val(),
                big_data: $('input[name=big_data]:checked').val(),
                deep_learning: $('input[name=deep_learning]:checked').val(),
                graduate: $('input[name=graduate]:checked').val(),
                undergrad: $('input[name=undergrad]:checked').val(),
                demo: $('#myRange').val()
            },
            type: 'POST',
            url: "/process"
        })
            .done(function (data) {
                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#result').hide()
                }

                else {
                    $('#errorAlert').hide()
                    $('#result').text(data.result).show()
                }
            })
        event.preventDefault();
    })
})