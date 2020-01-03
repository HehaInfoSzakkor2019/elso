import * from  'tugrasca.js';

    function Toll(_canvas, _width=1800, _height=900) {
        tmp = new Tugrasca(_canvas, _width, _height)

        // Hungarian localization
        tmp.tollatLe = tmp.penDown
        tmp.tollatFel = tmp.penUp
        tmp.vastagsag = tmp.setPenWidth
        tmp.menj = tmp.forward
        tmp.hatra = tmp.backward
        tmp.balra = tmp.left
        tmp.jobbra = tmp.right
        tmp.ugorj = tmp.jump
        tmp.ugorjIde = tmp.jumpTo
        tmp.szoveg = tmp.text
        tmp.szin=tmp.color
        tmp.torol=tmp.clear
        return tmp;
    };

