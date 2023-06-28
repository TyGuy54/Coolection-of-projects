#pragma once

#include <SDL2/SDL.h>
#include <iostream>

class Application{
    // a simple class to easily make windows
    public:
        Application();
        ~Application(); //deconstructer

        void update();
        void draw();
        
    private:
        SDL_Window *m_window;
        SDL_Surface *m_window_surface;
        SDL_Event m_window_event;
};
