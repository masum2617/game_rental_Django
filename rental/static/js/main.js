// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);


const counters = document.querySelectorAll('.counter');
const speed = 200;

counters.forEach(counter => {
  const updateCount = ()=>{
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;

    const inc = target / speed;

    if (count < target){
      counter.innerText = Math.ceil(count + inc);
      setTimeout(updateCount , 1);
    } else {
      count.innerText = target;
    }

    // console.log(inc);
    // console.log(typeof target);
  }

  updateCount();
});