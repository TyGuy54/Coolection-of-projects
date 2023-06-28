#include<raylib.h>

struct Paddle {
    Vector2 positions = {30, 150};
    Vector2 size = {10, 150};
    Color color = MAROON;
    float speed = 3.0f;
} paddle, paddle2;

struct Ball {
    Vector2 position = {350, 225};
    int size = 20;
    Color color = MAROON;
    Vector2 speed = { 4.0f, 3.0f };
} ball;

int main(void) {
    // Initialization
    //--------------------------------------------------------------------------------------
    const int screenWidth = 800;
    const int screenHeight = 450;

    Paddle paddle;
    Paddle paddle2;
    Ball ball;

    InitWindow(screenWidth, screenHeight, "Pong");
    paddle2.positions = {750, 150};

    SetTargetFPS(60);               // Set our game to run at 60 frames-per-second
    //--------------------------------------------------------------------------------------

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // Update
        //----------------------------------------------------------------------------------
        if (IsKeyDown(KEY_UP)) paddle.positions.y -= paddle.speed;
        if (IsKeyDown(KEY_DOWN)) paddle.positions.y += paddle.speed;

        if (IsKeyDown(KEY_W)) paddle2.positions.y -= paddle2.speed;
        if (IsKeyDown(KEY_S)) paddle2.positions.y += paddle2.speed;

        // Collision
        // if the paddle hits the top or bottom of the screen it wont faze through the screen
        if (paddle.positions.y >= (screenHeight - paddle.size.y)) {
            paddle.positions.y = screenHeight - 150;
        }
        if (paddle.positions.y <= 1) {
            paddle.positions.y = 1;
        }

        // Player 2 collisions
        if (paddle2.positions.y >= (screenHeight - paddle2.size.y)) {
            paddle2.positions.y = screenHeight - 150;
        }
        if (paddle2.positions.y <= 1) {
            paddle2.positions.y = 1;
        }

        // Bouncing ball logic
        ball.position.x += ball.speed.x;
        ball.position.y += ball.speed.y;

        // Ball collisions
        if ((ball.position.x >= paddle2.positions.x)) {
            ball.speed.x *= -1.0f;
        } 
        if ((ball.position.x <= paddle.positions.x)) {
            ball.speed.x *= -1.0f;
        } 
        if ((ball.position.y >= (screenHeight - ball.size)) || (ball.position.y <= ball.size)) {
            ball.speed.y *= -1.0f;
        } 

        //----------------------------------------------------------------------------------

        // Draw
        //----------------------------------------------------------------------------------
        BeginDrawing();

            ClearBackground(RAYWHITE);

            DrawRectangleV(paddle.positions, paddle.size, paddle.color);
            DrawRectangleV(paddle2.positions, paddle.size, paddle.color);

            DrawCircleV(ball.position, ball.size, ball.color);

        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    return 0;
}