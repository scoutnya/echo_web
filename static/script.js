//console.log("JS loaded")
function getRandomPost() {

    fetch("/random")
        .then(response => response.json())
        .then(data => {

            document.getElementById("randomPost").innerText = data.content

        })

}// JavaScript source code
