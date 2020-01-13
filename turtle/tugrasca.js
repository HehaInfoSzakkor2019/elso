// TuGraSca - Turtle Graphics Scaled
// copyright szalabala@yahoo.co.uk
// credits: 
//    https://cnx.org/contents/hTEMulu8@2/Turtle-graphics-with-the-HTML5-canvas
//    https://cnx.org/resources/bbd2f71ed14a04bfcc9c91f69f6500db1ab8cebd/TurtleGraphics.html

function TugrascaMinimal(_container, _width=1800, _height=900) {
    
    if (_typeof(_container) == 'String') {
        elem = document.getElementById(_container)
    } else {
        elem = _container
    }

    if (elem.nodeName == 'CANVAS') {
        this._mycanvas = elem
        this.ctx = this._mycanvas.getContext("2d")

        elem.width = elem.clientWidth
        elem.height = elem.clientHeight
    } else {
        console.log(`ERROR: wrong parameter in container: ${_typeof(_container)}`)
    }

    this.width = _width
    this.height = _height
    this.x = this.xa = 0
    this.y = this.ya = 0
    this.angleDeg = 0
    this.angleRad = 0
    this.directionDeg = 0
    this._penDown = false
    this.penColor = "#000000"
    this.penWidth = 1

    //console.log(`init: w:${_width} h:${_height} c.w:${this._mycanvas.width} c.cw:${this._mycanvas.clientWidth}  c.p.cw:${this._mycanvas.parentElement.clientWidth}`)


    this._xxmyresize = function() {
        if (this._mycanvas) {     // does the browser support 'canvas'?
            this._mycanvas.width = this._mycanvas.parentElement.clientWidth
            this._mycanvas.height = Math.floor(this._mycanvas.parentElement.clientHeight)
        }
    }


    this.penDown= function() {
        this._penDown=true
        return this
    }
    this.penUp= function() {
        this._penDown=false
        return this
    }
    this.jumpTo= function(x, y) {
        this.x = x
        this.y = y
        this.xa = x
        this.ya = y
        this.angleDeg = 0
        this.angleRad = 0
        return this
    }
    this.jump= function(dx, dy) {
        return this.jumpTo( this.x += dx, this.y += dy)
    }

    this.savePos= function() {
        this.angle0 = this.angleRad
        this.x0 = this.x
        this.y0 = this.y
    }
    this.loadPos= function() {
        this.angleRad = this.angle0
        this.x = this.x0
        this.y = this.y0
    }
    this.getPos= function() {
        return {x:this.x, y:this.y}
    }

    this.posToPx = function( x_, y_ ) {
        let sw = this._mycanvas.clientWidth;
        let sh = this._mycanvas.clientHeight;
        let rw = sw / this.width // screenwidth_per_canvaswith
        let rh = sh / this.height // screenheight_per_canvasheight
        let offset_x = (rh < rw) ? Math.floor((sw - rh*this.width) / 2) : 0
        let offset_y = (rh < rw) ? 0 : Math.floor((sh - rw*this.height) / 2) 
        let ratio = Math.min(rh,rw)

        px = { x: Math.floor(x_*ratio + offset_x), 
                y: Math.floor(sh - y_*ratio - offset_y) }
        //console.log(`  pos: ${x_}:${y_} -> screen=${sw}:${sh} rat=${rw}:${rh}  off=${offset_x}:${offset_y}\n  P:${px.x}:${px.y}`)
        return px
    }

    this.forward= function (length) {
        var x0 = this.x;
        var y0 = this.y;
        this.x += length * Math.sin(this.angleRad)
        this.y += length *  Math.cos(this.angleRad)
        if (this.ctx) {
            if (this._penDown) {
                p0 = this.posToPx(x0, y0)
                p1 = this.posToPx(this.x, this.y)
                //console.log(`fwd: p0=${x0}:${y0} -> ${p0.x}:${p0.y} to p1=${this.x}:${this.y} -> ${p1.x}:${p1.y}`)
                this.ctx.beginPath();
                this.ctx.lineWidth = this.penWidth;
                this.ctx.strokeStyle = this.penColor;
                this.ctx.moveTo(p0.x, p0.y);
                this.ctx.lineTo(p1.x, p1.y);
                this.ctx.stroke();
            }
        }
        else {
            this.ctx.moveTo(this.x, this.y);
        }
        return this;
    }
    this.backward= function (length) {
        this.forward(-length);
        return this;
    }

    this.right= function (angleInDegrees) {
        this.angleDeg += angleInDegrees
        this.angleRad = this.angleDeg * Math.PI / 180.0;
        return this;
    }
    
    this.left= function (angleInDegrees) {
        return this.right(-angleInDegrees)
    }
    this.setColor= function(color_) {
        this.penColor = color_
        return this
    }
    this.setPenWidth= function(width_) {
        this.penWidth = width_
        return this
    }
    this.text= function(text_, color_='black', font_='5vmin Comic Sans MS') {
        this.ctx.fillStyle = color_
        this.ctx.font = font_
        p = this.posToPx( this.x, this.y )
        this.ctx.fillText(text_, p.x, p.y);
    }
    this.clear= function() {
        this._mycanvas.getContext("2d").clearRect(0,0,this._mycanvas.clientWidth,this._mycanvas.clientHeight)
    }

    function _typeof( obj ) {
        return Object.prototype.toString.call( obj ).match(/\s(\w+)/)[1]
        // https://javascriptweblog.wordpress.com/2011/08/08/fixing-the-javascript-typeof-operator/
        // return ({}).toString.call( obj ).match(/\s(\w+)/)[1].toLowerCase();
    }

    this.simpleBorder= function() {
        let pen_save = this._penDown
        turtle._penDown = true
        for (i = 1; i <= 4; i++) {
            turtle.forward(i%2==0 ? turtle.width-1 : turtle.height-1);
            turtle.right(90);
        }
        turtle._penDown = pen_save;
    }
    
    function degToRad(angleDeg) {
        return angleDeg * (Math.PI / 180);
    }
};

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
Tugrasca = TugrascaMinimal
