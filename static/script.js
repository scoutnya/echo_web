//console.log("JS loaded")
function getRandomPost() {

    fetch("/random")
        .then(response => response.json())
        .then(data => {

            document.getElementById("randomPost").innerText = data.content

        })

}
function checkPost() {

    let text = document.getElementById("content").value

    if (text.trim() === "") {
        alert("Please enter something")
        return false
    }

    return true
}
