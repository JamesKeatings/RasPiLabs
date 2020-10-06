//
//	RadioactiveDecay.cpp
//	C++ script for UWS first year lab
//	Radioadctive Decay experiment
//	James Keatings
//	James.Keatings@uws.ac.uk
//


#include <iostream>  

using namespace std; 
  
// main function - 
// where the execution of program begins 
int main() 
{
	//Define variables
	int number = 1e6;
	const int loop_length = 11;
	const int sides = 3;
	int points_x[loop_length];
	int points_y[loop_length];
	points_x[0]=0;
	points_y[0]=number;
	int total = 0;
	int sum = 0;
	int x[sides+1]={0};

	for(int i=0; i < number; i++){
		x[rand() % 6] += 1;
	}

	for(int i=0; i <= sides; i++){
		cout << x[i] << endl;
	}

	for(int i=1; i < loop_length; i++){
		total = 0;
		for(int j=0; j < number; j++){
			if(rand() % sides-1 == 1) total++;
		}
		number -= total;
		sum = number + total;
		points_x[i] = i;
		points_y[i] = number;
		cout << "[" << i << "] Out of " << sum << " reamining nuclei, a total of " << total << " have decayed and " << number << " have not" << endl;
	}

	cout << "End of the experiment!" << endl;

	return 0; 
} 
