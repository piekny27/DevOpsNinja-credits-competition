var agroSnap = Snap('#agro-tile');
var investSnap = Snap('#invest-tile');
var heroSnap = Snap('#hero');

Snap.load("/static/svg/credits_page.svg", onCreditsLoaded);

function onCreditsLoaded(svg){ 
    var pos = new Snap.Matrix();
    pos.translate(-975,-210).scale(0.97,0.97);

    var pos2 = new Snap.Matrix();
    pos2.translate(-500,-230).scale(1,1);

    var pos3 = new Snap.Matrix();
    pos3.translate(1,-227).scale(1,1);

    var g1 = agroSnap.group(
        svg.select('#Pozyczka_agro')
    );
    g1.attr({id:'kafelek1'}).transform(pos);
    agroSnap.add(g1);

    var g2 = agroSnap.group(
        svg.select('#defs'),
        svg.select('#Hero')
    );
    g2.attr({id:'kafelek2'}).transform(pos2);
    heroSnap.add(g2);

    var g3 = investSnap.group(
        svg.select('#Kredyt_investycyjny')
    );
    g3.attr({id:'kafelek3'}).transform(pos3);
    investSnap.add(g3);

    var eyeLeftQ = document.getElementById("eye_left");
    var eyeRightQ = document.getElementById("eye_right");

    document.onmousemove = function(){
        var x=event.clientX*100/window.innerWidth;
        var y=event.clientY*100/window.innerHeight;
        x= map_range(x,0,100,-3,3);
        y= map_range(y,0,100,-1,1);
        eyeLeftQ.style.transform = "translate("+x+"%,"+y+"%)";
        eyeRightQ.style.transform = "translate("+x+"%,"+y+"%)";
    }
}

function map_range(value, low1, high1, low2, high2) {
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1);
}