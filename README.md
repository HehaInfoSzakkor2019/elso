# Bevezető
Info szakkör
  https://hehainfoszakkor2019.github.io/elso

# 2019. szeptember 16.
  * Mi a HTML? Mit jelent, hogy Hypertext Markup Language.
    * "Hiperszöveg leírónyelv" rövidítése angolul. Az a nyelv, amelynek segítségével weboldalakat lehet létrehozni. 
    * Egy HTML-oldal folyamatos kódolt szöveget tartalmaz, az oldal tartalma és a megjelenítéséhez szükséges elemek egyelege.
    * Az oldal végsõ formája a böngészõben jelenik meg (alakul ki), mert az értelmezi ezeket a megjelenítést szabályozó elemeket.
    * Elemek egymás utáni sorozata, az elemeket a böngészők jelenítik meg.
    * A különféle elemeket 'tag' -ek jelölik.
  * Első próba [w3schools](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default)
```html
<!DOCTYPE html>
<html>
<head>
<title>Cim</title>
</head>
<body>

<h1>Ez egy fejezet cim</h1>
<p>Ez egy bekezdes.</p>

</body>
</html>
```
  * Szöveg formázás
    * vastagítás... `<b>vastag</b>` vagy `<strong>vastag</strong>`
    * döntés... `<i>dőlt</i>` vagy `<em>ddd</em>`
    * aláhúzás... `<u>aláhúzott</u>`

# 2019. szeptember 23.
  * HTML alap formázások, gyakorlás
# 2019. szeptember 30.
  * Táblázatok elkezdése
    * `<table> <tr> <td>`
  * CSS elkezdése
```html
<style>
  table {
   border: 1px solid black;
   padding:0;
   margin:0;
  }
  tr {
   border: 1px solid blue;
  }
  td {
   border: 1px solid red;
  }
<style>
```
# 2019. október 7.
  * táblázat, a játék elrendetése
    * https://hehainfoszakkor2019.github.io/elso/tabla.html
    
