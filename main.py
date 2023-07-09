import math


def projectile(u, theta, g=9.8):
    _R = ((u * u) * math.sin(2 * theta)) / g
    _H = ((u * u) * (math.sin(theta) ** 2)) / (2 * g)
    _T = (2 * u * math.sin(theta)) / g
    return _R, _H, _T


def projectileAtT(u, theta, t, g=9.8):
    xo=10
    yo=500
    y =yo+ u * math.sin(theta) * t - 0.5 * g * t ** 2
    x = xo+u * math.cos(theta) * t
    return x, y


def main():
    theta = 45
    theta *= math.pi / 180
    u = 100
    g = 9.8
    t = 1.3
    _Range, _Height, _Time = projectile(u, theta, g)
    x, y = projectileAtT(u, theta, t, g)
    print(f"{_Range=} {_Height=} {_Time=} {x=}, {y=}")


if __name__ == '__main__':
    main()
