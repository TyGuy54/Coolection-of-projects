#include <SDL2/SDL.h>
#include <string>
#include <iostream>
#include "mainWindow.hpp"
using namespace std;


Application::Application(){
    // initialize the user window
    m_window = SDL_CreateWindow("Ty-CLI",
                                SDL_WINDOWPOS_CENTERED,
                                SDL_WINDOWPOS_CENTERED,
                                680, 480,
                                0);

    if(!m_window){
        std::cout << "Failed to create window\n";
        std::cout << "SDL2 Error: " << SDL_GetError() << "\n";
        return;
    }

    m_window_surface = SDL_GetWindowSurface(m_window);

    if(!m_window_surface){
        std::cout << "Failed to get window's surface\n";
        std::cout << "SDL2 Error: " << SDL_GetError() << "\n";
        return;
    }
}

Application::~Application(){
    SDL_FreeSurface(m_window_surface);
    SDL_DestroyWindow(m_window);
}

void Application::update(){
    bool keep_window_open = true;
    while(keep_window_open)
    {
        while(SDL_PollEvent(&m_window_event) > 0)
        {
            switch(m_window_event.type)
            {
                case SDL_QUIT:
                    keep_window_open = false;
                    break;
            }
        }

        draw();
    }
}

void Application::draw(){
    SDL_UpdateWindowSurface(m_window);
}

























