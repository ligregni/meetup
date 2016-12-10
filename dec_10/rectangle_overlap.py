# Rectangle overlap

def normalize_rectangle(rectangle):
    p1,p2 = rectangle
    x1,y1 = p1
    x2,y2 = p2
    rx1 = min(x1,x2)
    rx2 = max(x1,x2)
    ry1 = min(y1,y2)
    ry2 = max(y1,y2)

    return rx1,ry1,rx2,ry2

def is_overlap(rectangle1, rectangle2):
    ax1,ay1,ax2,ay2 = normalize_rectangle(rectangle1)
    bx1,by1,bx2,by2 = normalize_rectangle(rectangle2)

    if (ax1 <= bx2 and ax2 >= bx1) and (ay1 <= by2 and ay2 >= by1):
        return True

    return False
