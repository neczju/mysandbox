#include <iostream>

using namespace std;

float bmi_calculation(float, float);
void bmi_text_output(float);

int main()
{
    float user_weigh{0};
    float user_height{0};

    system("clear");
    cout << "BMI CALCULATOR\n";
    cout << "BY NECZJU\n\n";
    cout << "HOW MUCH YOU WEIGH(IN KILOGRAMS)\n";
    cout << "? ";
    cin >> user_weigh;
    cout << "HOW TALL ARE YOU(IN CENTIMETERS)\n";
    cout << "? ";
    cin >> user_height;
    float bmi_result = bmi_calculation(user_weigh, user_height);
    cout << "YOUR BMI: " << bmi_result << endl;
    cout << "RESULT: ";
    bmi_text_output(bmi_result);
}

float bmi_calculation(float kilograms, float meters)
{
    meters = meters / 100; // centimeters to meters
    float result = kilograms / (meters * meters); // bmi formula
    return result;
}

void bmi_text_output(float bmi)
{
    if(bmi > 0)
    {
        if(bmi <= 16)
            cout << "SEVERE THINNESS\n";
        else if(bmi <= 17)
            cout << "MODERATE THINNESS\n";
        else if(bmi <= 18.5)
            cout << "MILD THINNESS\n";
        else if(bmi <= 25)
            cout << "NORMAL\n";
        else if(bmi <= 30)
            cout << "OVERWEIGHT\n";
        else if(bmi <= 35)
            cout << "OBESE CLASS I\n";
        else if(bmi <= 40)
            cout << "OBESE CLASS II\n";
        else if(bmi > 40)
            cout << "OBESE CLASS III\n";
    }
    else
        cout << "RESULT IS NEGATIVE?\n";

}
