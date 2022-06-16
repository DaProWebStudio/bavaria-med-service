$('#get_services').click(function (e) {
    e.preventDefault();
    serviceContent = $('.services__content')
    letter = e.originalEvent.target.value;
    console.log()
    url = '/service/api/letter/' + letter + '/'
    $.ajax({
        url: url, type: 'GET', data: {}, cache: true,
        success: function (data) {
            serviceContent.html('')
            $.each(data.services, function(k, v){
                urlData = '/service/detail/' + v.slug + '/'
                serviceContent.append('<a href="'+ urlData +'" class="service__item">' + v.title + '</a>');
            });
        }
    })
});
var myFunction = function() {
    $('.myBtn').removeClass('active')
    $(this).addClass('active')
}
$('.myBtn').on('click', myFunction);