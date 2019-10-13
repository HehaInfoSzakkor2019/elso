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
  * https://www.w3schools.com/code/tryit.asp?filename=G8XC4VWBQXOG
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
