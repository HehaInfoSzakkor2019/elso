//import * from tugrasca.js
// TuGraSca - basic shapes addition
function Tugrasca(_container, _width=1800, _height=900) {
    let t=new TugrascaMinimal(_container, _width, _height)

    t.square = function(a) {
        i = 1
        while (i <= 4) {
          turtle.forward(a)
          turtle.right(90)
          i += 1
        }
    }
   
    t.drawRegularShape= function(numEdge,lenEdge) {
        for (i = 1; i <= numEdge; i++) {
            turtle.forward(lenEdge);
            turtle.right(360/numEdge);
        }
        return this
    }
    t.drawRegularShapeByDiag= function(numEdge,diag_) {
        this.savePos()
        //this.jump(2*diag_/(numEdge+2), -diag_/4)//- diag_/5.5)
        this.jump(0, -diag_/3)//- diag_/5.5)
        //turtle.left(90);
        a_ = 180 * (numEdge - 2) / numEdge
        turtle.left(a_ / 2);
        this.drawRegularShape(numEdge, diag_ * Math.sin(degToRad(180/numEdge)))
        this.loadPos()
        return this
    }
    t.triangle= function(lenEdge) {
        return this.drawRegularShape(3,lenEdge)
    }
    t.square= function(lenEdge) {
        return this.drawRegularShape(4,lenEdge)
    }
    t.hexagon= function(lenEdge) {
        return this.drawRegularShape(6,lenEdge)
    }


    function betucsillag( betu ) {
        csillag2(36)
        turtle.szoveg(betu, getRandomColor())
    } 
    
    function csillag( hossz ) {
        turtle.color(getRandomColor())
        i = 1
        while (i <=9) {
            turtle.menj(hossz);
            turtle.balra(110);
            turtle.menj(hossz);
            turtle.jobbra(150);
            i += 1
        }
    } 
    
    
    function csillag1( hossz) {
        i = 1
        while (i<=5) {
            turtle.menj(hossz)
            turtle.jobbra(144)
            i += 1
        }
    }
    function csillag2(hossz ) {
        turtle.jump(-1, -40)
        turtle.color(getRandomColor())
        i = 1
        while (i <=9) {
            turtle.menj(hossz);
            turtle.balra(110);
            turtle.menj(hossz);
            turtle.jobbra(150);
            i += 1
        }
        turtle.jump(1, 40)
    } 
    
	function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
		var color = '#';
		for (var i = 0; i < 6; i++ ) {
            color += letters[Math.floor(Math.random() * 16)];
		}
		return color;
    }
    
    function rajzoljKeretet(  ) {
        for (i = 1; i <= 4; i++) {
            turtle.forward(i%2==0 ? turtle.width-1 : turtle.height-1);
            turtle.right(90);
        }
    }
    return t
}
    