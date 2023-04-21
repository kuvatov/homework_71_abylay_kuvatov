$(document).ready(function() {
    $('.card_body_form').on('submit', function(event) {
        event.preventDefault();
        let $form = $(this);
        $.ajax({
            url: $form.attr('action'),
            method: $form.attr('method'),
            data: $form.serialize(),
            success: function(data) {
                let $btn = $form.find('button');
                let $img = $btn.find('img');
                if ($img.attr('alt') == 'like') {
                    $img.attr('src', '../../static/media/unlike.jpg');
                    $img.attr('alt', 'unlike');
                } else {
                    $img.attr('src', '../../static/media/like.jpg');
                    $img.attr('alt', 'like');
                }
                let $likesCount = $('#likes_count');
                console.log($likesCount)
                $likesCount.text(data.likes_count);
            }
        });
    });
});
