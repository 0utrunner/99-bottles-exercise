function bottleSong(num) {
  let bottles = num;
  while(bottles > 1){
    if(bottles == 2){
      console.log(bottles + ' bottles of beer on the wall, ' + bottles + ' bottles of beer. Take one down and pass it around, ' + (bottles - 1) + ' bottle of beer on the wall.')
    } else {
    console.log(bottles + ' bottles of beer on the wall, ' + bottles + ' bottles of beer. Take one down and pass it around, ' + (bottles - 1) + ' bottles of beer on the wall.')
    }
    bottles--
  }
  return '1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, ' + num + ' bottles of beer on the wall.';
 };
 
 console.log(bottleSong(99));