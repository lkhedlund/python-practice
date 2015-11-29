'''A few notes before we begin

I'll separate my notes into three types, docstrings like this, whole line comments, and
inline comments. Docstrings will discuss the ideas behind the objects. What's the intent,
and what programming concepts do they present that are worth discussing. Full line comments
will discuss the details of the implementation. What the code is doing and why. Inline
comments will comprise a small portion of my notes, and are mostly to point out examples
mentioned in the rest of my notes, or return values. Another convention that I use is
backticks, which will be used to refer to an actual object in the code. If I say the word
one, it's just a word, but `one` is a reference to some object in code.
'''

# Not much to say here. Just some imports. I like the PEP8 style, but any convention is fine
# Note that they don't pollute the namespace by dumping everything from `random`
from sys import exit
from random import randint


# Think of a class like a blueprint to a house. It isn't the house, but it outlines what
# the house is, what features it will have and what structures are used. In Python 2,
# most classes will inherit from `object` to take advantage of new style classes. New style
# classes were introduced to combat issues like the diamond problem of multiple inheritance.
class Scene(object):
    """This class is what other languages might call an interface, or an abstract base class.
       The intent is not that it be used directly, but that it be subclassed by other classes,
       ensuring that they conform to the `Scene` interface. That they implement a `enter` method.
       Do a quick search and confirm that this class is never instantiated. As Python makes no
       Guarantees about interfaces being implemented, some choose not to follow this approach,
       myself included. This class effectively does nothing except to attempt to make the
       interface explicit, which can be useful.
   """

    # I'm not entirely sure of your experience with classes, so I'll explain methods.
    # Methods are just functions that belong to a class. That is to say that they're
    # in the scope or namespace of that class. You can access them using standard dot
    # notation (`Scene.enter`). The bit that can confuse Python programmers is the
    # `self` parameter. In most every method you encounter, you'll see `self` as the
    # first positional argument, and that has to do with descriptors. Descriptors can
    # be difficult to understand, so I'll leave that to Mr. Hettinger:
    # 
    # http://users.rcn.com/python/download/Descriptor.htm
    #
    # But simply put, that first positional argument will be passed a reference to
    # the instance that called the method:
    #
    #     foo = Scene()
    #     foo.enter()  # <= During execution of the `enter` method, `self` refers to `foo`
    #
    # The parameter isn't used in this method, but as it's passed as an argument,
    # you've got to have a parameter to accept it. We'll discuss this more later
    def enter(self):
        """This is the Python version of an abstract method. Kinda. I'd argue that
           it's more reasonable to raise the NotImplementedError exception. That's
           what it's there for. I can only assume that error handling hasn't been
           introduced, so feel free to ignore the above.
    
           What the method does is fairly obvious, simply informing the user that
           the class is intended to be subclassed and ceasing execution with an
           error state (the `1` argument to the call to `exit`).
    
           For more on exit status: http://en.wikipedia.org/wiki/Exit_status
        """
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    """This time, we have the first class that will actually do something. This class
       provides a namespace to store state, and a busy loop.
    """

    # You'll notice the following "dunder" (double underscore) convention in some
    # special methods in Python. These methods typically perform some task that
    # is called automatically. The `__init__` method that we see here will be
    # invoked when the class is instantiated. When we build the house.
    #
    # With this method, we have a second parameter. The `scene_map` object will
    # have a reference stored in the instance's "scene_map" attribute. This is where
    # we need to discuss the difference between instances and classes. Remember
    # how I said classes were like blueprints for a house? Instances are the house.
    # We follow the blueprint to create the house just as the interpreter instantiates
    # the object using the info from the class. Let's look at the process:
    #
    #     an_engine = Engine(some_mapping)
    #     different_engine = Engine(another_mapping)
    #
    # So we have two houses built from the same blueprint. What happens when we change
    # one house, do the other houses like it change to reflect our alteration? NO! And
    # neither are all instances altered when you muck about with one of them. If we
    # were to change the mapping in `an_engine`, we should not expect the
    # `different_engine` to be affected. But they're both calling the same `__init__`
    # method, why aren't they the same? It's because of that `self` parameter. When the
    # `Engine.__init__` method is invoked, that `self` parameter will be passed a
    # reference to the instance that is being created. So we're changing just that
    # object, not the class its self. There are means to alter the class, but as this
    # class does not do anything of the sort, I'll avoid and discussion in depth. Let's
    # say only that such methods are usually referred to as class or static methods.
    def __init__(self, scene_map):
        """The initial line is simply some means of logging activity. It's likely
           that logging hasn't been introduced, so I'll avoid it for now. This function
           will just report activity and assign a reference as an attribute.
        """

        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map  # `scene_map` is stored as an attribute

    def play(self):
        """This is the busy loop. The while-true loop will run for forever, or
           until a call to either the `enter` or `next_scene` throw an exception.
           This is where we see why an interface can be nice. The loop doesn't have
           to care what kind of scene it is, it just knows that each scene will
           implement a `enter` method. Other languages will guarantee this and
           throw errors during compilation, but not Python. It's the abstraction
           of the scenes that's useful. While some scenes might implement exotic
           behaviors, we know that at least they'll have the methods we're looking
           for. No reason to build all sorts of corner case handling with long
           ugly if/then chains if you can specify that all of the scenes will
           act a certain way. This is called polymorphism, and it's an important
           idea in programming. I'd suggest studying it from a more thorough
           source:

           http://en.wikipedia.org/wiki/Polymorphism_in_object-oriented_programming
        """

        # Calling the `opening_scene` method on the Map instance will return
        # a reference to the first Scene in that instance's `scenes` `dict`.
        current_scene = self.scene_map.opening_scene()
        # More logging that isn't logging
        print "Play's first scene", current_scene

        # Start of the busy loop
        while True:
            print "\n--------"
            # Whatever `Scene` instance is referenced by `current_scene` will have
            # its `enter` method invoked, which will return a `str` with the name...
            # Or rather, that method should return, but doesn't. This is where the
            # bug is noticed.
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            # Next, we call the `Map.next_scene` method and pass the scene name from
            # the above call to `enter`. This would return a `Scene` object. Do note
            # that when I call it a `Scene` object, it could also be any subclass.
            # We don't have to care because they all have `enter` methods.
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene


