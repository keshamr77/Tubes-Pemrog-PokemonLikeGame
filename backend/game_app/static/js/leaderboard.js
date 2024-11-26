document.addEventListener('DOMContentLoaded', function () {
    fetch('/leaderboard/')
        .then(response => response.json())
        .then(data => {
            const leaderboardBody = document.getElementById('leaderboard-body');
            leaderboardBody.innerHTML = '';

            data.forEach(player => {
                const row = document.createElement('tr');
                const usernameCell = document.createElement('td');
                const scoreCell = document.createElement('td');

                usernameCell.textContent = player.username;
                scoreCell.textContent = player.score;

                row.appendChild(usernameCell);
                row.appendChild(scoreCell);
                leaderboardBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error:', error));
});
