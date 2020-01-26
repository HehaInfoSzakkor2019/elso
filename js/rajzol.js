var HMAX = 1000        // maximum magasság érték pl 0..1000, ezt képezzük le a képernyőre
var WMAX = 1000
var time = {
    tick: 0, frame: 0,
    tickMs: 50, tickPerFrame: 1, msPerTick: 1000,
    loop: 0
}
Tu
function start() {
    i = 0
    while (i<)

}

function mozog(x_pc, y_pc) {
    let canv = document.getElementById("mycanvas");
    let elem = document.getElementById("urhajo");
    let H = canv.offsetHeight - elem.offsetHeight;
    let W = canv.offsetWidth - elem.offsetWidth;
    let x2 = x_pc / WMAX
    let y2 = y_pc / HMAX
    elem.style.top = (H - Math.floor(H * y2)) + "px";
    elem.style.left = Math.floor(W * x2) + "px";
    console.log(`. y_pc:${y_pc} H:${H} y2:${y2} oh:${canv.offsetHeight} - H*y2=${H * y2} -> top:${elem.style.top}`)
}
function getcoord(x_pc, y_pc) {
    let canv = document.getElementById("mycanvas");
    let H = canv.offsetHeight - elem.offsetHeight;
    let W = canv.offsetWidth - elem.offsetWidth;
    let y2 = y_pc / HMAX
    let x2 = x_pc / WMAX
    return { x_px: (Math.floor(W * x2)), y_px: (H - Math.floor(H * y2)) }
}
function vonal(x1, y1, x2, y2, offsetx = 0, offsety = 0) {
    let elem = document.getElementById("urhajo");
    let ctx = document.getElementById("mycanvas").getContext("2d");
    ctx.strokeStyle = "green";
    ctx.beginPath();
    ctx.lineWidth = 3
    let c1 = getcoord(x1, y1)
    let c2 = getcoord(x2, y2)
    ctx.moveTo(c1.x_px + offsetx, c1.y_px + offsety);
    ctx.lineTo(c2.x_px + offsetx, c2.y_px + offsety);
    console.log(`. x1:${c1.x_px + offsetx} y1:${c1.y_px} x2:${c2.x_px + offsetx} y2:${c2.y_px}`)
    ctx.stroke();
}
function log(text) {
    console.log(text)
    document.getElementById("status").innerHTML = text
}