# This time, the class inherits from `Scene`. You can imagine that meaning that anything
# that was specified by the `Scene` class will hold true here as well. Unless you change
# it. Recall that `Scene` implements a `enter` method that's a stub/abstract/whatever.
# We will overwrite that method with one that hold behavior unique to this type of `Scene`.
# Being as `Death` is a subclass of `Scene`, we can treat it as a `Scene`, and I often do.
class Death(Scene):

    # Our first class variable! Note the lack of any reference to `self`? That means that
    # there's no instance involved. This is an attribute of the class. It's like writing
    # on the blueprint instead of on the wall of your house. The class/blueprint "owns"
    # the `quips` attribute. The attribute is an otherwise uninteresting `list` object.
    # Because of the name resolution, instances can refer to this object as well:
    #
    #     deathly_instance = Death()     
    #     print(deathly_instance.quips)  # Prints out the `Death.quips` `list`
    #     die_another_day = Death()
    #     die_another_day.quips.append("You're just roguelike fodder")
    #     print(deathly_instance.quips)  # Note that the added quip above can be seen
    #     die_another_day.quips is deathly_instance.quips  #=> True 
    #     Death.quips is deathly_instance.quips  #=> True 
    # 
    # What happened there? Well, since the `quips` attribute belongs to the class, not
    # the instance, your references to it will resolve to the same object. Again, the
    # `quips` object "belongs" to the `Death` class, not any of the instances. If you
    # reference it from an instance, that instance will check to see if it exists in
    # it's namespace (does it belong to me?). When it fails to find it, the interpreter
    # will check the type, or class of that instance. In this case, the type of the
    # instance is `Death`. The `Death` namespace does have a "quips" attribute, so it
    # will be used. That means that when I append my death line to the `quips` list,
    # it's the same list used by all of the instances of `Death`. Were one of the
    # instances define a `quips` attribute, it would be used instead. It all comes
    # down to the idea of name resolution. Name resolution is an important concept, and
    # I suggest you take some time to read over this article, or another like it:
    #
    # http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html
    #
    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    # Remember that talk about name resolution above? The same thing is happening here.
    # We've seen this before, but I want to use this as an example for a name resolution:
    # When a `Death` instance invokes the `enter` method, we need to find out what object
    # that refers to, and invoke it. The instance doesn't have `enter` defined in its
    # namespace (doesn't have an attribute/member/property called "enter"), so it goes to
    # the type of that instance, `Death`. The `Death` class does define an attribute called
    # "enter," so the resolution is finished and the `Death.enter` object is invoked. But
    # what if `Death` didn't have an `enter` method? The name resolution would look at the
    # type of `Death`, which is a `Scene`. Of course, the `Scene` class does specify an
    # `enter` method, so it would be used.
    def enter(self):
        """Pick a random member of the `Death.quips` `list` and print it, then exit
        """
        # I'd personally use `print(random.choice(self.quips)` but they're functionally
        # equivalent. This basically creates a range spanning from zero to the length of
        # the `Death.quips` `list` (though this one references it as an attribute of the
        # instance, doesn't matter, same object is referenced), and a number is chosen
        # from that range. That `int` is used as an index to lookup a member of `quips`
        print Death.quips[randint(0, len(self.quips)-1)]
        # I'd probably exit using `0` here as there was no error, but it doesn't matter
        exit(1)


