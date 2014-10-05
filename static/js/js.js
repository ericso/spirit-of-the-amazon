// For Off-Canvas Menu
/*====================================
=            ON DOM READY            =
====================================*/
$(function() {
  $('.toggle-nav').click(function() {
    // Calling a function in case you want to expand upon this.
    toggleNav();
  });
  // $('.toggle-nav').mouseenter(function() {
  //   toggleNav();
  // });
  // $('.toggle-nav').mouseleave(function() {
  //   toggleNav();
  // });

  // Activate the product carousel
  $('.carousel').carousel();
});


/*========================================
=            CUSTOM FUNCTIONS            =
========================================*/

/* Uncomment the following to use hiding side menubar
function toggleNav() {
  if ($('#site-wrapper').hasClass('show-nav')) {
    // Do things on Nav Close
    $('#site-wrapper').removeClass('show-nav');
  } else {
    // Do things on Nav Open
    $('#site-wrapper').addClass('show-nav');
  }

  //$('#site-wrapper').toggleClass('show-nav');
}
*/
