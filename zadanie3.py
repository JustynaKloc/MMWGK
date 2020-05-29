# xi = cos(ti)*(3+cos(ui))
# yi = sin(ti)*(3+cos(ui))
# zi=0.6*ti+sin(ui)

glBegin(GL_QUADS)
for t in range(0,T,dt): #(float t = 0 t < T t += dt)  
    sint = sinf(t)
    cost = cosf(t)
    sint2 = sinf(t + dt)
    cost2 = cosf(t + dt)
    c[0][0] = c[3][0] = RATIO * t / T
    c[1][0] = c[2][0] = RATIO * (t + dt) / T

    for u in range(0,U,du):#(float u = 0 u < U u += du) 
        sinu = sinf(u)
        cosu = cosf(u)
        sinu2 = sinf(u + du)
        cosu2 = cosf(u + du)

        v[0][0] = cost * (3 + cosu)
        v[0][1] = sint * (3 + cosu)
        v[0][2] = size * t / T + sinu
        n[0][0] = v[0][0] - cost * 3
        n[0][1] = v[0][1] - sint * 3
        n[0][2] = v[0][2] - size * t / T

        v[1][0] = cost2 * (3 + cosu)
        v[1][1] = sint2 * (3 + cosu)
        v[1][2] = size * (t + dt) / T + sinu
        n[1][0] = v[1][0] - cost2 * 3
        n[1][1] = v[1][1] - sint2 * 3
        n[1][2] = v[1][2] - size * (t + dt) / T

        c[0][1] = c[1][1] = u / U

        v[2][0] = cost2 * (3 + cosu2)
        v[2][1] = sint2 * (3 + cosu2)
        v[2][2] = size * (t + dt) / T + sinu2
        n[2][0] = v[2][0] - cost2 * 3
        n[2][1] = v[2][1] - sint2 * 3
        n[2][2] = v[2][2] - size * (t + dt) / T

        v[3][0] = cost * (3 + cosu2)
        v[3][1] = sint * (3 + cosu2)
        v[3][2] = size * t / T + sinu2
        n[3][0] = v[3][0] - cost * 3
        n[3][1] = v[3][1] - sint * 3
        n[3][2] = v[3][2] - size * t / T

        c[2][1] = c[3][1] = (u + du) / U

        for i in range(4): #(int i = 0 i < 4 i++) 
                glTexCoord2fv(c[i])
                glNormal3fv(n[i])
                glVertex3fv(v[i])
            
        
    
    glEnd()