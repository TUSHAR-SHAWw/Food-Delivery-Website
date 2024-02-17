
function increaseValue(name) {
    c=parseInt(document.getElementsByClassName(name)[0].innerHTML);
    console.log(typeof(c));
    c++;
    updateCounter(name,c);
}

function decreaseValue(name) {
    c=parseInt(document.getElementsByClassName(name)[0].innerHTML);
    if (c>0){
        c--;
        updateCounter(name,c);
    }
}

function updateCounter(name,c) {
    document.getElementsByClassName(name)[0].innerHTML=c
}

$(document).ready(function() {
      $(".decrement-btn").click(function() {
        var itemId = $(this).data("item-id");
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({
          type: "POST",
          url: "/decrement_url/",
          data: {
            food_id: itemId,
            csrfmiddlewaretoken: csrfToken
          },
          success: function(response) {
            if (response.success) {
              updateQuantity(itemId, response.quantity);
            }
          }
        });
      });

      $(".increment-btn").click(function() {
        var itemId = $(this).data("item-id");
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({
          type: "POST",
          url: "/increment_url/",
          data: {
            food_id: itemId,
            csrfmiddlewaretoken: csrfToken
          },
          success: function(response) {
            if (response.success) {
              updateQuantity(itemId, response.quantity);
            }
          }
        });
      });

      function updateQuantity(itemId, quantity) {
        $(".item" + itemId).text(quantity);
      }
    });