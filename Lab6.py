#include <iostream>
#include <iomanip>
#include "windows.h"
#include "math.h"

using namespace std;

int main()
{
	int x, n, y;
	cout << "\nEnter x: ";
	cin >> x;
	y = 0;
	for (n = 1; n < 6; n++)
	{
		y += n;
	}
	cout << cos(y * x) + 5 + pow(x, 2);
}
