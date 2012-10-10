#include <math.h>
#include <stdio.h>

const float pi = 3.1415;

int main()
{
    float x0 = 0;
    float y0 = 0;
    float yf = -30;
    float g = -10;
    float theta = pi/4;
    float v = 30;

    float x, y, t;
    float xv, yv;
    float dt = .01;

    // Step forward in time while the ball is above ground
    t = 0;
    y = y0;
    while(y > yf){
        t+=dt;
        y = y0 + v * sin(theta)*t + g*t*t;
    }
    x = x0 + v + cos(theta)*t;

    printf("Landed at xf = %f", x);
}





