/////////////////////////////
// JavaScript for Posts page
/////////////////////////////
let likeCount = document.getElementById('likeCount');

let count = 0;

$(function() {
    //Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        //$(this) : Self element, namely div.js-menu-icon
        //next() : Next to div.js-menu-icon, namely div.menu
        //toggle() : Switch show and hide
        $(this).next().toggle();
    })
})


// $(function() {
//     $('.js-heart-icon').click(function() {
//         $(this).toggleClass('is-liked')
        
        

//         if ($(this).hasClass('is-liked')) {
//             count++;
            
//             document.getElementById("like").src = "static/img/love.png";
//           } else {
//             count--;
//             document.getElementById("like").src = "static/img/heart.png";
//           }
        
//         likeCount.innerText = count;
//         if (count == 0) likeCount.innerText=" "; 
//     })
// })

