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
