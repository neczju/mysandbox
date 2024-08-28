#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <time.h>
#include <string>

using namespace std;

int game_count{0};

int pc_score{0}; // scores
int user_score{0};

void game_calculation(string);
void error_msg();
void score_board(int, int);
void system_pause();

int main()
{
    int user_pick{0};
    string user_pick_text{""};

    bool hide_scoreboard = true; // program starts with scoreboard disabled

    while(true)
    {
        system("clear");
        cout << "ROCK PAPER SCISSORS THE GAME" << endl;
        cout << "\tBY NECZJU" << endl << endl;

        if(!hide_scoreboard)
            score_board(user_score, pc_score);

        cout << "WHAT DO YOU WANT TO PLAY?\n";
        cout << "1. ROCK\n";
        cout << "2. PAPER\n";
        cout << "3. SCISSORS\n";
        cout << "4. EXIT GAME\n\n";
        cout << "? ";
        cin >> user_pick;
        cout << endl;

        switch (user_pick) {
            case 1:
                cout << "YOU PICKED ROCK!\n";
                user_pick_text = "rock";
                game_calculation(user_pick_text);
                break;
            case 2:
                cout << "YOU PICKED PAPER!\n";
                user_pick_text = "paper";
                game_calculation(user_pick_text);
                break;
            case 3:
                cout << "YOU PICKED SCISSORS!\n";
                user_pick_text = "scissors";
                game_calculation(user_pick_text);
                break;
            case 4:
                exit(0);
                break;
            default:
                error_msg();
                break;
        }

        hide_scoreboard = false;
        ++game_count;
    }
}

void game_calculation(string user_pick_text) // this function returns output dependent on user input
{

    srand(time(NULL)); // randomizer
    int pc_random_pick{rand() % 3};

    string pc_pick_text{""};

    switch (pc_random_pick) {
        case 0:
            cout << "PC PICKED ROCK.\n";
            pc_pick_text = "rock";
            break;
        case 1:
            cout << "PC PICKED PAPER.\n";
            pc_pick_text = "paper";
            break;
        case 2:
            cout << "PC PICKED SCISSORS\n";
            pc_pick_text = "scissors";
            break;
    }

    if(user_pick_text == pc_pick_text)
    {
        cout << "We have a tie!\n";
        ++user_score;
        ++pc_score;
    }
    else if (user_pick_text == "rock" && pc_pick_text == "paper")
    {
        cout << "PC WINS!\n";
        ++pc_score;
    }
    else if (user_pick_text == "rock" && pc_pick_text == "scissors") {
        cout << "YOU WON!\n";
        ++user_score;
    }
    else if (user_pick_text == "paper" && pc_pick_text == "rock") {
        cout << "YOU WON!\n";
        ++user_score;
    }
    else if (user_pick_text == "paper" && pc_pick_text == "scissors")
    {
        cout << "PC WINS!\n";
        ++pc_score;
    }
    else if (user_pick_text == "scissors" && pc_pick_text == "rock") {
        cout << "PC WINS\n";
        ++pc_score;
    }
    else if (user_pick_text == "scissors" && pc_pick_text == "paper") {
        cout << "YOU WON!\n";
        ++user_score;
    }
    cout << endl;
    system_pause();
}

void error_msg()
{
    char minus{'-'};
    for(int x = 0; x < 3; ++x) // this is decoration loop
    {
        if(x != 1)
        {
            for(int i = 0; i <= 59; ++i) // if i will know how to get number of characters from string
            {
                cout << minus;
            }
        }
        else
        {
            cout << "---\t EXIT 0 YOU TRIED TO DO SOMETHING TERRIBLE!\t ---";
        }
        cout << endl;
    }
    exit(0);
}

void score_board(int user, int pc)
{
    cout << "GAME COUNTER: " << game_count << endl << endl;
    cout << "YOUR SCORE: " << user << endl;
    cout << "PC SCORE: " <<pc << endl << endl;
}

void system_pause()
{
    cout << "PRESS ANY KEY TO CONTINUE";
    getchar();getchar();
}
