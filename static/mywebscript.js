function RunSentimentAnalysis() {
    // Get the text to analyze from the input field
    const textToAnalyze = document.getElementById('textToAnalyze').value;

    // Make a POST request to your server endpoint
    fetch('/emotionDetector?textToAnalyze=' + textToAnalyze, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        // Check for errors or valid response
        if (data.error) {
            document.getElementById('system_response').innerHTML = '<p>Error: ' + data.error + '</p>';
        } else if (data.response) {
            document.getElementById('system_response').innerHTML = '<p>' + data.response + '</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('system_response').innerHTML = '<p>Server error. Please try again later.</p>';
    });
}
