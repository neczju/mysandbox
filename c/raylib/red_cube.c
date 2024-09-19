#include "raylib.h"

int main(void)
{
	const int screenWidth = 640;
	const int screenHeight = 480;
	InitWindow(screenWidth, screenHeight, "red_cube");
	ToggleFullscreen();

	SetTargetFPS(60);

	while(!WindowShouldClose())
	{
		BeginDrawing();

			ClearBackground(RAYWHITE);
			DrawRectangle(320, 240, 20, 20, RED);

		EndDrawing();
	}

	CloseWindow();
	return 0;
}
