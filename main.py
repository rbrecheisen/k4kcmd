import os
import json

import matplotlib.pyplot as plt
import matplotlib.image as i


def show_figure(f):
    img = i.imread(f)
    plt.imshow(img)
    plt.show()


def main():
    
    # load course data
    with open('course.json', 'r') as f:
        course = json.load(f)
    
    # run through course lessons
    for lesson in course:
        for question in lesson['questions']:
            with open(question['file'], 'r') as f:
                os.system('clear')
                for line in f.readlines():
                    print(line.strip())
            if question['type'] == 'message':
                print()
                input('Druk op de enter toets om verder te gaan...')
            elif question['type'] == 'figure':
                print()
                input('Druk op de enter toets om verder te gaan')                
                show_figure(question['figure'])
            else:
                pass


if __name__ == '__main__':
    main()
