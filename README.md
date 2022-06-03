# cse210-04

Greed
    Classes:
        Actor: store and keep track of attributes and methods common to all actors
            *falling object: store points
        *Player: manage the player object and user input
        keyboard_service: manage user input
        video_service: manage the window and other graphic processess
        *director: run the game, points and interactions between objects
        color: manage and store colors
        point: manage and store location data
        cast: manage groups of actors
        *main:

Order
    keyboard_service
    video_service
    color
    point
    actor
    cast
    *falling_object
    *player
    *director
    *main


    Actor: 
        inherits:
            Color
            Point
        attributes:
            text
            font size
            position
            velocity
            color
        methods:
            set (attribute)
            get (attribute)
            move
    
    Falling object:
        inherits:
            Actor
        attributes:
            point value
        methods
            get point
            set point

    keyboard_service:
        attributes:
            cell size
        methods:
            get direction
    
    video service:
        use one from rfk as refrence

    director:
        inherits:
            video service
            keyboard service
        attributes:
            video service
            keyboard service
        methods:
            start game
            do inputs
            do updates
            do outputs

    color:
        attributes:
            R
            G
            B
            alpha
        methods:
            generate color

    point:
        attributes:
            x
            y
        methods:
            get x
            get y
            add
            scale
            equals

