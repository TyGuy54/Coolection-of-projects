// TyGuy CLI
#include <iostream>
#include "windows/mainWindow.cpp"

int main(){
    // make a new window that greet the user with the title of the CLI tool (Porobably just going to call is TyGuy CLI)
    // the windo will be a little box
    // have the user able to cycle through some option and selectone to render a new window
    // have them be able to go back to the previous window
   
    Application app;

    app.update();
    app.draw();


	return 0;
}