class CentralCorridor(Scene):
    """Yet another subclass of the `Scene` class. Again, instances of the `CentralCorridor`
       class can be used as `Scene` objects.
    """

    def enter(self):
        """Again we have the `enter` method defined, as is suggested by the parent class.
           This method simply prints out some backstory and allows for a single interaction.
           Based on the user's input, a response is printed and a `str` returned. The `str`
           is used to specify some state. This is dirty, and referred to as "stringly typed."
           In any other language, an enum would be used, but Python only introduces enums in
           version 3.4 with PEP435. Instead, I'd use something like the following:
   
               shoot, dodge, tell_joke = range(3)
   	    actions = (shoot, dodge, tell_joke)
   
               action_taken = random.choice(actions)
               if action_taken is shoot:
                   "you shot stuff"
           
           This may not appear any different from the string version. I'm just using an `int`,
           how is that different? But I'm not just using an `int`! While integers have been
           assigned to each action, I'm referring to those actions, not the number that
           they hold. This allows me to take advantage of IDE or editor features like tab
           completion to ensure that I'm typing things correctly. This is not always reasonable
           with strings. Since Python 2 doesn't have an enum, use what you like, but be
           wary of string typing. More info on "stringly typed:"
   
           http://c2.com/cgi/wiki?StringlyTyped       
   
           Also note that each return value is a key of the `Map.scenes`, allowing the scene
           to be looked up as necessary. Still stringly typed, but it's acceptable.
        """

        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        # This part is somewhat interesting in that it's almost recursive. If the function receives
        # input that is unexpected, it will simply ask for the same method to be called again. It
        # stops short of calling its self, but the effect is the same. This is more elegant than
        # wrapping the whole damn thing in a loop and iterating until reasonable input is given.
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    """Yet another Scene type"""

    def enter(self):
        """This `enter` method is almost exactly like the last, in `CentralCorridor.enter`.
           Recall how I mentioned that the method was more elegant than looping over the whole
           thing? This is an example of that looping. It's otherwise unremarkable.
        """
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        # This is... interesting. They're building a three digit number using three calls
        # to `random.randint` and using formatting to turn them into a string. That's ugly.
        # 
        # code = str(randint(111, 999)
        # 
        # My example makes a single call to `random.randint` for any number between 111 and 999.
        # I'd rather use advanced string formatting:
        #
        #     "{:0>3}".format(randint(111, 999))
        #
        # Advanced string formatting supercedes the templating used in the original code.
        # You can read about advanced string formatting here:
        #
        # https://docs.python.org/2/library/string.html#format-string-syntax
        #
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        # Not terribly interesting: just loop, asking for input until the guesses are expended
        # I'm not thrilled about the way it's written. If the user somehow successfully guesses
        # the code, it is compared twice: once during the while-loop, and once after. Python
        # allows us some nice features to avoid this kind of ugly. I would have written it thusly:
        # 
        #     code = "{:0>3}".format(randint(0, 999))
        #     allotted_guesses = 10
        #
        #     for __ in range(allotted_guesses):
        #         players_guess = raw_input("[keypad]> ")
        #
        #         if players_guess == code:
        #             print(your_success_statement)
        #             return 'the_bridge'
        #     
        #     print(failure_statement)
        #     return 'death'
        # 
        # Couple of things that I'd like to mention about the above. First, I use a double
        # underscore in the for-loop to indicate that the index var is unused. For those of
        # you that prefer the single undescore, see this:
        #
        # http://docs.python-guide.org/en/latest/writing/style/#create-an-ignored-variable
        # 
        # From there, I just iterate over the number of allotted guesses, checking the user
        # input and moving to a success state if the guess is correct. If no guesses are
        # correct, and the number of attempts is expended, the for-loop completes and the
        # failure state is entered. Python isn't just about writing code, it's about writing
        # clean readable code. I'm being nitpicky and opinionated, to make that point.
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):
    """ Yet another `Scene` child. This one is nearly the same as `CentralCorridor`
        Consider that a "code smell." If you are doing nearly the same thing
        multiple times, try to generalize the approach and refactor such that
        only one routine is left to perform the desired actions. In fact, duplicate
        code is the first example of a code smell in Wikipedia's entry. In this case,
        I wouldn't bother. I simply wanted to bring up another programming concept
        For more on code smells, check out these links:

        http://en.wikipedia.org/wiki/Code_smell
        http://c2.com/cgi/wiki?CodeSmell
    """

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'


        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):
    """Same as above. I'm not going to bother commenting."""

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won! Now enjoy what time you have left while"
            print "you float impotently through the void."

            return 'finished'


