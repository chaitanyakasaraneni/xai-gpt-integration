function generateEmoji() {
    var text = document.getElementById("text").value;

    // Send the text to the Flask API using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/emoji", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var emoji = response.emoji;
            var output_text = response.text;

            // Update the result div with the generated emoji and text
            var resultDiv = document.getElementById("result");
            resultDiv.innerHTML = "<p>" + emoji + "</p><p>" + output_text + "</p>";
        }
    };
    xhr.send("text=" + text);
}
