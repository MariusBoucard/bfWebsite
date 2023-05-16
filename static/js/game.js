var launchState = {
    preload: function() {
        this.load.image('background', 'assets/launch_screen.png');
        this.load.image('startButton', 'assets/start_button.png');
    },
    create: function() {
        this.add.image(849, 600, 'background');
        var startButton = this.add.image(400, 500, 'startButton');
        startButton.setInteractive();
        startButton.on('pointerdown', function() {
            this.scene.start('gameState');
        }, this);
    }
};



var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: "game-container",
    physics: {
        default: "arcade",
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);
var player;
var coins;
var score = 0;
var scoreText;
var audioContext;
var soundButton;
var lives = 3;
var livesText;
var that;
var soundOn = false;
var gameOverYouKnow = false;
var gameover_image;
var endText;
var sprite;

function preload ()
{
    this.load.image('logo', './static/assets/Logo.png');
    this.load.image('coin', './static/assets/coin.png');
    this.load.audio('backgroundMusic', './static/assets/becane.mp3');
    this.load.audio('coinSound', './static/assets/caca.wav');
    this.load.image('background', './static/assets/background.png');
    this.load.image('soundOn', './static/assets/soundOn.png');
    this.load.image('soundOff', './static/assets/soundOff.png');
    this.load.image('gameover','./static/assets/gameover.jpg')
    this.load.image('restartButton','./static/assets/coin.png')
}

function create ()
{
    that = this;
    this.add.image(400, 300, 'background');
    player = this.physics.add.sprite(400, 500, 'logo');
    player.setCollideWorldBounds(true);
    this.input.keyboard.on('keydown_LEFT', function (event) {
        player.setVelocityX(-500);
    });
    this.input.keyboard.on('keydown_RIGHT', function (event) {
        player.setVelocityX(500);
    });
    this.input.keyboard.on('keydown_UP', function (event) {
        player.setVelocityY(-200);
    });
    this.input.keyboard.on('keydown_DOWN', function (event) {
        player.setVelocityY(200);
    });
    this.input.keyboard.on('keyup', function (event) {
        player.setVelocity(0);
    });

    coins = this.physics.add.group();

    coins.children.iterate(function (child) {
        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
        child.hitBottom = false;
    });

    this.input.keyboard.on('keydown_P', function (event) {
        console.log("pet")
        if(gameOverYouKnow){

            lives =3;
            score =0;
            gameOverYouKnow=false;
            gameover_image.destroy();
            sprite.destroy();
            endText.destroy();
            livesText = this.add.text(16, 150, 'Vies : ' + lives, { fontSize: '32px', fontWeight:"100px",fill: 'white' });
        }
    });

    this.physics.add.collider(player, coins, collectCoin, null, this);

    scoreText = this.add.text(16, 16, 'Grosse\nchiasse\n   0', { fontSize: '32px', fill: 'white' });

    backgroundMusic = this.sound.add('backgroundMusic');
    coinSound = this.sound.add('coinSound');


    this.time.addEvent({
        delay: 1000,                // ms
        callback: generateCoin,
        callbackScope: this,
        loop: true
    });
    soundButton = this.add.image(700, 50, 'soundOff').setInteractive();
    soundButton.on('pointerup', toggleSound);

   
    livesText = this.add.text(16, 150, 'Vies : ' + lives, { fontSize: '32px', fill: 'white' });


 
}

function gameOver() {
    gameOverYouKnow = true;
    // player.setTint(0xff0000); // tint the player red
    gameover_image = that.add.image(400, 300, 'gameover'); // add gameover image
    endText = that.add.text(100, 20, 'Nouveau son \n le 7 Juin !', { fontSize: '62px', fill: '#000' });

    endText = that.add.text(350, 300, 'Score: ' + score, { fontSize: '32px', fill: '#fff' });
    sprite = that.add.sprite(400, 400, 'restartButton');
 
    // code to end the game and display the score
}
function restart(){
    console.log("restart");
}

function update(){
    if(!gameOverYouKnow){
        coins.children.iterate(function (child) {
        if (child.y > 600) {
            child.disableBody(true, true);
            removeLife(child);
            child.hitBottom = true;
        }
    });
}
    }
    


function toggleSound(){
    if(soundOn){
        soundOn = false;
        soundButton.setTexture('soundOff');
        backgroundMusic.stop();
    }else{
        soundOn = true;
        soundButton.setTexture('soundOn');
        backgroundMusic.play();
    }
}
function collectCoin (player, coin)
{
    coin.disableBody(true, true);
    if(soundOn){
        coinSound.play();
    }
    score += 1;
    scoreText.setText('Chiasses\nrécoltées \n    ' + score);
}

function removeLife(coin) {
    if(!coin.hitBottom){

        lives--;
        livesText.setText('Vies : ' + lives);
    }

    if (lives === 0) {
        gameOver();
    }
}





function generateCoin() {
    if(!gameOverYouKnow){

        var x = Phaser.Math.Between(0, config.width);
        var y = Phaser.Math.Between(0, -100);
        var coin = coins.create(x, y, 'coin');
        coin.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
    }
}