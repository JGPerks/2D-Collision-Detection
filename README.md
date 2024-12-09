# Collision Detection Physics Simulation

Team Members: Jonathan, Adonis, Phoenix<br/> <br/>
### Project Overview:
  We will build a simple collision detection physics simulation utilizing
the import pygame to set up a game loop. The main problem with our project is that every 
particle(circle) drawn in the window, we must check if it collides with every other particle
on screen. Simplistic collision detection algorithms have a time complexity of O(n^2). Each 
particle tests against every other particle if its distance is <= their combined radius’s. If two 
circles have a radius of 5, and the total distance between them is 10 or less then they are 
either just colliding or inside of each other. This means in the next frame after we detect a 
collision, we need to move the two circles away from each other, so they don’t collide. If 
we have 100 particles, created using an array p[0] through p[99]. Then p[0] must check its
distance with the other 99 particles. Particle p[1] must do the same and so on. This of 
course destroys our simulations efficiency if we want a lot of particles. By implementing a 
quadtree we can determine to test particle collision by only checking each particle with
those in its vicinity, drastically increasing performance. A quadtree is an adaptation of a 
binary tree and runs with a time complexity of O(log n).<br/> <br/>
### Objectives:
- Create a simple collision detection algorithm
- Tests its run time with 100 particles drawn to the screen
- Implement a quadtree data structure into the collision detection algorithm
- Tests its run time with 100 particles drawn to the screen
- Compare runtimes from the simplistic collision detection algorithm and the 
quadtree implemented algorithm.
- Increase runtime efficiency for the 100 particles drawn to the screen<br/> <br/>
### Methodology:
  We start by having a window filled with 100 particles. We’ll take an initial 
time before running the collision detection algorithm, and a time after we run the algorithm 
to calculate our runtime. This will be done in a window not utilizing the quadtree data 
structure. We’ll run another test in a separate window with the quadtree implemented 
algorithm. From here we can compare the runtime efficiency.

### Expected Outcomes: 
I hope to have the working basics of a simple 2D physics engine that 
can detect the collision of circles. We should see an increase in performance and thereby
allowing us to increase the overall number of particles capable of being drawn to the 
screen. The runtime should improve from the initial collision detection algorithms runtime.

### Timeline: 
We’ll move on a week-by-week basis. A simple version of the collision detection
simulation will be done a week from when we start. Implementation of the quadtree will 
begin in week 2. We’ll begin finishing touches, fixing bugs, and cleaning up code during 
week 3, then run our tests. We’ll keep in touch at the start of each week and make a game 
plan on expected deliverables for the end of the week.
