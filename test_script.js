var txtFile = new XMLHttpRequest();
txtFile.open("GET", "https://abrahamryzhik.github.io/TrustedGray/prices.txt", true);
txtFile.onreadystatechange = function() {
  if (txtFile.readyState === 4 && txtFile.status == 200) {
     allText = txtFile.responseText;
  }
};
txtFile.send();
console.log(allText);