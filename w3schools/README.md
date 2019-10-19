# Javascript
  * Alapozás:
    * bemutató
      * https://www.w3schools.com/js/js_whereto.asp
'''javascript
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
'''
    * HTML DOM
      * document.getElementById(id) 	Find an element by element id
      * document.getElementsByTagName(name) 	Find elements by tag name
      * document.getElementsByClassName(name) 	Find elements by class name
      * element.innerHTML =  new html content 	Change the inner HTML of an element
      * element.attribute = new value 	Change the attribute value of an HTML element
      * element.style.property = new style 	Change the style of an HTML element
      * element.setAttribute(attribute, value) 	Change the attribute value of an HTML element
      * https://www.w3schools.com/js/js_htmldom_document.asp
    * változó
'''javascript
var start_date=new Date();
var now = new Date();
document.getElementById('result').innerHTML=now - start_date;
'''
    * JS Events
      * https://www.w3schools.com/js/js_events.asp
    * időzítések
'''javascript
function startTimer() {
  start_date = new Date();
}
 setTimeout(startTimer, t); 
'''
      * megj: itt a startTimer mögött nincs (), mert nem hívjuk meg, a függvény is egy objektum
      * https://www.w3schools.com/js/tryit.asp?filename=tryjs_setinterval2
    * lista
'''javascript
  let r2 = results.slice();
  r2.sort();
  r2.sort(function(a, b){return a-b});
'''
  * Reflex játék
    * https://www.w3schools.com/code/tryit.asp?filename=G92UH4XVV6HQ
    * https://hehainfoszakkor2019.github.io/elso/w3schools/js1.html
   * Simons Reflex
     * 4 gomb, reflex
     * https://www.w3schools.com/code/tryit.asp?filename=G959A861TVEC
     * https://hehainfoszakkor2019.github.io/elso/w3schools/js3.html
   * Simon Says
     * 4 gomb, memória
