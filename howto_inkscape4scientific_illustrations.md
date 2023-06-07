[Shortcut references (latest)](https://inkscape.org/doc/keys.html)
Notable ones:
- hold `ctrl` to change something "discretely"

Tools:
- `F1` or `s`: selector

# General
## Setup page
- Setup a two columns 4A paper using lines (to draw them: click and drag from the side rules; then you can fine-tuning position them by click on them and set the desired values): this helps you understand dimensions for the final figure (fit into one or both columns) and other details such as the font size (usually, 11 pt)
- A grid can be useful (shortcut: `shift+#`)

## The process to compose an illustration
1. Determine what you want to convey with a figure; show a process, highlight a feature etc.
    Address the sub-points: what people should understand? What part of the protein is relevant? etc
2. Sketch out a rough draft
3. Begin compiling
4. Get feedback

## Using in combination with plots
- Export plots in SVG format/vector graph to have minimal problems once you import the plot (`MATLAB`, `matplotlib` and others can do it easily)
- Do everything da you can in the plotting software, do not loose time modify a lot of objects in inkscape

# Basic operations
## Modify objects
### Edit path
There is a an important semantic difference between `object` and `path`. An `object` can be a square that is allowed to change only in fixed ways (ratio, border curvature etc.). A `path` can be modified at will. The shapes are `objects` with bezier's curves are `paths`.
One can convert objects into paths. For example, create a square, leave only the outline, then convert it to a path in order to modifying it.  

Edit path tool modify the selected object. Hold `crtl` and left mouse key to modify "rigidly" an obj, such as the line in a graph. Use this tool when you have to modify lines instead of the selector tool. This avoids modification of the curve thickness.  

One can split a path at a specific node by first selecting the node, then break the path (on the top menu) and then in `Path > Break apart`.
### Shapes
- Properties are display on top of the UI
- Once you draw a shape, in the right corner there are some points to modify borders. The edit tool let you do de same
- holding `shift` let you rotate around corners
### [Bazier's curves](https://youtu.be/A1Mqx5qK7fc)
One can create a straight line and add multiple node to modify it (when using the edit tool). Then, to modify it, hold `shift` and move the various point selected.

One can draw irregular, sinusoidal, shapes using the mode `Spiro` of the bezier tool. It is very handy. E.g. creating illustrations of soft objects such as cells. Similarly one can obtain a less curvy object using the `BSpiro` mode.

The straight modes are also useful to populate an illustration with dots and one can do so by holding `crtl` and clicking in the canvas.

To create fade-in/fade-out lines, one can select the triangular-in/triangular-out shapes, respectively.

## Position objects
- Moving while hitting `space` duplicate an object
### Align
Open dialog: `shift + crtl + A`

Object alignment is controlled thought the `align and distribute` dialog box. Selected objects (you can select multiple objects holding `shift`) are aligned by default with respect to the last object selected. This behavior can be changed, usually I prefer to aligh wrt the first selected.  

# Next level
## Complex shapes using object logic
These are collected in the `Path` menu. Important in these operations is which obj is below or above. For example: if we have a circle above a rectangle, using the division operation will cut the overlapping portion of the circle from the rectangle. On the other hand, if the circle is below, than the result will be the union of the two figures minus the overlap.

[Example composing a DNA](https://youtu.be/YijES28CmbI). The idea is to start with a single shape that we create from simpler ones (if this makes sense) and then use it as a building block for the rest oft he DNA structure. 

# References
- [Di Carlo Lab seminar](https://youtu.be/1XKHm8MJt1I)
- [Inkscape scientific tutorial playlist](https://youtu.be/eyqH0IrzYLc)
- [An example illustration of a phospholipid bilayer](https://youtu.be/r4YM_gMyLGs) and [one using the "Pattern along path"](https://youtu.be/e8INxPhpCdQ)