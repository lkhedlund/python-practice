my_name = 'Lars K. Hedlund'
my_age = 27 #not a lie
my_height = 75 #inches
my_height_ft = my_height * 0.083 #conversion to ft
my_weight = 155 #lbs
my_weight_kg = 155 * 0.45 #conversion to kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "Or %0.1f ft tall in Canada." % my_height_ft
print "\nIf you're weird, that's %e in scientific notation.\n" % my_height_ft
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "In kilograms he weighs %0.1f." % my_weight_kg
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the tea." % my_teeth

# this line is exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + 
	my_height + my_weight)