function sendScore(username, score) {
    fetch('/submit_score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, score })
    })
    .then(response => response.ok ? console.log("Score submitted!") : console.log("Failed to submit score."));
}

// Contoh pemanggilan saat game over
sendScore("Player1", 12345);
