<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta charset="UTF-8">
<style>
html, body { width:100%;height:100%;margin:0;padding:0 }
body { background:black no-repeat left bottom; }
div { margin:0;padding:0 }
canvas {
    border:1px solid #d3d3d3;
    position:absolute;
    width:100%;
    height:100%;
    xbackground-color: #f1f1f1;
}
button { margin:2px;padding:2px;border:2px solid blue}
output { margin:2px;padding:2px;border:1px dashehd brown}
</style>

<script>
var HMAX = 1000        // maximum magasság érték pl 0..1000, ezt képezzük le a képernyőre
var WMAX = 1000
var time = { tick:0, frame:0,
             tickMs:50, tickPerFrame:1, msPerTick:1000,
             loop:0
           }
var planet = { name:"Föld", image:"Luna.jpg",
               height:600, width:800, 
               g:3.711,     // gravitációs állandó (m/s²).
                            // Föld: 9.807, Hold: 1.622, Mars: 3.711 m/s², A Jupiteren: 24.79 m/s²
                            // Tapasztalati érték, játssz vele!
               ground_y:50
             } 
var lander = { x:50,
               y:50,            // függőleges helyzet (m)
               vx:0,            // oldal, sofródás sebesség (m/s)
               vy:0,            // zuhanó sebesség (m/s)
               ay:0,            // zuhanás-gyorsulás (m/s²)
               str:8,           // leszálló rakéta tolóereje (m/s²)
               height:11,
               engineOn:false
             }
function start() {
    document.body.style.backgroundImage = `url('${planet.image}')`
    lander.x = 10 + Math.floor(Math.random()*100)
    lander.y = 900 + Math.floor(Math.random()*100)
    lander.vx = 1 // Math.floor(Math.random()*10)
    lander.ay = 0
    lander.vy = 0
    lander.height = document.getElementById("urhajo").offsetHeight
    if (time.loop == 0) {
        document.addEventListener("keydown",handleKeyDown, false);	
        document.addEventListener("keyup",handleKeyUp, false);	
        time.loop = setInterval(gameLoop,time.tickMs)
    } else {
        //clearInterval(time.loop)
        console.log("restart")
        time.loop = setInterval(gameLoop,time.tickMs)
    }
    
    let canv = document.getElementById("mycanvas");
    canv.height = canv.offsetHeight;
    canv.width = canv.offsetWidth;
}
function gameLoop() {
    time.tick += 1
    lander.ay = -planet.g
    lander.vy += lander.ay * (time.msPerTick/1000)
    let x0=lander.x
    let y0=lander.y
    lander.y += lander.vy * (time.msPerTick/1000)
    lander.x += lander.vx * (time.msPerTick/1000)
    log(`tick:${time.tick}: ay:${lander.ay}, vy:${lander.vy.toFixed(2)}, y:${lander.y.toFixed(2)}, lander:${lander.engineOn}`)
    if (lander.engineUp) {
        lander.y += 1
    }
    vonal(x0, y0, lander.x, lander.y)
    mozog(lander.x, lander.y)
    if (lander.y <= planet.ground_y) {
        endGame()
    }
}

function endGame() {
    clearInterval(time.loop)
}
function handleKeyDown(event) {
    log(`keY: ${event.key}-${event.keyCode}-${event.which}`)
	if (event.key == "W" || event.key=="w" || event.key==" ")
	{		
        lander.engineUp=true;
	}
}
function handleKeyUp(event) {
    lander.engineUp=false;
}

function mozog(x_pc, y_pc) {
    let canv = document.getElementById("mycanvas");
    let elem = document.getElementById("urhajo");
    let H = canv.offsetHeight - elem.offsetHeight;
    let W = canv.offsetWidth - elem.offsetWidth;
    let x2 = x_pc / WMAX
    let y2 = y_pc / HMAX
    elem.style.top = (H - Math.floor(H * y2)) + "px";
    elem.style.left = Math.floor(W * x2)+ "px";
    console.log(`. y_pc:${y_pc} H:${H} y2:${y2} oh:${canv.offsetHeight} - H*y2=${H * y2} -> top:${elem.style.top}`)
}
function getcoord(x_pc, y_pc) {
    let canv = document.getElementById("mycanvas");
    let elem = document.getElementById("urhajo");
    let H = canv.offsetHeight - elem.offsetHeight;
    let W = canv.offsetWidth - elem.offsetWidth;
    let y2 = y_pc / HMAX
    let x2 = x_pc / WMAX
    return {x_px: (Math.floor(W * x2)), y_px:(H - Math.floor(H * y2))}
}
function vonal(x1,y1,x2,y2) {
    let elem = document.getElementById("urhajo");
    let ctx = document.getElementById("mycanvas").getContext("2d");
    ctx.strokeStyle = "green";
    ctx.beginPath();
    ctx.lineWidth = 3
    let c1 = getcoord(x1,y1)
    let c2 = getcoord(x2,y2)
    ctx.moveTo(c1.x_px + elem.offsetWidth/2, c1.y_px);
    ctx.lineTo(c2.x_px + elem.offsetWidth/2, c2.y_px);
    console.log(`. x1:${c1.x_px + elem.offsetWidth/2} y1:${c1.y_px} x2:${c2.x_px + elem.offsetWidth/2} y2:${c2.y_px}`)
    ctx.stroke(); 
}
function log(text) {
    console.log(text)
    document.getElementById("status").innerHTML = text
}
</script>

</head>
<body>
    <div style="position:relative;height:6vh">
        <button onclick="start()">START</button><output id="status">blabla</output>
    </div>
<div style="position:relative;height:90vh">
        <canvas id="mycanvas" style="z-index:1;"></canvas>
        <img id="urhajo" src="raketa-B1.png" style="position:absolute;z-index:2;max-height:10vh">
    </div>
</body>
<html>
