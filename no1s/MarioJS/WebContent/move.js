/**
 * 移動機能ためのコード
*/
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var x = canvas.width/2;
var middleY = canvas.height-55;
var dx = 2;
var dy = -2;
var paddleHeight = 10;
var paddleWidth = 50;
var paddleX = (canvas.width-paddleWidth)/2;
var rightPressed = false;
var leftPressed = false;
var imageFolder = "images/";
var imgClo = new Image();
var curImage = null;

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
}

function drawPaddle() {
	if(curImage == null){
		curImage = "mario_left_0.png";
		imgClo.src = imageFolder + "mario_left_0.png";	
	}
	imgClo.addEventListener("load", function(){
		ctx.drawImage(imgClo, paddleX, middleY, 50, 50);
	}, false);
		
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPaddle();    
    if(rightPressed && paddleX < canvas.width-paddleWidth) {
        paddleX += 7;
        if(curImage != null){
        	var array = curImage.split("_");
        	console.log(array)
        	if(array[1] == "left"){
        		curImage = "mario_right_0.png";
        		imgClo.src = imageFolder + curImage;
            }else if(array[1] == "right"){
            	if(array[2] == "0.png"){
            		curImage = "mario_right_1.png";
            		imgClo.src = imageFolder + curImage;
                }else if(array[2] == "1.png"){
                	curImage = "mario_right_2.png";
                	imgClo.src = imageFolder + curImage;
                }else if(array[2] == "2.png"){
                	curImage = "mario_right_0.png";
                	imgClo.src = imageFolder + curImage;
                }
            }      
        }else{
        	curImage = "mario_right_0.png";
        }
    }
    else if(leftPressed && paddleX > 0) {
        paddleX -= 7;
        if(curImage != null){
        	var array = curImage.split("_");
        	if(array[1] == "left"){
            	if(array[2] == "0.png"){
            		curImage = "mario_left_1.png";
            		imgClo.src = imageFolder + curImage;
                }else if(array[2] == "1.png"){
                	curImage = "mario_left_2.png";
                	imgClo.src = imageFolder + curImage;
                }else if(array[2] == "2.png"){
                	curImage = "mario_left_0.png";
                	imgClo.src = imageFolder + curImage;
                }
            }else if(array[1] == "right"){
            	curImage = "mario_left_0.png";
            	imgClo.src = imageFolder + curImage;
            } 
        }else{
        	curImage = "mario_left_0.png";
        	imgClo.src = imageFolder + curImage;
        }
    }
    ctx.drawImage(imgClo, paddleX, middleY, 50, 50);
}

setInterval(draw, 10);
