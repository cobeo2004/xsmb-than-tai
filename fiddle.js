//paste this inside the google inspector console to get the value and the name
let elm = document.getElementById("province");
let options = elm.options;
var text = "Options: ";
for (let i = 0; i < elm.length; i++) {
  console.log(`${options[i].value}: ${elm.options[i].text}`);
}
