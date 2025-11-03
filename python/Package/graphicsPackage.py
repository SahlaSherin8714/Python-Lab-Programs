from Graphics.Dgraphics.cuboid import cuboidArea
from Graphics.Dgraphics.sphere import sphereArea
from Graphics.Dgraphics.cuboid import cuboidPerimeter
from Graphics.Dgraphics.sphere import spherePerimeter
from Graphics.rectangle import rectangle
from Graphics.circle import circle

print(f"Area of Cuboid is {cuboidArea(1,2,3)}")
print(f"Perimeter of Cuboid is {cuboidPerimeter(1,2,3)}")

print(f"Area of spere is {sphereArea(2)}")
print(f"Perimeter of Sphere is {spherePerimeter(2)}")

circle_area,circle_peri=circle(2)
print(f"Area of circle is {circle_area}")
print(f"Perimeter of circle is {circle_peri}")

a,b=3,5
rectangle_area,rectangle_peri=rectangle(a,b)
print(f"Area of rectangle is {rectangle_area}")
print(f"Perimeter of rectangle is {rectangle_peri}")

