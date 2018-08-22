
$(function() {
        $('.like').click(function () {
            console.log('文章ID' + $(this).attr('artid'));
            var spanlike = $(this);
            var artid = $(this).attr('artid');
            $.getJSON(
                '/app/sanwen/',
                {'artid': artid},
                function (data) {
                    console.log(data);
                    if (data['status'] == 200) {
                        like_num = data['like_num'];
                        spanlike.attr('class', 'cs');
                        spanlike.next().html(like_num);
                    }
                    ;

                });


        });
    });