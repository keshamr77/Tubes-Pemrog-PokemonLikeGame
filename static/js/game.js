// Canvas setup
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const canvasWidth = 800;
const canvasHeight = 600;
canvas.width = canvasWidth;
canvas.height = canvasHeight;

// Images and assets
const background = new Image();
background.src = "/static/assets/images/background.gif";

const player = {
    x: 100,
    y: canvasHeight / 2,
    width: 50,
    height: 50,
    speed: 5,
    sprite: new Image(),
    projectiles: []
};
player.sprite.src = "/static/assets/images/player.gif";

let keys = {};
document.addEventListener('keydown', (e) => keys[e.code] = true);
document.addEventListener('keyup', (e) => keys[e.code] = false);

// Game variables
let obstacles = [];
let enemies = [];
let powerups = [];
let frameCount = 0;
let lifeCount = 3;
let score = 0;

// Power-up states
let isSpeedActive = false;
let isDoubleActive = false;
const powerUpDuration = 300;

// Input handling
function updatePlayer() {
    let currentSpeed = isSpeedActive ? player.speed * 2 : player.speed;
    if (keys['ArrowUp'] && player.y > 0) player.y -= currentSpeed;
    if (keys['ArrowDown'] && player.y + player.height < canvasHeight) player.y += currentSpeed;
}

// Projectile shooting
function shootProjectile() {
    let projectileCount = isDoubleActive ? 2 : 1;
    for (let i = 0; i < projectileCount; i++) {
        player.projectiles.push({
            x: player.x + player.width,
            y: player.y + (i * 10), // Offset for double projectile
            width: 10,
            height: 5,
            speed: 10
        });
    }
}

// Generate game elements
function generateObstacles() {
    if (frameCount % 120 === 0) {
        obstacles.push({
            x: canvasWidth,
            y: Math.random() * canvasHeight,
            width: Math.random() * 50 + 20,
            height: Math.random() * 50 + 20,
            speed: Math.random() * 2 + 3,
            sprite: new Image()
        });
        obstacles[obstacles.length - 1].sprite.src = "/static/assets/images/obstacle.gif";
    }
}

function generateEnemies() {
    if (frameCount % 180 === 0) {
        enemies.push({
            x: canvasWidth,
            y: Math.random() * canvasHeight,
            width: 50,
            height: 50,
            speed: 3,
            sprite: new Image()
        });
        enemies[enemies.length - 1].sprite.src = "/static/assets/images/enemy.gif";
    }
}

function generatePowerUps() {
    if (frameCount % 300 === 0) {
        powerups.push({
            x: canvasWidth,
            y: Math.random() * canvasHeight,
            width: 30,
            height: 30,
            type: Math.random() > 0.5 ? "speed" : "double",
            sprite: new Image()
        });
        powerups[powerups.length - 1].sprite.src =
            powerups[powerups.length - 1].type === "speed"
                ? "/static/assets/images/powerup_speed.png"
                : "/static/assets/images/powerup_double.png";
    }
}

// Collision detection
function detectCollision(obj1, obj2) {
    return obj1.x < obj2.x + obj2.width &&
           obj1.x + obj1.width > obj2.x &&
           obj1.y < obj2.y + obj2.height &&
           obj1.y + obj1.height > obj2.y;
}

// Apply power-ups
function applyPowerUp(type) {
    if (type === "speed") {
        isSpeedActive = true;
        setTimeout(() => isSpeedActive = false, powerUpDuration * 16.67);
    }
    if (type === "double") {
        isDoubleActive = true;
        setTimeout(() => isDoubleActive = false, powerUpDuration * 16.67);
    }
}

// Collision feedback
function handleCollisionFeedback() {
    const explosion = new Image();
    explosion.src = "/static/assets/images/explosion.png";
    ctx.drawImage(explosion, player.x, player.y, 50, 50);

    const hitSound = new Audio("/static/assets/sounds/hit.wav");
    hitSound.play();
}

// Game over check
function checkGameOver() {
    if (lifeCount <= 0) {
        const gameOverSound = new Audio("/static/assets/sounds/game_over.wav");
        gameOverSound.play();
        alert("Game Over! Reload to restart.");
        sendScore("Player", score);
    }
}

// Update score
function updateScore() {
    score += 10;
    ctx.fillStyle = "white";
    ctx.font = "20px Arial";
    ctx.fillText("Score: " + score, 10, 20);
}

// Send score to backend
function sendScore(username, score) {
    fetch('/submit_score', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, score })
    }).then(response => {
        if (response.ok) console.log("Score submitted!");
        else console.log("Failed to submit score.");
    });
}

// Main game loop
function gameLoop() {
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    
    // Draw background
    ctx.drawImage(background, 0, 0, canvasWidth, canvasHeight);

    // Update player
    updatePlayer();
    ctx.drawImage(player.sprite, player.x, player.y, player.width, player.height);

    // Generate and update obstacles
    generateObstacles();
    obstacles.forEach((obs, index) => {
        obs.x -= obs.speed;
        ctx.drawImage(obs.sprite, obs.x, obs.y, obs.width, obs.height);
        if (obs.x + obs.width < 0) obstacles.splice(index, 1);
        if (detectCollision(player, obs)) {
            lifeCount--;
            handleCollisionFeedback();
            obstacles.splice(index, 1);
        }
    });

    // Generate and update enemies
    generateEnemies();
    enemies.forEach((enemy, index) => {
        enemy.x -= enemy.speed;
        ctx.drawImage(enemy.sprite, enemy.x, enemy.y, enemy.width, enemy.height);
        if (enemy.x + enemy.width < 0) enemies.splice(index, 1);
        if (detectCollision(player, enemy)) {
            lifeCount--;
            handleCollisionFeedback();
            enemies.splice(index, 1);
        }
    });

    // Generate and update power-ups
    generatePowerUps();
    powerups.forEach((power, index) => {
        power.x -= 4;
        ctx.drawImage(power.sprite, power.x, power.y, power.width, power.height);
        if (detectCollision(player, power)) {
            applyPowerUp(power.type);
            powerups.splice(index, 1);
        }
    });

    // Update score and check game over
    updateScore();
    checkGameOver();

    frameCount++;
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
