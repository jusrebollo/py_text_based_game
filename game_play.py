from game_classes import River_path
from game_classes import Mountain_path
import graphics
import time

if __name__ == '__main__':
    v = 1
    new_list = []
    while v == 1:
        try:
            file = open("answers_input.txt", 'r')
            lines = file.readlines()
            new_list = [line.split('\n') for line in open("answers_input.txt")]

            file.close()
            i = 0
            break
            # close file and end loop

        # catch errors and continue loop
        # if two errors thrown prevent crash by exiting

        except (FileNotFoundError, NameError) as error:

            print("FileNotFoundError: Incorrect file name or "
                  "file does not exist!")
            file.close()
            exit()
        # else only one error

        except FileNotFoundError:
            print("FileNotFoundError: Incorrect file name or "
                  "file does not exist!")
            file.close()
            v = 1
            continue
        except NameError:
            print("Name error!")
            file.close()
            v = 1
            continue
        except IndexError:
            print("Index error!")
            file.close()
            v = 1
            continue

    # have these be supplied by .txt
    choice_A = str(new_list[0])
    choice_B = str(new_list[1])

    yes = str(new_list[2])
    no = str(new_list[3])

    objects_on_path = {'stick': 10, 'rock': 25}
    weather_ops = ["Sunny", "cloudy"]

    rock = 0

    print(graphics.intro_graphic())
    print("Welcome to D.B. Cooper's Treasure Hunt!", '\n'
                                                     "Do you have what it "
                                                     "takes to find the "
                                                     "missing treasure?")
    user_name = input("What is your name: ")
    tell_legend = input("Your grandpa was an avid treasure hunter and has "
                        "left you a map to D.B. Cooper's treasure."'\n'
                        "Do you know the legend of D.B. Cooper? (Y/N): ")
    try:
        # make from text.txt input
        if tell_legend in no:
            print("")
            print("D.B. Cooper is a man who hijacked an aircraft in "'\n'
                  "the airspace over Oregon and Washington, on  Wednesday, "'\n'
                  "November 24, 1971. He demanded $200,000 in ransom for the "
                  ""'\n'
                  "hijacked plane. Once he received the ransom he parachuted "
                  ""'\n'
                  "in the wilderness of the Pacific Northwest. No one knows "
                  "if "'\n'
                  "he lived or if the ransom money is still amongst the "
                  "forest!")
            print("___" * 30)
        elif tell_legend in yes:
            print("Good for you! I hope you find the treasure!")
        else:
            print("Ok I guess you don't care!")

    except ValueError:
        print("Value Error: Yes or no!")

    except NameError:
        print("Name Error: Yes or no!")

    except TypeError:
        print("Type Error:Yes or no!")

    print("Ok now let's start looking for some treasure!")
    print("---" * 30)
    time.sleep(.75)
    print("The map takes you to a wooded region of the Cascade Mountains.")
    print("The area has mountain lions, bears and other dangerous"'\n'
          "obstacles. Be careful! ")
    print("---" * 30)
    time.sleep(.5)
    print("Before you is a path leading to a ragged mountain (A) and a path"'\n'
          "leading to a river which looks promising (B).")
    time.sleep(.5)

    i = 0
    r = 0
    while r == 0:
        path_choice = input("Which trail do you want to take? (A/B): ")
        if path_choice in choice_B:
            river = River_path(weather_ops[1])  # fix this supplied
            print(river)
            print(graphics.river_graphic())
            print("___" * 30)
            i = 1
            break
        if path_choice in choice_A:
            mountain = Mountain_path(weather_ops[0], 0)
            print(mountain)
            print(graphics.mountain_graphic())
            print("___" * 30)
            i = 2
            break
        else:
            continue

    if i == 1:
        print("Be aware the weather is", river.weather)
        print("You see a sign that says: ")
        print(repr(river))
        print("You see a sharp rock along the path!")

        # choice to pickup rock
        j = 0
        while j == 0:
            choice = input("Should you pick up the rock? (Yes/No) ")
            if choice in yes:
                rock = 1
                j = 1
                break
            if choice in no:
                rock = 0
                j = 1
                break
            else:
                j = 0
                continue
        # encounter mountain lion
        print("Oh no! You see a mountain lion in the distance")
        print(graphics.lion_graphic())
        print("---" * 30)
        time.sleep(1)
        print("The mountain lion sees you and begins to run towards you!")

        k = 0
        while k == 0:
            choice_2 = input("What should you do? Run or fight? (A/B) ")
            try:
                if (choice_2 in choice_B) and rock == 1:
                    print("You throw the rock at the mountain lion")
                    time.sleep(1)
                    print("It works the mountain lion runs off for now. "
                          "You live!")
                    print("---" * 30)
                    k = 1
                if (choice_2 in choice_B) and rock == 0:
                    print("You try to fight the mountain lion")
                    time.sleep(1)
                    print("It doesn't work the mountain lion kills you!")
                    time.sleep(1)
                    exit(0)
                    k = 1
                if choice_2 in choice_A:
                    print("You try to run from the mountain lion")
                    time.sleep(1)
                    print(
                        "The mountain lion catches you! You die :( Better try "
                        "again!")
                    time.sleep(1)
                    exit(0)
                else:
                    break

            except ValueError:
                print("Value Error: Yes or no!")
                continue

            except NameError:
                print("Name Error: Yes or no!")
                continue

            except TypeError:
                print("Type Error:Yes or no!")
                continue
        l = 0
        while l == 0:
            print("You continue down the river")
            time.sleep(.75)
            print("You see something glimmering in the water!")
            time.sleep(.75)
            print("---" * 30)
            choice_4 = input("Do you want to jump in the water? (Y/N)")
            if choice_4 in yes:
                print("You dive into the water")
                time.sleep(.75)
                print("The current is strong")
                print("You swim deeper and see a parachute")
                choice_6 = input("Looks like there is no treasure here. Do you "
                                 "want to give up or head to the mountain "
                                 "path? (A/B) ")
                if choice_6 in choice_A:
                    print("Treasure hunting isn't for everyone! Thanks for"
                          " playing!")
                    exit(0)
                if choice_6 in choice_B:
                    print("You walk back towards the mountain trail")
                    print("Be careful of falling off!")
                    l = 1
                    k = 1
                else:
                    continue

            if choice_4 in no:
                print("You walk along the river")
                time.sleep(.75)
                print("---" * 30)
                choice_5 = input("The path dead ends. Do you want to give up"
                                 " or backtrack to the mountain path? (A/B) ")
                if choice_5 in choice_A:
                    print("Treasure hunting isn't for everyone! Thanks for"
                          "playing!")
                    exit(0)
                if choice_5 in choice_B:
                    print("You walk back towards the mountain trail")
                    print("Be careful of falling off!")
                    l = 1
                    k = 1
                else:
                    continue

    if i == 2:
        print("Be aware the weather is", mountain.weather)
        print("You see a sign that says: ")
        print(repr(mountain))
        print("You see a sharp rock along the path!")

    # choice to pickup spear
    print("You see a spear along the path!")
    print("---" * 30)

    j = 0
    while j == 0:
        choice_3 = input("Should you pick up the spear? (Yes/No) ")
        if choice_3 in yes:
            print()
            rock = 1
            j = 1
        if choice_3 in no:
            print()
            rock = 0
            j = 1
        else:
            continue

    print("Oh no! You see a bear in the distance")
    print(graphics.bear_graphic())
    time.sleep(1)
    print("---" * 30)
    print("The bear sees you and begins to run towards you!")

    # encounter bear
    k = 0
    while k == 0:
        choice_2 = input("What should you do? Run or fight? (A/B) ")
        if (choice_2 in choice_B) and rock == 1:
            print("You throw the spear at the bear ")
            time.sleep(1)
            print("It works the bear runs off for now. You live!")
            print("---" * 30)
            k = 1
        if (choice_2 in choice_B) and rock == 0:
            print("You try to fight the bear")
            time.sleep(1)
            print("It doesn't work the bear kills you!")
            time.sleep(1)
            exit(0)
            k = 1
        if choice_2 in choice_A:
            print("You try to run from the bear")
            time.sleep(1)
            print(
                "The bear catches you! You die :( Better try again!")
            time.sleep(1)
            exit(0)
            k = 1
        else:
            continue

    # fall off cliff or not
    print("You walk further along the mountain path. The path narrows to a"
          "tiny path along a cliff edge and a sheer drop!")
    print("---" * 30)
    m = 0
    while m == 0:
        print("You see what looks like an abandoned shelter near the top of "
              "the mountain")
        choice_7 = input("Do you want to go explore the shelter or give up?"
                         "(A/B)")
        if choice_7 in choice_A:
            print("You continue up the path and can see the shelter and what"
                  " looks like a lock box")
            print("---" * 30)
            m = 1
        if choice_7 in choice_B:
            print("Thank you for playing! You shouldn't give up that easily!")
            exit(0)
            m = 1
        else:
            continue

    print("You see the lock box has a combination lock")
    print("You see a piece of paper next to the lock box")
    print("---" * 30)
    print("I was unable to make it off the mountain but to whoever finds my\n"
          "treasure, you must solve one simple riddle to get to it,\n"
          "the riddle provides the first three numbers to the combo and the\n"
          "length of the answer is the last number of the combo-\n"
          ""
          "What walks on four legs in the morning, two legs at noon,\n "
          "and three legs in the evening?\n"
          ""
          ""
          ""
          "Signed, D.B. Cooper December 2, 1971")
    print("---" * 30)

    answer = ("human", "Human", "person", "Person", "people", "People")
    n = 0
    while n == 0:
        final_question = input("What is the answer to the riddle? (No spaces)")
        if final_question in answer:
            print("You got it right!")
            n = 1
        if final_question not in answer:
            print("Here's a hint it's not a man or woman but a....")
            continue
        else:
            continue

    x = 0
    while x == 0:
        final_lock = input("What is the combination to the lock?")
        if final_lock == '4235':
            print("You got it right!")
            mountain = Mountain_path(weather_ops[0], 0)
            mountain._Mountain_path__treasure_value = 1
            print(mountain._Mountain_path__treasure_private(1))
            print(graphics.treasure_graphic())
            x = 1
            print("THANK YOU FOR PLAYING!")
            print("Game by Justin Rebollo")
            exit(0)
        if final_lock != '4235':
            continue
        else:
            continue
