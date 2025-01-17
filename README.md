# mixamo-rig-joint-constraint
You may notice if you use a character that does not have human proportions, your mixamo animation on that character needs some work with collisions of body parts. Some of that seemed to do with some unnatural body positions due to issues with the way the mixamo site translates the animation of a human biped to (say) a cartoon monkey.
I am working on collision detection and other tools, but it occured to me if this was a problem with bone joint rotations, then why not simply put bone constraints on the joints?
Seemed to work a treat to remove some of the collisions, since they were (root cause) because of wrist over rotations especially.

The attached script applies a set of bone rotation limits (based upon humans and so representative of the source armature in the mixamo world view).  

Add or subtract as many or few bones, to/from "bone_constraints" dictionary, since you may not need constrain all bones to solve the collisions you're seeing.

Have fun animating.
## Twisted left and right wrists before running operator
![Alt text](pics/right%20wrist%20twist%20114.png)

## Twist limited to wrist joint limits after running operator
![Alt text](pics/right%20wrist%20untwisted%20114.png)

# Assumption
You are or are not using the Mixamo rig add-on (this only effects bones not control bones so seems to be fine (so far) ).

# Usage
1) Download https://github.com/OrganicMonkeyMotion/mixamo-rig-joint-constraint/blob/main/constrain_joints.py and stash it in your blender scripts folder.
2) Load constrain_joints.py into the Blender Text Editor tab.
3) Edit in/out as many joints you wish to put constraints upon.
4) Run constrain_joints.py from the Blender Text Editor tab.
5) In viewport (object mode), select armature.
6) F3 and search for and then run "Add Limit Rotation Constraints".

# Hints
Hands and fingers are often main culprits.  Wrists bent out of shape, fingers passing through one another or thumbs passing through hands.  May need some manual adjustments of control bones.
Note if you apply limits to fingers you may still get "collisions" but look at them intently, they'll often pass as fingers pressed and flesh compressed (given the often partial collision). That is, they won't be finger passing through bones in hand and out the other side but may pass as "natural" skin compression contact.  Up to your tastes as the animator.
