name = 'Vds Chiu'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Black'
teeth = 'a littel bit yellow'
hair = 'Black'

c_height = height * 2.54
k_weight = weight * 0.45

print "Let's talk about %s" % name
print "He's %d centimeters tall." % c_height
print "He's %d kilograms heavy." % k_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print """My name is %r, my age is %r,
my eyes are %r, my teeth is %r,
and my hair is %r""" % (name, age, eyes, teeth, hair)
