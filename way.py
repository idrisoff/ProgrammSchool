def odometer(oksana):
    rast = oksana[0]*oksana[1]
    for i in range(2, len(oksana)-1, 2):
        rast += oksana[i]*(oksana[i+1]-oksana[i-1])
    return rast