class Map(object):
    """I don't like this class. Let's get to the 'why.' Firstly, I don't
       like the name. While that may seem terribly tangential, it matters.
       Python isn't explicitly typed, so we use our variable names to give
       indications as to what object is referenced, and what will be
       done with that object. "Map" is a common term in programming that
       refers to a `dict`, or associative array, and such a name implies
       that it will act like a mapping. But it doesn't, it adds some
       behavior to an encapsulated map. I like composition more than
       inheritance too, but let's keep our terms straight. I'd probably
       call this a SceneHandler or SceneDirector as it manages `Scene`
       objects instead of mapping them to some other object.

       Also worth mentioning that this class follows the facade pattern
       and simply wraps the `dict` that drives it. If you don't know what
       a pattern is, that's okay. Just ignore this and you'll remember it
       somewhere down the line.
    """

    # This is another example of a class attribute. That is to say that
    # `scenes` belongs to the `Map` object/class, or that it is in that
    # namespace. It's just a `dict` that maps string names for `Scene`s
    # to instances of those scenes (note the parens after the name,
    # indicating that the classes are being instantiated.
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()  # I prefer to have trailing commas
    }

    # Another special method! Same as last time, this will be invoked
    # when the class is instantiated, initializing the instance.
    # Also some print-style logging as discussed before.
    def __init__(self, start_scene):
        """This serves only to allow the user to specify what scene
           should be played first.
        """
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    # This is where we found the bug that broke the code. The omission
    # of a return statement caused things to break. Unlike Rust (and other
    # similar languages), Python does not return the last object in the
    # method/function automatically. If there is no explicit return value,
    # `None` is returned implicitly. All functions and methods without
    # return values return `None`. Do you remember the last time you
    # made the following mistake:
    #
    #     i_want_sorted_but_got_none = some_list.sort()
    #
    # I see it all the time in /r/learnpython. The method uses side-
    # effects to mutate the list instance that invoked it. It's a
    # convention to not return values from impure functions (functions
    # with side-effects), so the method returns `None`. The `some_list`
    # will be sorted, but that's not what you expected. This type of
    # problem is quite common, and thankfully easy to debug. Just look for
    # AttributeExceptions that mention None not having an attribute.
    def next_scene(self, scene_name):
        """This is a facade method that sits in front of the `Map.scenes`
           `dict`, and I haven't a clue why. Again, the name is bad too.
           It does not retrieve the next scene, it looks up the `Scene`
           object that is associated with the name passed as an argument.
           Given the name, I expected that the scenes were ordered, and that
           this method would return the scene that follows the argument
           that I pass. None of that is the case.
        """
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)  # Method is facade over this call
        print "next_scene returns", val
        # return val  #<= This would fix the method

    def opening_scene(self):
        """Looks like this was simply added to make things read nicer.
           I have zero problems with that so long as no complexity is
           added.
        """
        return self.next_scene(self.start_scene)


# I assume the if-main idiom hasn't been introduced. These should probably
# be wrapped in such a conditional in case the module is imported elsewhere.
# It would be unexpected behavior for a game to start playing when a module
# was simply imported. I suggest the following link for further reading:
#
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do

# First, we create a map object. Just call it `map`, we don't need smurf naming
# Note that we pass the name for a scene as our argument. The `Map.__init__`
# method will be invoked with a reference to the object being created (`a_map`),
# and the string, "central_corridor." That string will be stored as an attribute
# of the instance, to be used by the `opening_scene` method.
a_map = Map('central_corridor')
# Next we instantiate the `Engine`. The `Engine.__init__` will be called and passed
# a reference to the instance that called the method (`a_game`), and the `Map` to
# be used, which we just created.
a_game = Engine(a_map)
# Finally, we invoke the busy-loop method from `Engine` and the game starts up
# with the scene that we specified when creating a `Map`.
a_game.play()

