# POLYGON — Regular Polygon Solver for the TI-84 Plus

Give it **any one** of these about a regular polygon:

| You know | It solves for n using |
|---|---|
| Number of sides | n |
| Each exterior angle E | n = 360 / E |
| Each interior angle I | n = 360 / (180 − I) |
| Sum of interior angles S | n = S/180 + 2 |
| Number of diagonals D | n = (3 + √(9 + 8D)) / 2 |

Then it shows: the polygon's name, sides, each exterior angle (360/n), each
interior angle (180(n−2)/n), interior angle sum (180(n−2)), exterior sum (360),
and diagonals (n(n−3)/2). Press ENTER to **draw a picture** of the polygon,
with or without all its diagonals (diagonals are drawn for up to 25 sides).

If the number you type doesn't give a whole number of sides ≥ 3, it says
"NOT A REGULAR POLYGON". Rounded angles like 128.57 are fine.

![preview](preview.png)

## Installing

**Option A – send the file:** load `POLYGON.8xp` with TI Connect CE.

**Option B – type it in:** `PRGM` → `NEW` → name it `POLYGON`, then type each
line of `POLYGON.txt`. Commands come from menus, not by spelling them out:

| Command | Keys |
|---|---|
| `Degree`, `Float` | `MODE` (pick from the list while editing) |
| `Lbl`, `Goto`, `If`, `Then`, `For(`, `End`, `Pause`, `Menu(` | `PRGM` → CTL |
| `Input`, `Disp`, `Output(`, `ClrHome` | `PRGM` → I/O |
| `ClrDraw`, `Line(`, `Text(` | `2nd` `PRGM` (DRAW) |
| `AxesOff`, `GridOff`, `LabelOff` | `2nd` `ZOOM` (FORMAT) |
| `FnOff` | `VARS` → Y-VARS → On/Off |
| `PlotsOff` | `2nd` `Y=` (STAT PLOT) |
| `ZSquare` | `ZOOM` |
| `Xmin` `Xmax` `Ymin` `Ymax` | `VARS` → Window |
| `round(`, `abs(`, `fPart(` | `MATH` → NUM |
| `Str1` | `VARS` → String |
| `and`, `or`, `=`, `≤`, `≥`, `<`, `>` | `2nd` `MATH` (TEST / LOGIC) |
| `→` | `STO→` |
| `⁻` (negative) | `(-)` key, **not** minus |
| `√(` | `2nd` `x²` |

Note: the program switches the calculator to Degree mode.

`make_8xp.py` rebuilds `POLYGON.8xp` from `POLYGON.txt`.

---

# DIAGS — Sides ↔ Diagonals for the TI-84 Plus

A smaller program that does just one thing: turns a number of sides into a
number of diagonals, or the other way around.

| Menu choice | You type | It uses |
|---|---|---|
| SIDES TO DIAGS | number of sides n | D = n(n − 3) / 2 |
| DIAGS TO SIDES | number of diagonals D | n = (3 + √(9 + 8D)) / 2 |

Examples: 6 sides → 9 diagonals; 35 diagonals → 10 sides. If no polygon has
exactly that many diagonals (for example, 7), it says so.

Install it like POLYGON: send `DIAGS.8xp` with TI Connect CE, or create a
program named `DIAGS` and type in `DIAGS.txt` using the key table above.
Rebuild with `python3 make_8xp.py DIAGS.txt DIAGS.8xp`.

---

# INTANGLE — Interior Angle of a Regular Polygon

Type the number of sides n and it shows how many degrees are in **each**
interior angle, using I = 180(n − 2) / n.

Examples: 3 → 60, 4 → 90, 5 → 108, 6 → 120, 8 → 135, 7 → 128.5714286.

Send `INTANGLE.8xp` with TI Connect CE, or create a program named `INTANGLE`
and type in `INTANGLE.txt`. Rebuild with
`python3 make_8xp.py INTANGLE.txt INTANGLE.8xp`.

---

# ANGRATIO — Sides from How the Interior and Exterior Angles Compare

Solves word problems like *"How many sides does a regular polygon have if
each interior angle is 8 times its adjacent exterior angle?"* (answer: 18).

It uses the fact that an interior angle and its adjacent exterior angle add
to 180°, so it can find the exterior angle E, then n = 360 / E.

| Menu choice | Problem says | Exterior angle E |
|---|---|---|
| INT=K*EXT | interior is K times the exterior | 180 / (K + 1) |
| EXT=K*INT | exterior is K times the interior | 180K / (K + 1) |
| INT=EXT+D | interior is D degrees more than the exterior | (180 − D) / 2 |

It shows the number of sides, each interior angle and each exterior angle.
K can be a fraction (type `3/2`), and D can be negative if the interior is
*less* than the exterior. If the answer isn't a whole number of sides ≥ 3,
it says it's not a regular polygon.

Send `ANGRATIO.8xp` with TI Connect CE, or create a program named `ANGRATIO`
and type in `ANGRATIO.txt`. Rebuild with
`python3 make_8xp.py ANGRATIO.txt ANGRATIO.8xp`.
