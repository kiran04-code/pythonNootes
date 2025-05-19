// colorCode = document.getElementById("color-code");
// OptionContainer = document.getElementById("option_container");
// randomColor = null;
// function generateRandomNum(min, max) {
//   return min + Math.floor(Math.random() * (max - min + 1));
// }
// function generateRandomColor(){
//   let red = generateRandomNum(0, 255);
//   let green = generateRandomNum(0, 255);
//   let blue = generateRandomNum(0, 255);
//   return `rgb(${red}, ${green}, ${blue})`;
// }
// function startgame() {
//   randomColor = generateRandomColor();
//   colorCode.innerText = randomColor;
//   const ansIndex = generateRandomNum(0, 5);
//   for (let i = 0; i < 6; i++) {
//     const div = document.createElement("div");
//     div.addEventListener("click", validateResult);
//     div.style.backgroundColor =
//       i === ansIndex ? randomColor : generateRandomColor();
//     OptionContainer.append(div);
//   }
// }
// function validateResult(el) {
//   const selectedColor = el.target.style.backgroundColor;
//   console.log(selectedColor);
//   console.log(randomColor);
//   console.log(selectedColor === randomColor);
// }
// window.addEventListener("load", startgame);

function productExeptSelf(num){
  let n = num.length
  let result = Array(n)

  let left = 1
  for(let i = 0;i<n;i++){
   result[i] = left;
   left*=num[i]
  }

  let right = 1;
  for(let i = n-1;i>=0;i--){
    result[i] *=right;
    right*=num[i]
  }

  return result
}

let  num = [1,2,3,4]
console.log(productExeptSelf(num))