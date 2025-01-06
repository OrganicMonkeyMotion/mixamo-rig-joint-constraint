# mixamo-rig-joint-constraint
You may notice if you use a character that does not have human proportions, your mixamo animation on that character needs some work with collisions of body parts. Some of that seemed to do with some unnatural body positions due to issues with the way the mixamo site translates the animation of a human biped to (say) a cartoon monkey.
I am working on collision detection and other tools, but it occured to me if this was a problem with bone joint rotations, then why not simply put bone constraints on the joints?
Seemed to work a treat to remove some of the collisions, since they were (root cause) because of wrist over rotations especially.

The attached script applies a set of bone rotation limits (based upon humans and so representative of the source armature in the mixamo world view).  

Add or subtract as many or few bones, to/from "bone_constraints" dictionary, since you may not need constrain all bones to solve the collisions you're seeing.

Have fun animating.

# Usage
1) In viewport, select armature.
2) F3 and search for "Add Limit Rotation Constraints".