# 2019. október 14.
  * Kedvcsinálónak: https://www.w3schools.com/code/tryit.asp?filename=G8XC4VWBQXOG
  * tábla szerkesztés, újra-alapozás.. "házi feladat":
    * https://www.w3schools.com/code/tryit.asp?filename=G8YEZI0KX84X
      * Használd a [HTML puskát](https://hehainfoszakkor2019.github.io/elso/html-puska-okt14.pdf) is!
    * Erről az oldalról kiindulva csináljátok meg a játék keretét, azaz
      * a tábla teljes képernyőt elfoglalja
        * ne legyen görgető az oldal szélén (margin:0) 
      * a két szélső oszlop szélessége 20% legyen, a középső rész 60%
      * a sarokban levő cellák magassága 25% legyen
      * a cellák keretét változtasd meg valamire, mindegy mire csak próbálgasd a lehetőségeket: vastagság, vonal, szín
      * a bal felső mezőben legyen a játék neve kiemelve (h2), alatta pár mondatan a játék leírása
      * a jobb felső sarokban legyen a nevetek, _**vastag és dőlt**_ betűvel 
      * a bal alsó sarokban legyen 2 kép, két BMW logo `https://www.carlogos.org/logo/BMW-logo-2000-640x550.jpg`
        * a képek legyenek úgy méretezve, hogy a 3 mindig elférjen, vagyis egy kép szélessége a cella szélességének 45%-a legyen
      * a jobb alsó sarokban ugyanaz, mint a bal alsó sarokban
  * HTML elemek
    * tábla: `<table> <tr> <td>`
    * kép: `<img src="https://www.carlogos.org/logo/BMW-logo-2000-640x550.jpg">`
  * CSS elemek - a **style** megadásával a kinézet szerkesztése
    * CSS stílus beállítás többféleképpen is lehet, mi kettőt használunk: a fejlécben
      * az első az össes **td** elemre vonatkozik
      * a második csak arra az egy **td** elemre
```html
<style>
td {
  border: 1px solid red;
}
</style>

<td style="border: 1px solid green">
```
  * CSS stílus elemek, ezeket elég használni. 

```css
border: 1px solid black;
height:100%;
width:30%;
max-height:90%;
max-width:30%;
padding:0;
margin:0;
border-collapse: collapse;
```
  * Használd a [HTML puskát](https://hehainfoszakkor2019.github.io/elso/html-puska-okt14.pdf) is!
  * tipp: Ha a cella mérete nem akkora, mint amekkorának szerinted lennie kellene, akkor két dolgot nézz meg:
     * elírtál-e valamit: pl width és widht
     * lehet hogy az tartalmazó elem méretét is meg kell adni. A **html** -ben van a **body**,
     * amin belül van a **table**
     * azaz nem elég a table szélességét beállítani, hanem a **html** és a **body** méretét is kell.
  * Ha elkészült, mentsd el az oldalad és küld el a címét a lovas12-szakkor@yahoo.com emailre.
     ![save](https://hehainfoszakkor2019.github.io/elso/w3schools-editor-save.jpg)
    * valahogy így kellene kinéznie
    * Ha bármivel elakadsz, nem világoss kérdezz bátran!
      * mentsd el ameddig eljutottál, küld el és megbeszéljük mi lehet a gond.
  * Javascipt alapok
    * alap függvények: alert, prompt, ...
    * matek: 
      * Math.random()
      * Mark.floor()
    * saját függvény
```javascript
function f1() {
  alert("hello");
}
```
   * függvény hívása a HTML oldalról:
```html
<button onclick="f1();">Hello</button>
```
  
# És ami még hátravan

  * Ékezetek és egyéb furcsa karakterek
    * A számítógépek angol ABC-t és az alapvető írásjeleket ismerik, azokon kívül kódok használatával írhatunk le másfajta betűket és : `&valami;`
      * Ahol ez a _valami_ lehet kód `#xxx` vagy `kódnév`.
      * `&Aacute;` | Á
      * `&aacute;` | á
      * `&frac12;` | 1/2
      * `&ouml;` | ö
      * `&#337; &#336;` | ő Ő
      * `&#369; &#368;` | ű Ű
    * lásd https://www.w3schools.com/html/html_entities.asp és  https://www.w3schools.com/html/html_symbols.asp
    * lásd https://www.w3schools.com/charsets/ref_utf_latin1_supplement.asp
    * https://sites.psu.edu/symbolcodes/languages/europe/hungarian/
  * Csináljuk saját oldalt!
    * lásd https://hehainfoszakkor2019.github.io/elso/1-minta.html
  * Színek
```
<body bgcolor="yellow">
```
   * [w3schools színek](https://www.w3schools.com/colors/default.asp)
      * https://www.w3schools.com/tags/ref_colornames.asp
      * https://www.w3schools.com/colors/colors_hex.asp
   * RGB - Reg Green Blue
      * Az RGB színtér egy olyan additív színmodell, ami a vörös, zöld és kék fény különböző mértékű keverésével határozza meg a különböző színeket.
      * Az RGB skálán egy színt az határoz meg, hogy milyen intenzitású a három komponense.
    * érdekesség: [hexclock](http://www.jacopocolo.com/hexclock/)

  * Címsor
  * Elrendezések
    * bekezdések.....`<p> szöveg </p>`
    * Új sor soremelés... `<br />`
    * szóköz... `&nbsp;`
    * középre `<center>aa</center>`
    * nézzük meg: [w3schools page intro](https://www.w3schools.com/html/html_intro.asp)
    * DIV - align
      * később
  * Nyomógomb
```
<button>Click me</button> 
```
  * Képek
    * tag attributomok, kiegészítő adatok
```
<img src="html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com"> 
```
  * Hivatkozások, linkek
    * kép, mint hivatkozás
  * valami
```
<a href="default.asp">
  <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;border:0;">
</a> 
```
  * gombok
```
      <button>Click me</button> 
```
  * Felsorolás, lista
    * később
  * táblázat
    * ajajaj
    * [HTML lecke](https://www.kataporta.net/tanf/leckek.php?kod=kod7)
  * háttérzene
    * [HTML lecke](https://www.kataporta.net/tanf/leckek.php?kod=kod9)
  * egyéb sorközi módisító
```  
<a> <abbr> <acronym>
<b> <bdo> <big> <br> <button>
<cite> <code>
<dfn> <em> <i>
<img> <input> <kbd>
<label> <map> <object> <output>
<q> <samp> <script> <select> <small>
<span> <strong> <sub> <sup> <textarea> <time> <tt> <var>
```
 * Stílusok, osztályok
   * [classes](https://www.w3schools.com/html/html_classes.asp)
 * Oldal elrendezés
   * [layout](https://www.w3schools.com/html/html_layout.asp)
     * table
     * CSS
       * [w3.css](https://www.w3schools.com/w3css/default.asp)
  * HTML5
    * [HTML5 elemek](https://www.w3schools.com/html/html5_new_elements.asp)
# 2020. március 9.
  * telefon érintőkijelző kezelés...
    * https://hehainfoszakkor2019.github.io/elso/js/landing2.html
    * styles...
```
	    * { margin: 0; padding: 0;
			-webkit-user-select: none;
			-khtml-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;
			outline: none;
			-webkit-tap-highlight-color: rgba(255, 255, 255, 0); /* mobile webkit */
		}
```
  * javascript functions
```
    function mystart_() {
      lander.sprite.sheet.src = lander.sprite.img_src
      let canv = document.getElementById("mycanvas");
      document.body.addEventListener("keydown", handleKeyDown, false);
      document.body.addEventListener("keyup", handleKeyUp, false);
			if ('ontouchstart' in window) {
			// canv, document
				window.addEventListener("touchstart", handleTouch, false)
				window.addEventListener("touchend", handleTouch, false)
				window.addEventListener("touchmove", handleTouch, false)
			}

      document.getElementById("div-canvas").style.backgroundImage = `url('${planet.image}')`
      let w = parseInt(document.getElementById("div-canvas").offsetWidth)
      canv.height = canv.offsetHeight;
      canv.width = canv.offsetWidth; //  just because it's needed...
      myrestart()
      gameLoop()
      time.loop = setInterval(gameLoop_, time.tickMs_)
    }

  	var mytouch = { id:0, x0:0, y0:0, dx:0, dy:0, x1:0, y1:0 }
    function handleTouch(event) {
  		event.preventDefault();
 	    if (event.type == 'touchstart' && event.touches.length == 1) {
				mytouch.id = 1
				mytouch.x0 = event.touches[0].clientX
				mytouch.y0 = event.touches[0].clientY - canv.clientTop;
			} else if (event.type == 'touchend' && event.touches.length <= 1) {
				mytouch.id = 0
				mytouch.dx = 0
				mytouch.dy = 0
			} else if (event.type == 'touchmove') {
				mytouch.dx = event.touches[0].clientX - mytouch.x0
				mytouch.dy = event.touches[0].clientY - mytouch.y0
			}
    }
```
   * 3. lépés
```
   function getInputs() {
			ret = []
			//log(`zz.${JSON.stringify(uiActions)}`)
			Object.keys(uiActions).forEach(x => {
				if (uiActions[x].some(r=> keysDown.includes(r))) {
					ret.push(x)
				}
			})
			if (mytouch.id != 0) {
				if (mytouch.dy < 10) {
					ret.push('up')
				}
				if (mytouch.dx < -20) {
					ret.push('left')
				} else if (mytouch.dx > 20) {
					ret.push('right')
				}
			}

			return ret
		}

    function isAnyPressed(keys) {
	    let ret = false
			if (keysDown.length > 0) {
			    ret = true
			}
			if (mytouch.id != 0) {
			    ret = true
			}
		  return ret
    } 
  
    function isWaitUntilNoInput() {
                //log(`l4.${JSON.stringify(event.touches[0].target)}`,4)
		    ret = (keysDown.length == 0) && (mytouch.id == 0)
			return ret
		}
                                                                      
   function messageDraw() {
     ...
  	  if (mytouch.id != 0) {
				let oy = Math.floor(canvrect.top);
				line(mytouch.x0, mytouch.y0 - oy, mytouch.x0 + mytouch.dx, mytouch.y0 + mytouch.dy - oy)
			}
    }
  
    function line(x1,y1,x2,y2)  {
			let r = Math.floor(Math.min(canv.offsetWidth, canv.offsetHeight) / 20);
            log(`ll:${HMAX}:${WMAX}:${Math.min(HMAX, WMAX)}:${r}`,4)
			ctx.beginPath();
			ctx.lineWidth = 3;
			ctx.arc(x1, y1, r, 0, 2 * Math.PI, false);
			ctx.strokeStyle = "blue";
			ctx.moveTo(x1, y1);
			ctx.lineTo(x2, y2);
			ctx.stroke();
		}

```                                                         

    
