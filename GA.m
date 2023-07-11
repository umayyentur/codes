function = fx(c)

g = 2*c./(4+0.8*c+c.^2+0.2*c.^3);

function [p,yp] = golden(func,ab,eps,delta)
%verilen argumanim(girdi) sayisina gore eps delta degerlerini oto. al

if (nargin<5) delta = 1.0e-10; end
if (nargin<4) delta = 1.0e-10; eps = 1.0e-10 end

r = (sqrt(5)-1)/2;
h=b-a;
c=b-r*h;
d=a+r*h;
ya = feval(func,a);
yb = feval(func,b);
yc = feval(func,c);
yd = feval(func,d);
maxit = 200;
k=1;

while (abs(yb-ya)) > eps & (h>delta) & (k<maxit))
k = k+1;
if(yc>=yd)
    b = d;
    yb = yd;
    d = c;
    yd = yc;
    h = b-a;
    c = b-r*h;
    yc = feval(func,c);
else
    a = c;
    ya = yc;
    c = d;
    h = b-a;
    d = a+r*h;
    yd = feval(func,d);
    end
end

dp = abs(b-a);
dy = abs(yb-ya);
p = a;
yp = ya;
if(yb<ya)
    p = b;
    yp=yb;
end
if(k >maxit)
    uyari = "maksimum iterasyonu astiniz. Sonuc dogru olamayabilir"
    


