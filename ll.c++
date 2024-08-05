#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int GRID_SIZE = 10;

// Structure to represent the car's position
struct Car {
    int x, y;
};

// Function to draw the grid
void drawGrid(Car car, int obstacles[][2], int numObstacles) {
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (i == car.y && j == car.x) {
                cout << "C "; // Car's position
            } else {
                bool isObstacle = false;
                for (int k = 0; k < numObstacles; k++) {
                    if (i == obstacles[k][0] && j == obstacles[k][1]) {
                        cout << "X "; // Obstacle's position
                        isObstacle = true;
                        break;
                    }
                }
                if (!isObstacle) {
                    cout << ". "; // Empty space
                }
            }
        }
        cout << endl;
    }
}

// Function to check if the car has hit an obstacle
bool hasHitObstacle(Car car, int obstacles[][2], int numObstacles) {
    for (int i = 0; i < numObstacles; i++) {
        if (car.x == obstacles[i][1] && car.y == obstacles[i][0]) {
            return true;
        }
    }
    return false;
}

int main() {
    srand(time(0)); // Seed the random number generator

    Car car;
    car.x = GRID_SIZE / 2;
    car.y = GRID_SIZE / 2;

    int numObstacles = 5;
    int obstacles[numObstacles][2];
    for (int i = 0; i < numObstacles; i++) {
        obstacles[i][0] = rand() % GRID_SIZE;
        obstacles[i][1] = rand() % GRID_SIZE;
    }

    while (true) {
        drawGrid(car, obstacles, numObstacles);

        char input;
        cout << "Enter direction (w, a, s, d): ";
        cin >> input;

        switch (input) {
            case 'w':
                car.y--;
                break;
            case 's':
                car.y++;
                break;
            case 'a':
                car.x--;
                break;
            case 'd':
                car.x++;
                break;
            default:
                cout << "Invalid input. Please try again." << endl;
                continue;
        }

        if (car.x < 0 || car.x >= GRID_SIZE || car.y < 0 || car.y >= GRID_SIZE) {
            cout << "Game over! You reached the edge of the grid." << endl;
            break;
        }

        if (hasHitObstacle(car, obstacles, numObstacles)) {
            cout << "Game over! You hit an obstacle." << endl;
            break;
        }
    }

    return 0;
}