//paste this inside the google inspector console to get the value and the name
let elm = document.getElementById("province");
let options = elm.options;
var text = "Options: ";
for (let i = 0; i < elm.length; i++) {
  console.log(`${options[i].value}: ${elm.options[i].text}`);
}

let casemiro = [];

for (const i of options) {
  casemiro.push(i.value);
}

console.log(casemiro);

const x = (par) => {
  if (par == 10) return par + x(par);
};

console.log(x(10));
