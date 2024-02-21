$('.like-form').submit(function(e) {
    e.preventDefault()
  
    const post_id = $(this).attr('id')
  
   const likeText = $(".like-btn"+post_id).find("i").hasClass("fa-heart-o") ? "Unlike":"Like"//check for class and if true then set value as unlike or like..
    const trim = $.trim(likeText)
  
    const url = $(this).attr('action')
  
    let res;
    const likes = $(`.like-count${post_id}`).text()
    const trimCount = parseInt(likes)
  
    /*  $.ajax({
        type: 'POST',
        url: url,
        data: {
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
          'post_id': post_id,
        },
        success: function(response) {*/
    if (trim === 'Unlike') {
    //use .html to add htmls codes
      $(`.like-btn${post_id}`).html('<i class="fa fa-heart" aria-hidden="true"></i>')
      res = trimCount - 1
    } else {
      $(`.like-btn${post_id}`).html('<i class="fa fa-heart-o" aria-hidden="true"></i>')
      res = trimCount + 1
    }
  
    $(`.like-count${post_id}`).text(res)
    /*  },
      error: function(response) {
        console.log('error', response)
      }
    })*/
  
  });