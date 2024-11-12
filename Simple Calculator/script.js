const n = document.getElementById("input");
function button(input) {
  n.value += input;
}

function inputClear() {
  n.value = "";
}

function calculate() {
  n.value = eval(n.value);
}
