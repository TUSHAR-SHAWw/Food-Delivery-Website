function convertToStars(rating) {
  const roundedRating = Math.round(rating * 2) / 2;
  const wholeStars = Math.floor(roundedRating);
  const halfStar = roundedRating % 1 !== 0;
  const emptyStars = 5 - wholeStars - (halfStar ? 1 : 0);

  let stars = '<i class="fa-solid fa-star"></i>'.repeat(wholeStars);
  if (halfStar) {
    stars += '<i class="fa-solid fa-star-half-stroke"></i>';
  }
  stars += '<i class="fa-regular fa-star"></i>'.repeat(emptyStars);

  return stars;
}

function updateCounter(foodId, quantity,cost,cart_total) {
      console.log(
        "Updating counter for food ID " + foodId + " with quantity " + quantity + "cost" +cost +"cart_total" + cart_total);
      $(".item" + foodId).text(quantity);
      $(".total" + foodId).text('Total : ' +cost * quantity);
      $(".cart_total").text('Cart Total Rs : '+cart_total );

    }